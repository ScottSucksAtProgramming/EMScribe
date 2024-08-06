from typing import Dict, List

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

    def generate_narrative(self, narrative_format: str, data: Dict) -> str:
        """
        Generates a narrative based on the specified format and data.

        Args:
            narrative_format (str): The key for the desired narrative format.
            data (Dict): The extracted information in a dictionary.

        Returns:
            str: The generated narrative.
        """
        try:
            narrative_steps = self.prompt_manager.get_prompt(
                narrative_format, data=data
            )

            narrative = []
            for step_prompt in narrative_steps.values():
                step_response = self._generate_response(step_prompt)
                narrative.append(step_response)

            return "\n\n".join(narrative).strip()
        except KeyError:
            # Allow KeyError to propagate
            raise
        except Exception as e:
            # Log the exception and handle it appropriately
            raise RuntimeError(f"Error generating narrative: {e}")

    def _generate_response(self, prompt: str) -> str:
        """
        Generates a response from the AI model based on the provided prompt.

        Args:
            prompt (str): The input prompt for the model.

        Returns:
            str: The AI model's response.
        """
        try:
            context_window_size = self.model_loader.context_window

            if len(prompt) > context_window_size:
                response_parts = [
                    self.model_loader.generate(prompt[i : i + context_window_size])
                    for i in range(0, len(prompt), context_window_size)
                ]
                return " ".join(response_parts)

            return self.model_loader.generate(prompt)
        except Exception as e:
            # Log the exception and handle it appropriately
            raise RuntimeError(f"Error generating response: {e}")
