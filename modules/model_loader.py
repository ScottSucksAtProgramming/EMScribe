from langchain_community.llms.ollama import Ollama
from typing import Optional, Dict
import logging


class ModelLoader:
    """
    A class to load and interact with AI models.

    Attributes:
        model_name (str): The name of the model to use.
        base_url (str): The base URL of the model API.
        context_window (int): The maximum context window size for the model.
    """

    def __init__(
        self,
        model_name: str,
        client: Optional[Ollama] = None,
        base_url: str = "http://localhost:11434",
    ):
        """
        Initializes the ModelLoader with the specified model name and base URL.

        Args:
            model_name (str): The name of the model to use.
            client (Optional[Ollama]): An instance of the Ollama client. Defaults to None.
            base_url (str): The base URL of the model API.
        """
        self.base_url = base_url
        self.model_name = model_name
        self.client = client or Ollama(base_url=base_url)
        self.context_window = 32768  # Fixed context window size
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)  # Ensure logging is configured

    def _get_options(self) -> Dict[str, int]:
        """
        Constructs the options for the model prompt.

        Returns:
            dict: The options for the model prompt.
        """
        return {"num_ctx": self.context_window}

    def generate(self, prompt: str) -> str:
        """
        Generates a response from the AI model based on the provided prompt and context window.

        Args:
            prompt (str): The input prompt for the model.

        Returns:
            str: The generated response from the model.
        """
        try:
            if isinstance(prompt, dict):
                prompt = prompt["prompt"]  # Ensure prompt is a string
            options = self._get_options()  # Get options including context window size
            self.logger.info(
                f"Generating response with context window: {self.context_window}"
            )
            self.logger.debug(f"Prompt: {prompt}")

            response = self.client.generate(
                model=self.model_name,  # Include the model name
                prompts=[prompt],  # Pass the prompt as a list of strings
                options=options,  # Pass options including context window size
            )
            # Access the text from the response object
            return response.generations[0][
                0
            ].text  # Adjusting to access the first text item
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            raise RuntimeError(f"Error generating response: {e}")
