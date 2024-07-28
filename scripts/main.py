import sys
import argparse
import pyperclip
from modules.prompt_manager import PromptManager
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager

# Initialize PromptManager and ModelLoader
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize TranscriptCleaner, TranscriptExtractor, and NarrativeManager
cleaner = TranscriptCleaner(model_loader, prompt_manager)
extractor = TranscriptExtractor(model_loader, prompt_manager)
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

def clean_transcript(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    cleaned_transcript = cleaner.clean(transcript)
    pyperclip.copy(cleaned_transcript)
    print("Cleaned Transcript:")
    print(cleaned_transcript)
    print("The cleaned transcript has been copied to your clipboard.")

def extract_information(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    extracted_data = extractor.extract(transcript)
    pyperclip.copy(extracted_data)
    print("Extracted Information:")
    print(extracted_data)
    print("The extracted information has been copied to your clipboard.")

def generate_narrative(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    extracted_data = extractor.extract(transcript)
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    pyperclip.copy(narrative)
    print("Generated Narrative:")
    print(narrative)
    print("The generated narrative has been copied to your clipboard.")

def main():
    parser = argparse.ArgumentParser(description="EMScribe 2.0 CLI Tool")
    parser.add_argument("action", choices=["clean", "extract", "narrative"], help="Action to perform")
    parser.add_argument("file_path", help="Path to the transcript text file")
    args = parser.parse_args()

    if args.action == "clean":
        clean_transcript(args.file_path)
    elif args.action == "extract":
        extract_information(args.file_path)
    elif args.action == "narrative":
        generate_narrative(args.file_path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
