from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager


class TranscriptCleaner:
    """
    A class to clean up an EMS transcript using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the TranscriptCleaner with a ModelLoader instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def clean(self, transcript: str) -> str:
        """
        Cleans the transcript using the specified prompt.

        Args:
            transcript (str): The transcript to clean.

        Returns:
            str: The cleaned transcript.
        """
        prompt = self.prompt_manager.get_prompt(
            "clean_transcript", transcript=transcript
        )

        # Calculate the optimal context window size based on the length of the prompt
        optimal_context_window = self.model_loader.calculate_optimal_context_window(len(prompt))

        # Update the context window of the model loader
        self.model_loader.context_window = optimal_context_window

        if isinstance(prompt, list):
            # If prompt is a list of chunks
            cleaned_parts = []
            for sub_prompt in prompt:
                response = self.model_loader.generate(sub_prompt)
                cleaned_parts.append(response)
            cleaned_transcript = " ".join(cleaned_parts)
        else:
            response = self.model_loader.generate(prompt)
            cleaned_transcript = response

        return cleaned_transcript.strip()