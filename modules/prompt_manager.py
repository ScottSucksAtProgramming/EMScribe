# -*- coding: utf-8 -*-
# modules/prompt_manager.py

"""
Module for managing prompts used in EMScribe.

This module defines the PromptManager class which is responsible for managing
prompts used in the EMScribe application.
"""


class PromptManager:
    """
    Class for managing prompts used in EMScribe.

    This class provides methods to retrieve and manage prompts for different sections
    of EMS narratives.
    """

    def __init__(self, prompts=None):
        """
        Initialize the PromptManager with optional prompts.

        Args:
            prompts (dict, optional): A dictionary of prompts.
        """
        if prompts is None:
            prompts = {}
        self.prompts = prompts

    def get_prompt(self, section, data):
        """
        Get the prompt for a specific section with the provided data.

        Args:
            section (str): The section to get the prompt for.
            data (dict): The data to include in the prompt.

        Returns:
            str: The prompt for the specified section.
        """
        prompt_template = self.prompts.get(section, "")
        return prompt_template.format(**data)

    def get_steps(self):
        """
        Get the steps for generating a narrative.

        Returns:
            list: A list of steps for generating a narrative.
        """
        return [
            "prearrival",
            "subjective",
            "history_of_present_illness",
            "patient_histories",
            "objective_1",
            "labs_and_tests",
            "assessment",
            "plan",
            "delta",
            "hand_off",
        ]
