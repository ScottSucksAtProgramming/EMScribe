# scripts/cli.py

import argparse
import pyperclip
import os
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager

def clean_transcript(transcript_path, output_path=None):
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    cleaner = TranscriptCleaner(model_loader, prompt_manager)
    
    with open(transcript_path, 'r') as file:
        transcript = file.read()

    cleaned_transcript = cleaner.clean(transcript)
    pyperclip.copy(cleaned_transcript)
    
    print("Cleaned Transcript:")
    print(cleaned_transcript)
    
    if output_path:
        with open(output_path, 'w') as file:
            file.write(cleaned_transcript)

def extract_information(transcript_path, output_path=None):
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    extractor = TranscriptExtractor(model_loader, prompt_manager)
    
    with open(transcript_path, 'r') as file:
        transcript = file.read()

    extracted_data = extractor.extract(transcript)
    pyperclip.copy(extracted_data)
    
    print("Extracted Information:")
    print(extracted_data)
    
    if output_path:
        with open(output_path, 'w') as file:
            file.write(extracted_data)

def generate_narrative(extracted_data_path, output_path=None):
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    narrative_manager = NarrativeManager(model_loader, prompt_manager)
    
    with open(extracted_data_path, 'r') as file:
        extracted_data = file.read()

    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    pyperclip.copy(narrative)
    
    print("Generated Narrative:")
    print(narrative)
    
    if output_path:
        with open(output_path, 'w') as file:
            file.write(narrative)

def main():
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    parser.add_argument("command", choices=["clean", "extract", "generate"], help="Command to run")
    parser.add_argument("transcript_path", help="Path to the transcript file")
    parser.add_argument("--output", help="Path to save the output")

    args = parser.parse_args()
    command = args.command
    transcript_path = args.transcript_path
    output_path = args.output

    if command == "clean":
        clean_transcript(transcript_path, output_path)
    elif command == "extract":
        extract_information(transcript_path, output_path)
    elif command == "generate":
        generate_narrative(transcript_path, output_path)

if __name__ == "__main__":
    main()
