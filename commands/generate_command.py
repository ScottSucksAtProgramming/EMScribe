import sys
import os
from typing import Optional

from modules.narrative_manager import NarrativeManager


class GenerateCommand:
    """
    Command class to handle the generation of narratives from extracted data.

    Attributes:
        narrative_manager (NarrativeManager): An instance of NarrativeManager to generate the narrative.
    """

    def __init__(self, narrative_manager: NarrativeManager):
        """
        Initializes the GenerateCommand with a NarrativeManager instance.

        Args:
            narrative_manager (NarrativeManager): An instance of NarrativeManager to generate the narrative.
        """
        self.narrative_manager = narrative_manager

    def execute(
        self,
        extracted_data_path: str,
        output_path: Optional[str] = "data/narrative.txt",
    ) -> None:
        """
        Executes the narrative generation process on the given extracted data file and saves the output.

        Args:
            extracted_data_path (str): The path to the extracted data file or '-' to read from stdin.
            output_path (Optional[str]): The path to save the generated narrative. If None, prints the output and copies to clipboard.

        Raises:
            IOError: If there is an error reading or writing the files.
            ImportError: If there is an error importing pyperclip for clipboard operations.
        """
        try:
            if extracted_data_path == "-":
                extracted_data = sys.stdin.read()
            else:
                with open(extracted_data_path, "r") as file:
                    extracted_data = file.read()

            narrative = self.narrative_manager.generate_narrative(
                "presoaped_format", data=extracted_data
            )

            if output_path:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, "w") as file:
                    file.write(narrative)
            else:
                print(narrative)
                try:
                    import pyperclip

                    pyperclip.copy(narrative)
                except ImportError as e:
                    raise ImportError(f"pyperclip module not found: {e}")
        except IOError as e:
            raise IOError(f"Error processing files: {e}")
