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

        for key in prompt_keys:
            prompt = self.prompt_manager.get_prompt(key, transcript=transcript)

            # Calculate the optimal context window size based on the length of the prompt
            optimal_context_window = self.model_loader.calculate_optimal_context_window(len(prompt))

            # Update the context window of the model loader
            self.model_loader.context_window = optimal_context_window

            if isinstance(prompt, list):
                # If prompt is a list of chunks
                for sub_prompt in prompt:
                    response = self.model_loader.generate(sub_prompt)
                    extracted_data.append(response)
            else:
                response = self.model_loader.generate(prompt)
                extracted_data.append(response)

        combined_response = "\n\n".join(extracted_data).strip()
        return combined_response