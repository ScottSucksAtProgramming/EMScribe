from typing import Union

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager


class TranscriptCleaner:
    """
    A class to clean EMS transcripts using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the TranscriptCleaner with a ModelLoader and PromptManager instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def clean(self, transcript: str) -> str:
        """
        Cleans the transcript using specified prompts.

        Args:
            transcript (str): The transcript to clean.

        Returns:
            str: The cleaned transcript.
        """
        prompt_key = "clean_transcript"
        try:
            prompt = self.prompt_manager.get_prompt(prompt_key, transcript=transcript)
            return self._generate_cleaned_transcript(prompt)
        except KeyError as e:
            # Allow KeyError to propagate
            raise e
        except Exception as e:
            # Log the exception and handle it appropriately
            raise RuntimeError(f"Error cleaning transcript: {e}")

    def _generate_cleaned_transcript(self, prompt: Union[str, list[str]]) -> str:
        """
        Generates the cleaned transcript based on the provided prompt.

        Args:
            prompt (Union[str, list[str]]): The input prompt for the model.

        Returns:
            str: The cleaned transcript.
        """
        try:
            if isinstance(prompt, list):
                cleaned_parts = [
                    self.model_loader.generate(sub_prompt) for sub_prompt in prompt
                ]
                return " ".join(cleaned_parts).strip()

            return self.model_loader.generate(prompt).strip()
        except Exception as e:
            # Log the exception and handle it appropriately
            raise RuntimeError(f"Error generating cleaned transcript: {e}")
