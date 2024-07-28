# scripts/main.py

import argparse
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

# Function to read transcript from a file
def read_transcript_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to clean a transcript and display the output
def clean_transcript_and_display_output(file_path):
    example_transcript = read_transcript_from_file(file_path)
    cleaned_transcript = cleaner.clean(example_transcript)
    print("Cleaned Transcript:")
    print(cleaned_transcript)

# Function to extract information from a transcript and display the output
def extract_information_and_display_output(file_path):
    example_transcript = read_transcript_from_file(file_path)
    extracted_data = extractor.extract(example_transcript)
    print("Extracted Information:")
    print(extracted_data)

# Function to generate a narrative and display the output
def generate_narrative_and_display_output(file_path):
    example_transcript = read_transcript_from_file(file_path)
    cleaned_transcript = cleaner.clean(example_transcript)
    extracted_data = extractor.extract(cleaned_transcript)
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    print("Generated Narrative:")
    print(narrative)

def main():
    parser = argparse.ArgumentParser(description="EMScribe 2.0 CLI")
    parser.add_argument("action", choices=["clean", "extract", "generate"], help="Action to perform")
    parser.add_argument("file_path", help="Path to the transcript text file")

    args = parser.parse_args()

    if args.action == "clean":
        clean_transcript_and_display_output(args.file_path)
    elif args.action == "extract":
        extract_information_and_display_output(args.file_path)
    elif args.action == "generate":
        generate_narrative_and_display_output(args.file_path)

if __name__ == "__main__":
    main()
