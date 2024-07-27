from model_loader import ModelLoader
from cleaner import TranscriptCleaner

def preprocess_transcript(transcript):
    cleaner = TranscriptCleaner(model_loader=ModelLoader(base_url="http://localhost:11434", model_name="llama3.1"))
    cleaned_transcript = cleaner.clean(transcript)
    return cleaned_transcript

# Example usage
if __name__ == "__main__":
    example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    print(preprocess_transcript(example_transcript))