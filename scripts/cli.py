# scripts/cli.py

import argparse
import pyperclip
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager
from modules.prompt_manager import PromptManager

def parse_arguments():
    parser = argparse.ArgumentParser(description="EMScribe 2.0 CLI")
    parser.add_argument("function", choices=["clean", "extract", "generate"], help="Function to perform")
    parser.add_argument("transcript_path", help="Path to the transcript text file")
    parser.add_argument("--output", help="Path to save the output to a file")
    return parser.parse_args()

def read_transcript(file_path):
    with open(file_path, "r") as file:
        return file.read()

def save_output_to_file(output, file_path):
    with open(file_path, "w") as file:
        file.write(output)

def clean_transcript(transcript):
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    cleaner = TranscriptCleaner(model_loader, prompt_manager)
    cleaned_transcript = cleaner.clean(transcript)
    return cleaned_transcript

def extract_information(transcript):
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    extractor = TranscriptExtractor(model_loader, prompt_manager)
    extracted_data = extractor.extract(transcript)
    return extracted_data

def generate_narrative(transcript):
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    extractor = TranscriptExtractor(model_loader, prompt_manager)
    narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)
    extracted_data = extractor.extract(transcript)
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    return narrative

def main():
    args = parse_arguments()
    transcript = read_transcript(args.transcript_path)

    if args.function == "clean":
        output = clean_transcript(transcript)
    elif args.function == "extract":
        output = extract_information(transcript)
    elif args.function == "generate":
        output = generate_narrative(transcript)
    
    print(output)
    pyperclip.copy(output)
    
    if args.output:
        save_output_to_file(output, args.output)

if __name__ == "__main__":
    main()
