# scripts/main.py

import pyperclip
import os
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

def example_generate_narrative(transcript):
    # Step 1: Extract information from the transcript
    extracted_data = extractor.extract(transcript)
    
    # Step 2: Use the extracted data to generate the narrative
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    
    print("Generated Narrative:")
    print(narrative)
    pyperclip.copy(narrative)
    print("\nThe generated narrative has been copied to your clipboard.")

def example_clean_transcript(transcript):
    cleaned_transcript = cleaner.clean(transcript)
    print("Cleaned Transcript:")
    print(cleaned_transcript)
    pyperclip.copy(cleaned_transcript)
    print("\nThe cleaned transcript has been copied to your clipboard.")

def example_extract_information(transcript):
    extracted_data = extractor.extract(transcript)
    print("Extracted Information:")
    print(extracted_data)
    pyperclip.copy(extracted_data)
    print("\nThe extracted information has been copied to your clipboard.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="EMScribe 2.0 CLI")
    parser.add_argument("action", choices=["clean", "extract", "narrative"], help="Action to perform")
    parser.add_argument("file", help="Path to the transcript file")

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' not found.")
        exit(1)

    with open(args.file, "r") as f:
        transcript = f.read()

    if args.action == "clean":
        example_clean_transcript(transcript)
    elif args.action == "extract":
        example_extract_information(transcript)
    elif args.action == "narrative":
        example_generate_narrative(transcript)
