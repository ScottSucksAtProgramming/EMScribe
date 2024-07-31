import argparse
import sys
import os
import subprocess
from modules.prompt_manager import PromptManager
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager
from modules.reviewer import Reviewer

# Initialize PromptManager and ModelLoader
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize other modules
cleaner = TranscriptCleaner(model_loader, prompt_manager)
extractor = TranscriptExtractor(model_loader, prompt_manager)
narrative_manager = NarrativeManager(model_loader, prompt_manager)
reviewer = Reviewer(model_loader, prompt_manager)

def clear_screen():
    if os.name == 'nt':  # For Windows
        _ = subprocess.call('cls', shell=True)
    else:  # For macOS and Linux
        _ = subprocess.call('clear', shell=True)

def review_extracted_data(extracted_data_path=None, output_path=None):
    if not extracted_data_path:
        extracted_data_path = "data/extract.txt"

    with open(extracted_data_path, 'r') as file:
        extracted_data = file.read()

    sections = extracted_data.split('\n\n')
    reviewed_sections = []

    for section in sections:
        clear_screen()
        print("\n" + "="*50)
        print(f"Current Section:\n{section}")
        print("="*50)
        while True:
            user_input = input("\nEnter changes or type 'skip' or 's' to move to the next section: ").strip().lower()
            if user_input == 'skip' or user_input == 's':
                reviewed_sections.append(section)
                break
            else:
                response = reviewer.review_section(section, user_input)
                clear_screen()
                print("\n" + "-"*50)
                print(f"AI Response:\n{response}")
                print("-"*50)
                final_user_input = input("\nIs this correct? (yes/no): ").strip().lower()
                if final_user_input == 'yes':
                    reviewed_sections.append(response)
                    break
                else:
                    section = response

    reviewed_data = '\n\n'.join(reviewed_sections)

    if not output_path:
        output_path = "data/reviewed_extract.txt"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as file:
        file.write(reviewed_data)
    print(f"\nReviewed data saved to {output_path}")

def clean_transcript(transcript_path, output_path=None):
    if transcript_path == "-":
        transcript = sys.stdin.read()
    else:
        with open(transcript_path, "r") as file:
            transcript = file.read()

    cleaned_transcript = cleaner.clean(transcript)

    if not output_path:
        output_path = "data/cleaned_transcript.txt"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as file:
        file.write(cleaned_transcript)
    print(f"Cleaned transcript saved to {output_path}")


def extract_information(transcript_path=None, output_path=None):
    if not transcript_path:
        transcript_path = "data/cleaned_transcript.txt"

    with open(transcript_path, "r") as file:
        transcript = file.read()

    extracted_data = extractor.extract(transcript)

    if not output_path:
        output_path = "data/extract.txt"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as file:
        file.write(extracted_data)
    print(f"Extracted information saved to {output_path}")


def generate_narrative(extracted_data_path=None, output_path=None):
    if not extracted_data_path:
        extracted_data_path = "data/reviewed_extract.txt"

    with open(extracted_data_path, "r") as file:
        extracted_data = file.read()

    narrative = narrative_manager.generate_narrative(
        "presoaped_format", data=extracted_data
    )

    if not output_path:
        output_path = "data/narrative.txt"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as file:
        file.write(narrative)
    print(f"Narrative saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    clean_parser = subparsers.add_parser("clean", help="Clean the transcript")
    clean_parser.add_argument("transcript_path", help="Path to the transcript file")
    clean_parser.add_argument("--output", help="Path to save the cleaned transcript")

    extract_parser = subparsers.add_parser(
        "extract", help="Extract information from the transcript"
    )
    extract_parser.add_argument("transcript_path", nargs='?', help="Path to the transcript file")
    extract_parser.add_argument(
        "--output", help="Path to save the extracted information"
    )

    generate_parser = subparsers.add_parser(
        "generate", help="Generate a narrative from the extracted information"
    )
    generate_parser.add_argument(
        "extracted_data_path", nargs='?', help="Path to the extracted data file"
    )
    generate_parser.add_argument(
        "--output", help="Path to save the generated narrative"
    )

    review_parser = subparsers.add_parser(
        "review", help="Review and modify extracted data"
    )
    review_parser.add_argument("extracted_data_path", nargs='?', help="Path to the extracted data file")
    review_parser.add_argument(
        "--output", help="Path to save the reviewed extracted data"
    )

    args = parser.parse_args()

    if args.command == "clean":
        clean_transcript(args.transcript_path, args.output)
    elif args.command == "extract":
        extract_information(args.transcript_path, args.output)
    elif args.command == "generate":
        generate_narrative(args.extracted_data_path, args.output)
    elif args.command == "review":
        review_extracted_data(args.extracted_data_path, args.output)


if __name__ == "__main__":
    main()