# scripts/main.py

from modules.prompt_manager import PromptManager
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager

# Initialize PromptManager
prompt_manager = PromptManager()

# Initialize ModelLoader with the base URL for the AI model server and model name
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize TranscriptCleaner with the ModelLoader and PromptManager
cleaner = TranscriptCleaner(model_loader, prompt_manager)

# Initialize TranscriptExtractor with the ModelLoader and PromptManager
extractor = TranscriptExtractor(model_loader, prompt_manager)

# Initialize NarrativeManager with the ModelLoader and PromptManager
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

# Example usage for generating a narrative
def example_generate_narrative():
    example_transcript = "Unit 5-41-16 responding emergent to Dermatology office in Levittown. Dispatch reports a male patient with an unknown complaint. Unit has a full crew and experiences no delays. Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."

    # Step 1: Extract information from the transcript
    extracted_data = extractor.extract(example_transcript)
    
    # Step 2: Use the extracted data to generate the narrative
    narrative = narrative_manager.generate_narrative("presoaped_format", extracted_data)
    
    print("Generated Narrative:")
    print(narrative)

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
    example_generate_narrative()