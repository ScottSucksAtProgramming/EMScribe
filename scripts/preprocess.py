import re
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.prompt_manager import PromptManager


class TranscriptPreprocessor:
    """
    A class to preprocess EMS transcripts using an AI model and additional text processing.

    Attributes:
        cleaner (TranscriptCleaner): An instance of TranscriptCleaner to clean transcripts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the TranscriptPreprocessor with a ModelLoader and PromptManager instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.cleaner = TranscriptCleaner(model_loader, prompt_manager)

    def preprocess(self, transcript: str) -> str:
        """
        Preprocesses the transcript by cleaning it and applying further text processing.

        Args:
            transcript (str): The transcript to preprocess.

        Returns:
            str: The preprocessed transcript.
        """
        cleaned_transcript = self.cleaner.clean(transcript)
        cleaned_transcript = re.sub(r"\s+", " ", cleaned_transcript).strip()
        return cleaned_transcript


# Example usage
if __name__ == "__main__":
    model_loader_instance = ModelLoader(
        base_url="http://localhost:11434", model_name="llama3.1"
    )
    preprocessor = TranscriptPreprocessor(model_loader_instance, PromptManager())

    example_transcript = (
        "The patient is experiencing experiencing shortness of breath. "
        "The patient is The patient is also complaining of chest pain."
    )
    print(preprocessor.preprocess(example_transcript))
