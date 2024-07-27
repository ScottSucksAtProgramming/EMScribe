from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
import re

def preprocess_transcript(transcript):
    """
    Preprocesses the given transcript by cleaning it using the AI model.

    Args:
        transcript (str): The transcript to preprocess.

    Returns:
        str: The cleaned and preprocessed transcript.
    """
    cleaner = TranscriptCleaner(model_loader=ModelLoader(base_url="http://localhost:11434", model_name="llama3.1"))
    cleaned_transcript = cleaner.clean(transcript)
    cleaned_transcript = re.sub(r'\s+', ' ', cleaned_transcript).strip()
    return cleaned_transcript

if __name__ == "__main__":
    example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    print(preprocess_transcript(example_transcript))