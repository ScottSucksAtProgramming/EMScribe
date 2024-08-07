import sys
import os
from typing import Optional

from modules.transcript_extractor import TranscriptExtractor


class ExtractCommand:
    """
    Command class to handle the extraction of information from a transcript.

    Attributes:
        extractor (TranscriptExtractor): An instance of TranscriptExtractor to extract information from the transcript.
    """

    def __init__(self, extractor: TranscriptExtractor):
        """
        Initializes the ExtractCommand with a TranscriptExtractor instance.

        Args:
            extractor (TranscriptExtractor): An instance of TranscriptExtractor to extract information from the transcript.
        """
        self.extractor = extractor

    def execute(
        self, transcript_path: str, output_path: Optional[str] = "data/extract.txt"
    ) -> None:
        """
        Executes the extraction process on the given transcript file and saves or prints the output.

        Args:
            transcript_path (str): The path to the transcript file or '-' to read from stdin.
            output_path (Optional[str]): The path to save the extracted information. If None, prints the output and copies to clipboard.

        Raises:
            IOError: If there is an error reading or writing the files.
            ImportError: If there is an error importing pyperclip for clipboard operations.
        """
        try:
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
                try:
                    import pyperclip

                    pyperclip.copy(extracted_data)
                except ImportError as e:
                    raise ImportError(f"pyperclip module not found: {e}")
        except IOError as e:
            raise IOError(f"Error processing files: {e}")
