import argparse

from commands.clean_command import CleanCommand
from commands.extract_command import ExtractCommand
from commands.generate_command import GenerateCommand
from commands.review_command import ReviewCommand
from modules.extract_reviewer import ExtractReviewer
from modules.model_loader import ModelLoader
from modules.narrative_manager import NarrativeManager
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor


def initialize_components(base_url="http://localhost:11434", model_name="llama3.1"):
    """Initialize all the required components."""
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url=base_url, model_name=model_name)

    cleaner = TranscriptCleaner(model_loader, prompt_manager)
    extractor = TranscriptExtractor(model_loader, prompt_manager)
    narrative_manager = NarrativeManager(model_loader, prompt_manager)
    extract_reviewer = ExtractReviewer(model_loader, prompt_manager)

    return cleaner, extractor, narrative_manager, extract_reviewer


def create_parser():
    """Create and return the argument parser."""
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Clean command
    parser_clean = subparsers.add_parser("clean", help="Clean the transcript")
    parser_clean.add_argument("transcript_path", help="Path to the transcript file")
    parser_clean.add_argument(
        "--output",
        default="data/cleaned_transcript.txt",
        help="Path to save the cleaned transcript",
    )

    # Extract command
    parser_extract = subparsers.add_parser(
        "extract", help="Extract information from the transcript"
    )
    parser_extract.add_argument(
        "transcript_path",
        nargs="?",
        default="data/cleaned_transcript.txt",
        help="Path to the transcript file",
    )
    parser_extract.add_argument(
        "--output",
        default="data/extract.txt",
        help="Path to save the extracted information",
    )

    # Generate command
    parser_generate = subparsers.add_parser(
        "generate", help="Generate a narrative from the extracted information"
    )
    parser_generate.add_argument(
        "transcript_path",
        nargs="?",
        default="data/reviewed_extract.txt",
        help="Path to the extracted data file",
    )
    parser_generate.add_argument(
        "--output",
        default="data/narrative.txt",
        help="Path to save the generated narrative",
    )

    # Review command
    review_parser = subparsers.add_parser("review", help="Review extracted data")
    review_parser.add_argument(
        "extracted_data_path",
        type=str,
        nargs="?",
        default="data/extract.txt",
        help="Path to the extracted data file",
    )
    review_parser.add_argument(
        "--output",
        type=str,
        default="data/reviewed_extract.txt",
        help="Path to the reviewed output file",
    )

    return parser


def execute_command(args, components):
    """Execute the command based on parsed arguments."""
    cleaner, extractor, narrative_manager, extract_reviewer = components

    command_map = {
        "clean": CleanCommand(cleaner),
        "extract": ExtractCommand(extractor),
        "generate": GenerateCommand(narrative_manager),
        "review": ReviewCommand(extract_reviewer),
    }

    command = command_map.get(args.command)
    if command:
        if args.command == "review":
            command.execute(args.extracted_data_path, args.output)
        else:
            command.execute(args.transcript_path, args.output)
    else:
        print(f"Unknown command: {args.command}")


def main():
    print("Main function called")
    parser = create_parser()
    try:
        args = parser.parse_args()
    except SystemExit as e:
        error_message = (
            "error: argument command: invalid choice"
            if e.code == 2
            else "Unknown error"
        )
        print(f"Error: cli.py: {error_message}")
        raise

    components = initialize_components()
    execute_command(args, components)


if __name__ == "__main__":
    main()
