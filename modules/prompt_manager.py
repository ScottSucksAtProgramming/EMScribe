from typing import Any, Dict, Union

from modules.prompts import (
    cleaning_prompts,
    extraction_prompts,
    narrative_prompts,
    review_prompts,
)


class PromptManager:
    """
    Manages prompts for various tasks such as extraction, cleaning, narrative generation,
    and quality control.
    """

    def __init__(
        self,
        prompts: Dict[str, Union[str, Dict[str, str]]] = None,
        context_window_size: int = 32000,
    ):
        """
        Initializes the PromptManager with a dictionary of prompts.

        Args:
            prompts (Dict[str, Union[str, Dict[str, str]]], optional): A dictionary of prompts. Defaults to None.
            context_window_size (int): The maximum context window size for the prompts.
        """
        if prompts is None:
            prompts = {
                **extraction_prompts.extraction_prompts,
                **cleaning_prompts.cleaning_prompts,
                **narrative_prompts.narrative_prompts,
                **review_prompts.review_prompts,
            }
        self.prompts = prompts
        self.context_window_size = context_window_size

    def get_prompt(
        self, key: str, **kwargs: Any
    ) -> Union[str, Dict[str, str], list[str]]:
        """
        Retrieves a prompt template and formats it with the provided keyword arguments.

        Args:
            key (str): The key for the prompt template.
            **kwargs: Keyword arguments to format the template.

        Returns:
            Union[str, Dict[str, str], list[str]]: The formatted prompt.

        Raises:
            KeyError: If no prompt is found for the given key.
        """
        prompt_template = self.prompts.get(key)
        if not prompt_template:
            raise KeyError(f"No prompt found for key: {key}")

        if isinstance(prompt_template, dict):
            return {k: v.format(**kwargs) for k, v in prompt_template.items()}

        formatted_prompt = prompt_template.format(**kwargs)

        if len(formatted_prompt) > self.context_window_size:
            prompt_chunks = [
                formatted_prompt[i : i + self.context_window_size]
                for i in range(0, len(formatted_prompt), self.context_window_size)
            ]
            return prompt_chunks

        return formatted_prompt
