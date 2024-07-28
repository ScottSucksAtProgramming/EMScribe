# modules/narrative_manager.py

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager

class NarrativeManager:
    """
    A class to generate EMS narratives using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the NarrativeManager with a ModelLoader and PromptManager instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def generate_narrative(self, narrative_format: str, data: str) -> str:
        """
        Generates a narrative based on the specified format and data.

        Args:
            narrative_format (str): The key for the desired narrative format.
            data (str): The extracted information in a single string.

        Returns:
            str: The generated narrative.
        """
        narrative_steps = self.prompt_manager.get_prompt(narrative_format, data=data)

        narrative = []
        for step_key, step_prompt in narrative_steps.items():
            response = self.model_loader.generate(step_prompt)
            narrative.append(response)

        return "\n\n".join(narrative).strip()