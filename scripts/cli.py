import argparse
import sys
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

def review_extracted_data(extracted_data_path, output_path=None):
    with open(extracted_data_path, 'r') as file:
        extracted_data = file.read()

    sections = extracted_data.split('\n\n')
    reviewed_sections = []

    for section in sections:
        print("\n" + "="*50)
        print(f"Current Section:\n\n{section}")
        print("="*50)
        while True:
            user_input = input("\nEnter changes or type 'skip' or 's' to move to the next section: ").strip().lower()
            if user_input == 'skip' or user_input == 's':
                reviewed_sections.append(section)
                break
            else:
                response = reviewer.review_section(section, user_input)
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

    if output_path:
        with open(output_path, 'w') as file:
            file.write(reviewed_data)
        print(f"\nReviewed data saved to {output_path}")
    else:
        default_output_path = "data/reviewed_extract.txt"
        with open(default_output_path, 'w') as file:
            file.write(reviewed_data)
        print(f"\nReviewed data saved to {default_output_path}")

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
        "review", help="Review and modify extracted data"
    )
    review_parser.add_argument("extracted_data_path", help="Path to the extracted data file")
    review_parser.add_argument(
        "--output", help="Path to save the reviewed extracted data", default="data/reviewed_extract.txt"
    )

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