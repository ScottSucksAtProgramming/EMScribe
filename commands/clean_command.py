# -*- coding: utf-8 -*-
class CleanCommand:
    """
    Command class to handle the cleaning of a transcript.

    Attributes:
        cleaner (TranscriptCleaner): An instance of TranscriptCleaner to clean the transcript.
    """

    def __init__(self, cleaner):
        """
        Initializes the CleanCommand with a TranscriptCleaner instance.

        Args:
            cleaner (TranscriptCleaner): An instance of TranscriptCleaner to clean the transcript.
        """
        self.cleaner = cleaner

    def execute(self, transcript_path, output_path):
        """
        Executes the cleaning process on the given transcript file and saves the output.

        Args:
            transcript_path (str): The path to the transcript file.
            output_path (str): The path to save the cleaned transcript.
        """
        with open(transcript_path, "r", encoding="utf-8") as file:
            transcript = file.read()

        cleaned_transcript = self.cleaner.clean(transcript)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(cleaned_transcript)
