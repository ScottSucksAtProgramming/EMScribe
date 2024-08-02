# -*- coding: utf-8 -*-
# modules/extract_reviewer.py

"""
Module for reviewing extracted information.

This module defines the ExtractReviewer class which is responsible for reviewing
extracted EMS data.
"""


class ExtractReviewer:
    """
    Class for reviewing extracted EMS data.

    This class provides methods to review and make corrections to extracted EMS data.
    """

    def __init__(self, model_loader, prompt_manager):
        """
        Initialize the ExtractReviewer with a ModelLoader and PromptManager.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader.
            prompt_manager (PromptManager): An instance of PromptManager.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def review_section(self, section):
        """
        Review a section of extracted EMS data.

        Args:
            section (str): The section of extracted EMS data to review.

        Returns:
            str: The reviewed section.
        """
        prompt = self.prompt_manager.get_prompt(
            "review_section", {"section_data": section}
        )
        response = self.model_loader.load_model().generate(prompt)
        return response

    def summary(self):
        """
        Provide a summary of the review process.

        Returns:
            str: Summary of the review process.
        """
        return "ExtractReviewer: Reviews extracted EMS data using ModelLoader and PromptManager."
