import sys
import os
from typing import Optional

from modules.transcript_extractor import TranscriptExtractor
from modules.pdf_extractor import PDFExtractor


class ExtractCommand:
    """
    Command class to handle the extraction of information from a transcript or PDF.

    Attributes:
        transcript_extractor (TranscriptExtractor): An instance of TranscriptExtractor to extract information from text files.
        pdf_extractor (PDFExtractor): An instance of PDFExtractor to extract information from PDF files.
    """

    def __init__(
        self, transcript_extractor: TranscriptExtractor, pdf_extractor: PDFExtractor
    ):
        """
        Initializes the ExtractCommand with a TranscriptExtractor and PDFExtractor instance.

        Args:
            transcript_extractor (TranscriptExtractor): An instance of TranscriptExtractor to extract information from text files.
            pdf_extractor (PDFExtractor): An instance of PDFExtractor to extract information from PDF files.
        """
        self.transcript_extractor = transcript_extractor
        self.pdf_extractor = pdf_extractor

    def execute(
        self, transcript_path: str, output_path: Optional[str] = "data/extract.txt"
    ) -> None:
        """
        Executes the extraction process on the given transcript file and saves or prints the output.

        Args:
            transcript_path (str): The path to the transcript or PDF file or '-' to read from stdin.
            output_path (Optional[str]): The path to save the extracted information. If None, prints the output and copies to clipboard.

        Raises:
            IOError: If there is an error reading or writing the files.
            ImportError: If there is an error importing pyperclip for clipboard operations.
        """
        try:
            if transcript_path == "-":
                content = sys.stdin.read()
            else:
                with open(transcript_path, "rb") as file:
                    content = file.read()

            if transcript_path.endswith(".pdf"):
                extracted_data = self.pdf_extractor.extract(content)
                extracted_data_str = self._format_extracted_data(extracted_data)
            elif transcript_path.endswith(".txt"):
                transcript = content.decode("utf-8")
                extracted_data_str = self.transcript_extractor.extract(transcript)
            else:
                raise ValueError(
                    "Unsupported file type. Only .txt and .pdf files are supported."
                )

            print(f"Extracted data: {extracted_data_str}")  # Debugging statement

            if output_path:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, "w") as file:
                    file.write(extracted_data_str)
            else:
                print(extracted_data_str)
                try:
                    import pyperclip

                    pyperclip.copy(extracted_data_str)
                except ImportError as e:
                    raise ImportError(f"pyperclip module not found: {e}")
        except IOError as e:
            raise IOError(f"Error processing files: {e}")

    def _format_extracted_data(self, data: dict) -> str:
        """Formats the extracted data dictionary into a readable string."""
        formatted_data = ""
        for category, info in data.items():
            formatted_data += f"{category}:\n"
            for key, value in info.items():
                formatted_data += f"  {key}: {value}\n"
        return formatted_data
