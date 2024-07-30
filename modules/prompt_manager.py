# modules/prompt_manager.py

from modules.prompts import (
    cleaning_prompts,
    extraction_prompts,
    narrative_prompts,
    review_prompts
)


class PromptManager:
    """
    Manages prompts for various tasks such as extraction, cleaning, narrative generation, and quality control.
    """

    def __init__(self):
        """
        Initializes the PromptManager with a dictionary of prompts.
        """
        self.prompts = {
            **extraction_prompts.extraction_prompts,
            **cleaning_prompts.cleaning_prompts,
            **narrative_prompts.narrative_prompts,
            **review_prompts
        }

    def get_prompt(self, key: str, **kwargs) -> str:
        """
        Retrieves a prompt template and formats it with the provided keyword arguments.

        Args:
            key (str): The key for the prompt template.
            **kwargs: Keyword arguments to format the template.

        Returns:
            str: The formatted prompt.

        Raises:
            KeyError: If no prompt is found for the given key.
        """
        prompt_template = self.prompts.get(key)
        if prompt_template:
            if isinstance(prompt_template, dict):
                return {k: v.format(**kwargs) for k, v in prompt_template.items()}
            else:
                return prompt_template.format(**kwargs)
        else:
            raise KeyError(f"No prompt found for key: {key}")
