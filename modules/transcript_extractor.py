from typing import List, Union

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager


class TranscriptExtractor:
    """
    A class to extract information from an EMS transcript using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the TranscriptExtractor with a ModelLoader and PromptManager instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def extract(self, transcript: str) -> str:
        """
        Extracts information from the transcript using specified prompts.

        Args:
            transcript (str): The transcript to extract information from.

        Returns:
            str: The extracted information in a single string.
        """
        prompt_keys = [
            "incident_info",
            "patient_demographics",
            "subjective_info",
            "history_of_present_illness",
            "patient_histories",
            "objective_1",
            "objective_2",
            "vitals",
            "poc_tests",
            "labs",
            "imaging",
            "impressions",
            "treatments",
            "packaging",
            "transport",
            "transfer_of_care",
        ]
        extracted_data = [
            self._extract_from_prompt(key, transcript) for key in prompt_keys
        ]

        combined_response = "\n\n".join(extracted_data).strip()
        return combined_response

    def _extract_from_prompt(self, prompt_key: str, transcript: str) -> str:
        """
        Extracts information from the transcript using a single prompt.

        Args:
            prompt_key (str): The key for the desired prompt.
            transcript (str): The transcript to extract information from.

        Returns:
            str: The extracted information.
        """
        try:
            prompt = self.prompt_manager.get_prompt(prompt_key, transcript=transcript)

            if isinstance(prompt, list):
                responses = [
                    self.model_loader.generate(sub_prompt) for sub_prompt in prompt
                ]
                return " ".join(responses).strip()

            return self.model_loader.generate(prompt).strip()
        except KeyError as e:
            raise KeyError(f"No prompt found for key: {prompt_key}") from e
        except Exception as e:
            raise RuntimeError(f"Error extracting information: {e}") from e
