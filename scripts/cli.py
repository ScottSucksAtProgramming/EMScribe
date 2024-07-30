# cli.py

import argparse
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager
from modules.quality_controller import QualityController
import pyperclip

def clean_transcript(transcript_path, output_path):
    with open(transcript_path, 'r') as file:
        transcript = file.read()
    
    cleaned_transcript = cleaner.clean(transcript)
    print("Cleaned Transcript:")
    print(cleaned_transcript)

    pyperclip.copy(cleaned_transcript)
    print("Output has been copied to the clipboard.")
    
    if output_path:
        with open(output_path, 'w') as file:
            file.write(cleaned_transcript)
        print(f"Output saved to {output_path}")

def extract_information(transcript_path, output_path):
    with open(transcript_path, 'r') as file:
        transcript = file.read()

    extracted_data = extractor.extract(transcript)
    print("Extracted Information:")
    print(extracted_data)

    pyperclip.copy(extracted_data)
    print("Output has been copied to the clipboard.")
    
    if output_path:
        with open(output_path, 'w') as file:
            file.write(extracted_data)
        print(f"Output saved to {output_path}")

def generate_narrative(extracted_data_path, output_path):
    with open(extracted_data_path, 'r') as file:
        extracted_data = file.read()
    
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)

    print("Generated Narrative:")
    print(narrative)

    pyperclip.copy(narrative)
    print("Output has been copied to the clipboard.")
    
    if output_path:
        with open(output_path, 'w') as file:
            file.write(narrative)
        print(f"Output saved to {output_path}")

def quality_control(narrative_path, transcript_path, output_path):
    with open(narrative_path, 'r') as narrative_file, open(transcript_path, 'r') as transcript_file:
        narrative = narrative_file.read()
        transcript = transcript_file.read()
    
    improved_narrative = quality_controller.improve_narrative(narrative, transcript)
    narrative_with_requirements = quality_controller.check_requirements(improved_narrative, "presoaped_format")

    print("Improved Narrative:")
    print(narrative_with_requirements)

    pyperclip.copy(narrative_with_requirements)
    print("Output has been copied to the clipboard.")
    
    if output_path:
        with open(output_path, 'w') as file:
            file.write(narrative_with_requirements)
        print(f"Output saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    parser.add_argument("command", choices=["clean", "extract", "generate", "quality"], help="Command to run")
    parser.add_argument("transcript_path", help="Path to the transcript file")
    parser.add_argument("--output", help="Path to save the output")
    parser.add_argument("--narrative_path", help="Path to the narrative file for quality control", default=None)

    args = parser.parse_args()

    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    cleaner = TranscriptCleaner(model_loader, prompt_manager)
    extractor = TranscriptExtractor(model_loader, prompt_manager)
    narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)
    quality_controller = QualityController(model_loader=model_loader, prompt_manager=prompt_manager)

    if args.command == "clean":
        clean_transcript(args.transcript_path, args.output)
    elif args.command == "extract":
        extract_information(args.transcript_path, args.output)
    elif args.command == "generate":
        generate_narrative(args.transcript_path, args.output)
    elif args.command == "quality":
        if not args.narrative_path:
            print("Please provide the narrative path for quality control.")
        else:
            quality_control(args.narrative_path, args.transcript_path, args.output)
