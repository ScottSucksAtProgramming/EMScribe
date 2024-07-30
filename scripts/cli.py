import argparse
import sys
from modules.prompt_manager import PromptManager
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager
from modules.quality_controller import QualityController

# Initialize PromptManager and ModelLoader
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize other modules
cleaner = TranscriptCleaner(model_loader, prompt_manager)
extractor = TranscriptExtractor(model_loader, prompt_manager)
narrative_manager = NarrativeManager(model_loader, prompt_manager)
quality_controller = QualityController(model_loader, prompt_manager)

def clean_transcript(transcript_path, output_path):
    if transcript_path == "-":
        transcript = sys.stdin.read()
    else:
        with open(transcript_path, 'r') as file:
            transcript = file.read()

    cleaned_transcript = cleaner.clean(transcript)

    if output_path:
        with open(output_path, 'w') as file:
            file.write(cleaned_transcript)
    else:
        print(cleaned_transcript)
        import pyperclip
        pyperclip.copy(cleaned_transcript)

def extract_information(transcript_path, output_path):
    if transcript_path == "-":
        transcript = sys.stdin.read()
    else:
        with open(transcript_path, 'r') as file:
            transcript = file.read()

    extracted_data = extractor.extract(transcript)

    if output_path:
        with open(output_path, 'w') as file:
            file.write(extracted_data)
    else:
        print(extracted_data)
        import pyperclip
        pyperclip.copy(extracted_data)

def generate_narrative(extracted_data_path, output_path):
    if extracted_data_path == "-":
        extracted_data = sys.stdin.read()
    else:
        with open(extracted_data_path, 'r') as file:
            extracted_data = file.read()

    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)

    if output_path:
        with open(output_path, 'w') as file:
            file.write(narrative)
    else:
        print(narrative)
        import pyperclip
        pyperclip.copy(narrative)

def quality_control(transcript_path, narrative_path, output_path):
    with open(transcript_path, 'r') as file:
        transcript = file.read()

    with open(narrative_path, 'r') as file:
        narrative = file.read()

    improved_narrative = quality_controller.review_narrative(transcript, narrative)
    checked_narrative = quality_controller.check_required_info(improved_narrative, format="presoaped_format")

    if output_path:
        with open(output_path, 'w') as file:
            file.write(checked_narrative)
    else:
        print(checked_narrative)
        import pyperclip
        pyperclip.copy(checked_narrative)

def main():
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    clean_parser = subparsers.add_parser("clean", help="Clean the transcript")
    clean_parser.add_argument("transcript_path", help="Path to the transcript file")
    clean_parser.add_argument("--output", help="Path to save the cleaned transcript")

    extract_parser = subparsers.add_parser("extract", help="Extract information from the transcript")
    extract_parser.add_argument("transcript_path", help="Path to the transcript file")
    extract_parser.add_argument("--output", help="Path to save the extracted information")

    generate_parser = subparsers.add_parser("generate", help="Generate a narrative from the extracted information")
    generate_parser.add_argument("transcript_path", help="Path to the extracted data file")
    generate_parser.add_argument("--output", help="Path to save the generated narrative")

    quality_parser = subparsers.add_parser("quality", help="Perform quality control on the narrative")
    quality_parser.add_argument("transcript_path", help="Path to the transcript file")
    quality_parser.add_argument("--narrative_path", help="Path to the narrative file", required=True)
    quality_parser.add_argument("--output", help="Path to save the improved narrative")

    args = parser.parse_args()

    if args.command == "clean":
        clean_transcript(args.transcript_path, args.output)
    elif args.command == "extract":
        extract_information(args.transcript_path, args.output)
    elif args.command == "generate":
        generate_narrative(args.transcript_path, args.output)
    elif args.command == "quality":
        quality_control(args.transcript_path, args.narrative_path, args.output)

if __name__ == "__main__":
    main()
