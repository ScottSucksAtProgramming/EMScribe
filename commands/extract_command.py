# -*- coding: utf-8 -*-
import sys
import os
import pyperclip


class ExtractCommand:
    """
    Command to extract data from a transcript.

    This command reads a transcript from a file or standard input, extracts
    relevant data using the provided extractor, and writes the extracted data
    to a specified output file or copies it to the clipboard.
    """

    def __init__(self, extractor):
        self.extractor = extractor

    def execute(self, transcript_path, output_path="data/extract.txt"):
        if transcript_path == "-":
            transcript = sys.stdin.read()
        else:
            with open(transcript_path, "r", encoding="utf-8") as file:
                transcript = file.read()

        extracted_data = self.extractor.extract(transcript)

        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(extracted_data)
        else:
            print(extracted_data)

            pyperclip.copy(extracted_data)
