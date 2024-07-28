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

def main():
    print("Welcome to EMScribe 2.0")
    user_transcript = input("Please enter the EMS transcript: ")

    # Step 1: Clean the transcript
    cleaned_transcript = cleaner.clean(user_transcript)
    print("Cleaned Transcript:")
    print(cleaned_transcript)

    # Step 2: Extract information from the cleaned transcript
    extracted_data = extractor.extract(cleaned_transcript)
    print("Extracted Information:")
    print(extracted_data)

    # Step 3: Generate the narrative based on extracted data
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    print("Generated Narrative:")
    print(narrative)

if __name__ == "__main__":
    main()
