# -*- coding: utf-8 -*-
"""
Module for cleaning EMS transcripts.

This module defines the CleanCommand class which is responsible for cleaning
EMS transcripts using the TranscriptCleaner.
"""


class CleanCommand:
    """
    Command class for cleaning EMS transcripts.

    This class provides a method to execute the cleaning of EMS transcripts
    and save the cleaned transcript to a file.
    """

    def __init__(self, cleaner):
        """
        Initialize the CleanCommand with a TranscriptCleaner.

        Args:
            cleaner (TranscriptCleaner): An instance of TranscriptCleaner.
        """
        self.cleaner = cleaner

    def execute(self, transcript_path, output_path):
        """
        Execute the cleaning process on the provided transcript file.

        Args:
            transcript_path (str): The path to the transcript file.
            output_path (str): The path to save the cleaned transcript.
        """
        with open(transcript_path, "r", encoding="utf-8") as file:
            transcript = file.read()

        cleaned_transcript = self.cleaner.clean(transcript)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(cleaned_transcript)

    def summary(self):
        """
        Provide a summary of the cleaning process.

        Returns:
            str: Summary of the cleaning process.
        """
        return "CleanCommand: Cleans EMS transcripts using TranscriptCleaner."
