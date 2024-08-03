# -*- coding: utf-8 -*-
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

    def generate_narrative(self, narrative_format: str, data: dict) -> str:
        """
        Generates a narrative based on the specified format and data.

        Args:
            narrative_format (str): The key for the desired narrative format.
            data (dict): The extracted information in a dictionary.

        Returns:
            str: The generated narrative.
        """
        narrative_steps = self.prompt_manager.get_prompt(narrative_format, data=data)

        narrative = []
        for step_prompt in narrative_steps.values():
            if len(step_prompt) > self.model_loader.context_window:
                # Split the prompt if it exceeds the context window size
                narrative_parts = []
                for i in range(0, len(step_prompt), self.model_loader.context_window):
                    sub_prompt = step_prompt[i : i + self.model_loader.context_window]
                    response = self.model_loader.generate(sub_prompt)
                    narrative_parts.append(response)
                step_response = " ".join(narrative_parts)
            else:
                step_response = self.model_loader.generate(step_prompt)

            narrative.append(step_response)

        return "\n\n".join(narrative).strip()
