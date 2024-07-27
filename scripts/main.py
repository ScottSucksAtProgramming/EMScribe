from modules.prompt_manager import PromptManager
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor

# Initialize PromptManager
prompt_manager = PromptManager()

# Initialize ModelLoader with the base URL for the AI model server
model_loader = ModelLoader(base_url="http://localhost:11434")

# Initialize TranscriptCleaner with the ModelLoader and PromptManager
cleaner = TranscriptCleaner(model_loader, prompt_manager)

# Initialize TranscriptExtractor with the ModelLoader and PromptManager
extractor = TranscriptExtractor(model_loader, prompt_manager)

# Example usage for cleaning a transcript
def example_clean_transcript():
    example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    cleaned_transcript = cleaner.clean(example_transcript)
    print("Cleaned Transcript:")
    print(cleaned_transcript)

# Example usage for extracting information from a transcript
def example_extract_information():
    example_transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
    extracted_data = extractor.extract(example_transcript)
    print("Extracted Information:")
    for key, value in extracted_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Example usage
    example_clean_transcript()
    example_extract_information()