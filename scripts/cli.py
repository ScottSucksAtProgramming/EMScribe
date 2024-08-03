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
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url=base_url, model_name=model_name)

    cleaner = TranscriptCleaner(model_loader, prompt_manager)
    extractor = TranscriptExtractor(model_loader, prompt_manager)
    narrative_manager = NarrativeManager(model_loader, prompt_manager)
    extract_reviewer = ExtractReviewer(model_loader, prompt_manager)

    return cleaner, extractor, narrative_manager, extract_reviewer


def parse_args():
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    clean_parser = subparsers.add_parser("clean", help="Clean the transcript")
    clean_parser.add_argument("transcript_path", help="Path to the transcript file")
    clean_parser.add_argument(
        "--output",
        default="data/cleaned_transcript.txt",
        help="Path to save the cleaned transcript",
    )

    extract_parser = subparsers.add_parser(
        "extract", help="Extract information from the transcript"
    )
    extract_parser.add_argument(
        "transcript_path",
        nargs="?",
        default="data/cleaned_transcript.txt",
        help="Path to the transcript file",
    )
    extract_parser.add_argument(
        "--output",
        default="data/extract.txt",
        help="Path to save the extracted information",
    )

    generate_parser = subparsers.add_parser(
        "generate", help="Generate a narrative from the extracted information"
    )
    generate_parser.add_argument(
        "transcript_path",
        nargs="?",
        default="data/reviewed_extract.txt",
        help="Path to the extracted data file",
    )
    generate_parser.add_argument(
        "--output",
        default="data/narrative.txt",
        help="Path to save the generated narrative",
    )

    review_parser = subparsers.add_parser("review", help="Review extracted information")
    review_parser.add_argument(
        "extracted_data_path",
        nargs="?",
        default="data/extract.txt",
        help="Path to the extracted data file",
    )
    review_parser.add_argument(
        "--output",
        default="data/reviewed_extract.txt",
        help="Path to save the reviewed data",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    cleaner, extractor, narrative_manager, extract_reviewer = initialize_components()

    if args.command == "clean":
        CleanCommand(cleaner).execute(args.transcript_path, args.output)
    elif args.command == "extract":
        ExtractCommand(extractor).execute(args.transcript_path, args.output)
    elif args.command == "generate":
        GenerateCommand(narrative_manager).execute(args.transcript_path, args.output)
    elif args.command == "review":
        ReviewCommand(extract_reviewer).execute(args.extracted_data_path, args.output)


if __name__ == "__main__":
    main()
