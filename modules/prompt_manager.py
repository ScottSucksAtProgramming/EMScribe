# modules/prompt_manager.py

from modules.prompts.extraction_prompts import extraction_prompts
from modules.prompts.cleaning_prompts import cleaning_prompts
from modules.prompts.narrative_prompts import narrative_prompts

class PromptManager:
    """
    A class to manage and format prompts for various tasks.

    Attributes:
        prompts (dict): A dictionary of predefined prompts.
    """

    def __init__(self):
        """
        Initializes the PromptManager with a dictionary of prompts.
        """
        self.prompts = {
            **extraction_prompts,
            **cleaning_prompts,
            **narrative_prompts,
            # Add other prompt modules as needed...
        }

    def get_prompt(self, key, **kwargs):
        """
        Returns a formatted prompt based on the key and provided keyword arguments.

        Args:
            key (str): The key for the desired prompt.
            **kwargs: Keyword arguments to format the prompt.

        Returns:
            str or dict: The formatted prompt or dictionary of prompts.
        """
        prompt_template = self.prompts.get(key)
        if prompt_template:
            if isinstance(prompt_template, dict):
                return {k: v.format(**kwargs) for k, v in prompt_template.items()}
            else:
                return prompt_template.format(**kwargs)
        else:
            raise KeyError(f"No prompt found for key: {key}")
