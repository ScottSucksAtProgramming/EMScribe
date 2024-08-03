# -*- coding: utf-8 -*-
# modules/narrative_manager.py

"""
Module for managing EMS narratives.

This module defines the NarrativeManager class which is responsible for generating
and managing EMS narratives.
"""


class NarrativeManager:
    """
    Class for generating and managing EMS narratives.

    This class provides methods to generate narratives from extracted EMS data.
    """

    def __init__(self, model_loader, prompt_manager):
        """
        Initialize the NarrativeManager with a ModelLoader and PromptManager.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader.
            prompt_manager (PromptManager): An instance of PromptManager.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def generate_narrative(self, extracted_data):
        """
        Generate a narrative from the extracted EMS data.

        Args:
            extracted_data (str): The extracted EMS data.

        Returns:
            str: The generated narrative.
        """
        narrative = ""
        for step in self.prompt_manager.get_steps():
            prompt = self.prompt_manager.get_prompt(step, {"data": extracted_data})
            response = self.model_loader.generate(prompt)
            narrative += response + "\n\n"
        return narrative
