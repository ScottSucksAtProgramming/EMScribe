import argparse
import pyperclip

from modules.prompt_manager import PromptManager
from modules.model_loader import ModelLoader
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
extractor = TranscriptExtractor(model_loader, prompt_manager)

# Initialize NarrativeManager with the ModelLoader and PromptManager
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

def clean_transcript(transcript):
    cleaned_transcript = cleaner.clean(transcript)
    return cleaned_transcript

def extract_information(transcript):
    extracted_data = extractor.extract(transcript)
    return extracted_data

def generate_narrative(transcript):
    extracted_data = extractor.extract(transcript)
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    return narrative

def save_output(output, output_path):
    with open(output_path, 'w') as file:
        file.write(output)

def main():
    parser = argparse.ArgumentParser(description="EMScribe 2.0 CLI")
    parser.add_argument('function', choices=['clean', 'extract', 'generate'], help="Function to perform: clean, extract, or generate")
    parser.add_argument('transcript_path', help="Path to the transcript text file")
    parser.add_argument('--output', help="Path to save the output to a file")

    args = parser.parse_args()

    with open(args.transcript_path, 'r') as file:
        transcript = file.read()

    if args.function == 'clean':
        output = clean_transcript(transcript)
    elif args.function == 'extract':
        output = extract_information(transcript)
    elif args.function == 'generate':
        output = generate_narrative(transcript)

    # Always copy the output to the clipboard
    pyperclip.copy(output)
    print("Output copied to clipboard")

    # Save the output to a file if specified
    if args.output:
        save_output(output, args.output)
        print(f"Output also saved to {args.output}")

    # Print the output to the console
    print(output)

if __name__ == "__main__":
    main()
