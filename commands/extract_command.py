# -*- coding: utf-8 -*-
# commands/extract_command.py

"""
Module for extracting information from EMS transcripts.

This module defines the ExtractCommand class which is responsible for extracting
information from EMS transcripts using the TranscriptExtractor.
"""

import pyperclip


class ExtractCommand:
    """
    Command class for extracting information from EMS transcripts.

    This class provides a method to execute the extraction of information
    from EMS transcripts and save the extracted data to a file.
    """

    def __init__(self, extractor):
        """
        Initialize the ExtractCommand with a TranscriptExtractor.

        Args:
            extractor (TranscriptExtractor): An instance of TranscriptExtractor.
        """
        self.extractor = extractor

    def execute(self, transcript_path, output_path):
        """
        Execute the extraction process on the provided transcript file.

        Args:
            transcript_path (str): The path to the transcript file.
            output_path (str): The path to save the extracted information.
        """
        with open(transcript_path, "r", encoding="utf-8") as file:
            transcript = file.read()

        extracted_data = self.extractor.extract(transcript)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(extracted_data)

        pyperclip.copy(extracted_data)
        print("Extracted data copied to clipboard and saved to", output_path)

    def summary(self):
        """
        Provide a summary of the extraction process.

        Returns:
            str: Summary of the extraction process.
        """
        return (
            "ExtractCommand: Extracts information from EMS transcripts using "
            "TranscriptExtractor."
        )
