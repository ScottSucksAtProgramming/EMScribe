import argparse
import sys
from modules.prompt_manager import PromptManager
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager
from modules.reviewer import Reviewer
import os

# Initialize PromptManager and ModelLoader
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize other modules
cleaner = TranscriptCleaner(model_loader, prompt_manager)
extractor = TranscriptExtractor(model_loader, prompt_manager)
narrative_manager = NarrativeManager(model_loader, prompt_manager)
reviewer = Reviewer(model_loader, prompt_manager)

def review_extracted_data(extracted_data_path, output_path):
    with open(extracted_data_path, 'r') as file:
        extracted_data = file.read()

    sections = extracted_data.split('\n\n')
    reviewed_sections = []

    for section in sections:
        while True:
            response = reviewer.review_section(section)
            print(f"Current Section: {section}")
            print(f"AI Response: {response}")
            user_input = input("Enter changes or type 'skip' to move to the next section: ").strip()
            if user_input.lower() == 'skip':
                reviewed_sections.append(section)
                break
            else:
                final_response = reviewer.final_review(updated_section=user_input)
                print(f"Final AI Response: {final_response}")
                user_input = input("Is this correct? (yes/no): ").strip()
                if user_input.lower() == 'yes':
                    reviewed_sections.append(final_response)
                    break

    reviewed_data = '\n\n'.join(reviewed_sections)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as file:
        file.write(reviewed_data)
    print(f"Reviewed data saved to {output_path}")

def clean_transcript(transcript_path, output_path):
    if transcript_path == "-":
        transcript = sys.stdin.read()
    else:
        with open(transcript_path, "r") as file:
            transcript = file.read()

    cleaned_transcript = cleaner.clean(transcript)

    if output_path:
        with open(output_path, "w") as file:
            file.write(cleaned_transcript)
    else:
        print(cleaned_transcript)
        import pyperclip

        pyperclip.copy(cleaned_transcript)

def extract_information(transcript_path, output_path):
    if transcript_path == "-":
        transcript = sys.stdin.read()
    else:
        with open(transcript_path, "r") as file:
            transcript = file.read()

    extracted_data = extractor.extract(transcript)

    if output_path:
        with open(output_path, "w") as file:
            file.write(extracted_data)
    else:
        print(extracted_data)
        import pyperclip

        pyperclip.copy(extracted_data)

def generate_narrative(extracted_data_path, output_path):
    if extracted_data_path == "-":
        extracted_data = sys.stdin.read()
    else:
        with open(extracted_data_path, "r") as file:
            extracted_data = file.read()

    narrative = narrative_manager.generate_narrative(
        "presoaped_format", data=extracted_data
    )

    if output_path:
        with open(output_path, "w") as file:
            file.write(narrative)
    else:
        print(narrative)
        import pyperclip

        pyperclip.copy(narrative)

def main():
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    clean_parser = subparsers.add_parser("clean", help="Clean the transcript")
    clean_parser.add_argument("transcript_path", help="Path to the transcript file")
    clean_parser.add_argument("--output", help="Path to save the cleaned transcript")

    extract_parser = subparsers.add_parser(
        "extract", help="Extract information from the transcript"
    )
    extract_parser.add_argument("transcript_path", help="Path to the transcript file")
    extract_parser.add_argument(
        "--output", help="Path to save the extracted information"
    )

    generate_parser = subparsers.add_parser(
        "generate", help="Generate a narrative from the extracted information"
    )
    generate_parser.add_argument(
        "transcript_path", help="Path to the extracted data file"
    )
    generate_parser.add_argument(
        "--output", help="Path to save the generated narrative"
    )

    review_parser = subparsers.add_parser(
        "review", help="Review extracted data section by section"
    )
    review_parser.add_argument("extracted_data_path", help="Path to the extracted data file")
    review_parser.add_argument("--output", help="Path to save the reviewed data", default="data/reviewed_extract.txt")

    args = parser.parse_args()

    if args.command == "clean":
        clean_transcript(args.transcript_path, args.output)
    elif args.command == "extract":
        extract_information(args.transcript_path, args.output)
    elif args.command == "generate":
        generate_narrative(args.transcript_path, args.output)
    elif args.command == "review":
        review_extracted_data(args.extracted_data_path, args.output)

if __name__ == "__main__":
    main()