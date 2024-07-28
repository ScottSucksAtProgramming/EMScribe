from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager

class NarrativeManager:
    """
    A class to manage and generate narratives using multiple prompts.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def generate_narrative(self, narrative_format: str, data: dict) -> str:
        """
        Generates a narrative using the specified format and data.

        Args:
            narrative_format (str): The format to use for the narrative.
            data (dict): The data to include in the narrative.

        Returns:
            str: The generated narrative.
        """
        narrative_steps = self.prompt_manager.get_prompt(narrative_format)
        narrative = []

        for step_name, step_prompt in narrative_steps.items():
            prompt = step_prompt.format(**data)
            response = self.model_loader.generate(prompt)
            narrative.append(response)

        return "\n\n".join(narrative)
