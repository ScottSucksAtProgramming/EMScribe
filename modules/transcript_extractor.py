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
        extracted_data = []

        context_window_size = 32000  # Adjusting to use the new context window size

        for key in prompt_keys:
            prompt = self.prompt_manager.get_prompt(key, transcript=transcript)
            if len(prompt) > context_window_size:
                # Split the prompt if it exceeds the context window size
                for i in range(0, len(prompt), context_window_size):
                    sub_prompt = prompt[i : i + context_window_size]
                    response = self.model_loader.generate(sub_prompt)
                    extracted_data.append(response)
            else:
                response = self.model_loader.generate(prompt)
                extracted_data.append(response)

        combined_response = "\n\n".join(extracted_data).strip()
        return combined_response
