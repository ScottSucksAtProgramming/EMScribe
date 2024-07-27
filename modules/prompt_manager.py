# modules/prompt_manager.py

class PromptManager:
    """
    A class to manage and format prompts for various tasks.

    Attributes:
        prompts (dict): A dictionary of predefined prompts.
    """

    def __init__(self, prompts):
        """
        Initializes the PromptManager with a dictionary of prompts.

        Args:
            prompts (dict): A dictionary where keys are prompt names and values are prompt templates.
        """
        self.prompts = prompts

    def get_prompt(self, key, **kwargs):
        """
        Returns a formatted prompt based on the key and provided keyword arguments.

        Args:
            key (str): The key for the desired prompt.
            **kwargs: Keyword arguments to format the prompt.

        Returns:
            str: The formatted prompt.
        """
        prompt_template = self.prompts.get(key)
        if prompt_template:
            return prompt_template.format(**kwargs)
        else:
            raise KeyError(f"No prompt found for key: {key}")