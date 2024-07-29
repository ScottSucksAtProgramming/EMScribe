import sys
import argparse
import pyperclip
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager

# Initialize PromptManager
prompt_manager = PromptManager()

# Initialize ModelLoader with the base URL for the AI model server and model name
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize TranscriptCleaner with the ModelLoader and PromptManager
cleaner = TranscriptCleaner(model_loader, prompt_manager)

# Initialize TranscriptExtractor with the ModelLoader and PromptManager
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

# Initialize NarrativeManager with the ModelLoader and PromptManager
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

def main():
    parser = argparse.ArgumentParser(description="EMScribe CLI tool")
    parser.add_argument("command", choices=["clean", "extract", "generate"], help="Command to run")
    parser.add_argument("transcript_path", help="Path to the transcript file or '-' to read from stdin")
    parser.add_argument("--output", help="Path to save the output")

    args = parser.parse_args()

    if args.transcript_path == "-":
        transcript = sys.stdin.read()
    else:
        with open(args.transcript_path, "r") as file:
            transcript = file.read()

    if args.command == "clean":
        cleaned_transcript = cleaner.clean(transcript)
        output = cleaned_transcript
    elif args.command == "extract":
        extracted_data = extractor.extract(transcript)
        output = extracted_data
    elif args.command == "generate":
        narrative = narrative_manager.generate_narrative("presoaped_format", data=transcript)
        output = narrative

    if args.output:
        with open(args.output, "w") as file:
            file.write(output)
    else:
        print(output)

    # Copy to clipboard
    pyperclip.copy(output)
    print("Output has been copied to the clipboard.")

if __name__ == "__main__":
    main()
