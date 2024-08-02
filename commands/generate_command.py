# -*- coding: utf-8 -*-
# commands/generate_command.py

"""
Module for generating narratives from extracted EMS data.

This module defines the GenerateCommand class which is responsible for generating
narratives from extracted EMS data using the NarrativeManager.
"""

import pyperclip


class GenerateCommand:
    """
    Command class for generating narratives from extracted EMS data.

    This class provides a method to execute the generation of narratives
    from extracted EMS data and save the generated narrative to a file.
    """

    def __init__(self, narrative_manager):
        """
        Initialize the GenerateCommand with a NarrativeManager.

        Args:
            narrative_manager (NarrativeManager): An instance of NarrativeManager.
        """
        self.narrative_manager = narrative_manager

    def execute(self, extracted_data_path, output_path):
        """
        Execute the generation process on the provided extracted data file.

        Args:
            extracted_data_path (str): The path to the extracted data file.
            output_path (str): The path to save the generated narrative.
        """
        with open(extracted_data_path, "r", encoding="utf-8") as file:
            extracted_data = file.read()

        narrative = self.narrative_manager.generate_narrative(extracted_data)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(narrative)

        pyperclip.copy(narrative)
        print("Generated narrative copied to clipboard and saved to", output_path)

    def summary(self):
        """
        Provide a summary of the generation process.

        Returns:
            str: Summary of the generation process.
        """
        return (
            "GenerateCommand: Generates narratives from extracted EMS data using "
            "NarrativeManager."
        )
