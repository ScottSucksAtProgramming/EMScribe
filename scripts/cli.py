import argparse
import os
import pyperclip
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager
from modules.prompt_manager import PromptManager 

def load_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def save_output(output, output_path=None):
    pyperclip.copy(output)
    if output_path:
        with open(output_path, 'w') as file:
            file.write(output)

def clean_transcript(transcript):
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    prompt_manager = PromptManager()
    cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)
    cleaned_transcript = cleaner.clean(transcript)
    return "Cleaned Transcript:\n" + cleaned_transcript

def extract_information(transcript):
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    prompt_manager = PromptManager()
    extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)
    extracted_data = extractor.extract(transcript)
    return "Extracted Information:\n" + extracted_data

def generate_narrative(transcript):
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    prompt_manager = PromptManager()
    extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)
    narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)
    
    extracted_data = extractor.extract(transcript)
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    return "Generated Narrative:\n" + narrative

def main():
    parser = argparse.ArgumentParser(description='EMScribe CLI tool')
    parser.add_argument('command', choices=['clean', 'extract', 'generate'], help='Command to run')
    parser.add_argument('transcript_path', help='Path to the transcript text file')
    parser.add_argument('--output', help='Path to save the output')

    args = parser.parse_args()
    transcript = load_transcript(args.transcript_path)
    
    if args.command == 'clean':
        output = clean_transcript(transcript)
    elif args.command == 'extract':
        output = extract_information(transcript)
    elif args.command == 'generate':
        output = generate_narrative(transcript)

    print(output)
    save_output(output, args.output)

if __name__ == '__main__':
    main()
