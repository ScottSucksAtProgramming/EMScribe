import argparse
import pyperclip
import sys
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager
from modules.quality_controller import QualityController
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager

# Initialize the necessary components
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
cleaner = TranscriptCleaner(model_loader, prompt_manager)
extractor = TranscriptExtractor(model_loader, prompt_manager)
narrative_manager = NarrativeManager(model_loader, prompt_manager)
quality_controller = QualityController(model_loader, prompt_manager)

def clean_transcript(transcript_path, output_path=None):
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
    if extracted_data_path == '-':
        extracted_data = sys.stdin.read()
    else:
        with open(extracted_data_path, 'r') as file:
            extracted_data = file.read()
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    pyperclip.copy(narrative)
    print("Generated Narrative:")
    print(narrative)
    if output_path:
        with open(output_path, 'w') as file:
            file.write(narrative)

def quality_control(transcript_path, narrative_path, output_path=None):
    with open(transcript_path, 'r') as file:
        transcript = file.read()
    with open(narrative_path, 'r') as file:
        narrative = file.read()
    improved_narrative = quality_controller.review_narrative(transcript, narrative)
    checked_narrative = quality_controller.check_required_info(improved_narrative, format="presoaped_format")
    pyperclip.copy(checked_narrative)
    print("Quality Controlled Narrative:")
    print(checked_narrative)
    if output_path:
        with open(output_path, 'w') as file:
            file.write(checked_narrative)

def main():
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    subparsers = parser.add_subparsers(dest='command')

    parser_clean = subparsers.add_parser('clean', help='Clean a transcript')
    parser_clean.add_argument('transcript_path', type=str, help='Path to the transcript file')
    parser_clean.add_argument('--output', type=str, help='Path to save the output')

    parser_extract = subparsers.add_parser('extract', help='Extract information from a transcript')
    parser_extract.add_argument('transcript_path', type=str, help='Path to the transcript file')
    parser_extract.add_argument('--output', type=str, help='Path to save the output')

    parser_generate = subparsers.add_parser('generate', help='Generate a narrative from extracted data')
    parser_generate.add_argument('transcript_path', type=str, help='Path to the extracted data file or - for stdin')
    parser_generate.add_argument('--output', type=str, help='Path to save the output')

    parser_quality = subparsers.add_parser('quality', help='Perform quality control on a narrative')
    parser_quality.add_argument('transcript_path', type=str, help='Path to the transcript file')
    parser_quality.add_argument('--narrative_path', type=str, required=True, help='Path to the narrative file')
    parser_quality.add_argument('--output', type=str, help='Path to save the output')

    args = parser.parse_args()

    if args.command == 'clean':
        clean_transcript(args.transcript_path, args.output)
    elif args.command == 'extract':
        extract_information(args.transcript_path, args.output)
    elif args.command == 'generate':
        generate_narrative(args.transcript_path, args.output)
    elif args.command == 'quality':
        quality_control(args.transcript_path, args.narrative_path, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
