import logging
import os
import time
from typing import Dict, Optional

import httpx


class ModelLoader:
    """
    Load and interact with an AI model via LM Studio's OpenAI-compatible API.

    Attributes:
        model_name (str): The name of the model to use.
        base_url (str): Base URL of the LM Studio API.
        context_window (int): Maximum tokens to generate in a single call.
    """

    def __init__(
        self,
        model_name: str,
        client: Optional[httpx.Client] = None,
        base_url: str = "http://localhost:1234",
        request_timeout: Optional[float] = None,
        max_retries: int = 2,
        retry_backoff_seconds: float = 1.5,
        max_output_tokens: Optional[int] = None,
    ):
        """
        Initialize the ModelLoader with the model name and base URL.

        Args:
            model_name (str): The name of the model to use.
            client (Optional[httpx.Client]): Optional injected HTTP client.
            base_url (str): Base URL of the LM Studio API.
        """
        self.base_url = base_url
        self.model_name = model_name
        self.client = client or httpx.Client(base_url=base_url, timeout=60.0)
        env_context_window = os.getenv("EMS_CONTEXT_WINDOW")
        self.context_window = (
            int(env_context_window) if env_context_window is not None else 32768
        )
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

        # Configurable behavior via parameters or environment variables
        # Using env vars keeps CLI unchanged while allowing tuning at runtime.
        self.request_timeout = request_timeout or float(
            os.getenv("EMS_HTTP_TIMEOUT_SECONDS", "60")
        )
        self.max_retries = max(0, int(os.getenv("EMS_HTTP_MAX_RETRIES", max_retries)))
        self.retry_backoff_seconds = float(
            os.getenv("EMS_HTTP_RETRY_BACKOFF_SECONDS", retry_backoff_seconds)
        )
        # Limit output tokens to avoid extremely long generations by default.
        # Can be overridden via parameter or env var.
        env_max_tokens = os.getenv("EMS_MAX_OUTPUT_TOKENS")
        if env_max_tokens is not None:
            self.max_output_tokens = int(env_max_tokens)
        elif max_output_tokens is not None:
            self.max_output_tokens = int(max_output_tokens)
        else:
            self.max_output_tokens = 32768

    def _get_options(self) -> Dict[str, int]:
        """
        Construct options for generation.

        Returns:
            dict: Options for the model prompt.
        """
        # Cap the generation tokens to a sensible default to avoid long runs.
        return {"max_tokens": min(self.context_window, self.max_output_tokens)}

    def generate(self, prompt: str) -> str:
        """
        Generate a response from the AI model for the provided prompt.

        Args:
            prompt (str): The input prompt for the model.

        Returns:
            str: The generated response from the model.
        """
        try:
            if isinstance(prompt, dict):
                # Ensure prompt is a string
                prompt = prompt["prompt"]
            options = self._get_options()
            max_tokens = options["max_tokens"]
            self.logger.info("Max tokens: %s", max_tokens)
            self.logger.debug(f"Prompt: {prompt}")

            payload = {
                "model": self.model_name,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
                "max_tokens": max_tokens,
            }
            url = "/v1/chat/completions"

            last_exc: Exception | None = None
            for attempt in range(self.max_retries + 1):
                try:
                    resp = self.client.post(
                        url, json=payload, timeout=self.request_timeout
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    return data["choices"][0]["message"]["content"].strip()
                except (
                    httpx.ReadTimeout,
                    httpx.ConnectError,
                    httpx.ConnectTimeout,
                ) as exc:
                    last_exc = exc
                    if attempt >= self.max_retries:
                        break
                    sleep_multiplier = attempt + 1
                    sleep_seconds = self.retry_backoff_seconds * sleep_multiplier
                    self.logger.warning(
                        "Request attempt %s failed (%s). Retrying in %.1fs...",
                        attempt + 1,
                        exc.__class__.__name__,
                        sleep_seconds,
                    )
                    time.sleep(sleep_seconds)
                except httpx.HTTPStatusError as exc:
                    # Retry on common transient status codes
                    status = exc.response.status_code if exc.response else None
                    transient = status in {429, 500, 502, 503, 504}
                    if transient and attempt < self.max_retries:
                        sleep_multiplier = attempt + 1
                        sleep_seconds = self.retry_backoff_seconds * sleep_multiplier
                        self.logger.warning(
                            "HTTP %s on attempt %s. Retrying in %.1fs...",
                            status,
                            attempt + 1,
                            sleep_seconds,
                        )
                        time.sleep(sleep_seconds)
                        last_exc = exc
                        continue
                    raise

            # If we get here, retries were exhausted
            if last_exc is not None:
                raise last_exc
            raise RuntimeError("Unknown error")
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            raise RuntimeError(f"Error generating response: {e}")
