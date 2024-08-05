from modules.transcript_cleaner import TranscriptCleaner
from typing import Union


class CleanCommand:
    """
    Command class to handle the cleaning of a transcript.

    Attributes:
        cleaner (TranscriptCleaner): An instance of TranscriptCleaner to clean the transcript.
    """

    def __init__(self, cleaner: TranscriptCleaner):
        """
        Initializes the CleanCommand with a TranscriptCleaner instance.

        Args:
            cleaner (TranscriptCleaner): An instance of TranscriptCleaner to clean the transcript.
        """
        self.cleaner = cleaner

    def execute(self, transcript_path: str, output_path: str) -> None:
        """
        Executes the cleaning process on the given transcript file and saves the output.

        Args:
            transcript_path (str): The path to the transcript file.
            output_path (str): The path to save the cleaned transcript.

        Raises:
            IOError: If there is an error reading or writing the files.
        """
        try:
            with open(transcript_path, "r") as file:
                transcript = file.read()

            cleaned_transcript = self.cleaner.clean(transcript)

            with open(output_path, "w") as file:
                file.write(cleaned_transcript)
        except IOError as e:
            raise IOError(f"Error processing files: {e}")
