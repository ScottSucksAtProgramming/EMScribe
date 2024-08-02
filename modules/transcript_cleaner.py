# -*- coding: utf-8 -*-
# modules/transcript_cleaner.py

"""
Module for cleaning EMS transcripts.

This module defines the TranscriptCleaner class which is responsible for cleaning
EMS transcripts.
"""


class TranscriptCleaner:
    """
    Class for cleaning EMS transcripts.

    This class provides methods to clean EMS transcripts using a language model.
    """

    def __init__(self, model_loader, prompt_manager):
        """
        Initialize the TranscriptCleaner with a ModelLoader and PromptManager.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader.
            prompt_manager (PromptManager): An instance of PromptManager.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def clean(self, transcript):
        """
        Clean the provided EMS transcript.

        Args:
            transcript (str): The EMS transcript to clean.

        Returns:
            str: The cleaned transcript.
        """
        prompt = self.prompt_manager.get_prompt(
            "clean_transcript", {"transcript": transcript}
        )
        cleaned_transcript = self.model_loader.load_model().generate(prompt)
        return cleaned_transcript
