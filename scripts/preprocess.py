import re
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.prompt_manager import PromptManager

# Initialize PromptManager
prompt_manager = PromptManager()


# Function to preprocess the transcript
def preprocess_transcript(transcript):
    # Initialize ModelLoader
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

    # Initialize TranscriptCleaner with ModelLoader and PromptManager
    cleaner = TranscriptCleaner(
        model_loader=model_loader, prompt_manager=prompt_manager
    )

    # Clean the transcript
    cleaned_transcript = cleaner.clean(transcript)

    # Further basic preprocessing steps (if any)
    cleaned_transcript = re.sub(r"\s+", " ", cleaned_transcript).strip()

    return cleaned_transcript


# Example usage
if __name__ == "__main__":
    example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    print(preprocess_transcript(example_transcript))
