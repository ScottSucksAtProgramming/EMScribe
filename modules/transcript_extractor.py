# -*- coding: utf-8 -*-
# modules/transcript_extractor.py

"""
Module for extracting information from EMS transcripts.

This module defines the TranscriptExtractor class which is responsible for extracting
information from EMS transcripts.
"""


class TranscriptExtractor:
    """
    Class for extracting information from EMS transcripts.

    This class provides methods to extract information from EMS transcripts using
    a language model.
    """

    def __init__(self, model_loader, prompt_manager):
        """
        Initialize the TranscriptExtractor with a ModelLoader and PromptManager.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader.
            prompt_manager (PromptManager): An instance of PromptManager.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def extract(self, transcript):
        """
        Extract information from the provided EMS transcript.

        Args:
            transcript (str): The EMS transcript to extract information from.

        Returns:
            str: The extracted information.
        """
        prompt = self.prompt_manager.get_prompt(
            "extract_transcript", {"transcript": transcript}
        )
        extracted_data = self.model_loader.load_model().generate(prompt)
        return extracted_data
