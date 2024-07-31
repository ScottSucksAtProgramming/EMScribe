import sys
import os

class ExtractCommand:
    def __init__(self, extractor):
        self.extractor = extractor

    def execute(self, transcript_path, output_path):
        if transcript_path == "-":
            transcript = sys.stdin.read()
        else:
            with open(transcript_path, "r") as file:
                transcript = file.read()

        extracted_data = self.extractor.extract(transcript)

        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as file:
                file.write(extracted_data)
        else:
            print(extracted_data)
            import pyperclip
            pyperclip.copy(extracted_data)