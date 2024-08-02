# -*- coding: utf-8 -*-
# commands/review_command.py

"""
Module for reviewing extracted EMS data.

This module defines the ReviewCommand class which is responsible for reviewing
extracted EMS data using the ExtractReviewer.
"""


class ReviewCommand:
    """
    Command class for reviewing extracted EMS data.

    This class provides a method to execute the review of extracted EMS data
    and save the reviewed data to a file.
    """

    def __init__(self, reviewer):
        """
        Initialize the ReviewCommand with an ExtractReviewer.

        Args:
            reviewer (ExtractReviewer): An instance of ExtractReviewer.
        """
        self.reviewer = reviewer

    def execute(self, extracted_data_path, output_path):
        """
        Execute the review process on the provided extracted data file.

        Args:
            extracted_data_path (str): The path to the extracted data file.
            output_path (str): The path to save the reviewed data.
        """
        with open(extracted_data_path, "r", encoding="utf-8") as file:
            extracted_data = file.read()

        sections = extracted_data.split("\n\n")

        reviewed_sections = []
        for section in sections:
            reviewed_section = self.reviewer.review_section(section)
            reviewed_sections.append(reviewed_section)
            if "done" in reviewed_section.lower():
                break

        reviewed_data = "\n\n".join(reviewed_sections)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(reviewed_data)

    def summary(self):
        """
        Provide a summary of the review process.

        Returns:
            str: Summary of the review process.
        """
        return "ReviewCommand: Reviews extracted EMS data using ExtractReviewer."
