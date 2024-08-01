import sys
import os


class CleanCommand:
    def __init__(self, cleaner):
        self.cleaner = cleaner

    def execute(self, transcript_path, output_path="data/cleaned_transcript.txt"):
        if transcript_path == "-":
            transcript = sys.stdin.read()
        else:
            with open(transcript_path, "r") as file:
                transcript = file.read()

        cleaned_transcript = self.cleaner.clean(transcript)

        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as file:
                file.write(cleaned_transcript)
        else:
            print(cleaned_transcript)
            import pyperclip

            pyperclip.copy(cleaned_transcript)
