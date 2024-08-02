# -*- coding: utf-8 -*-
# modules/model_loader.py

"""
Module for loading language models.

This module defines the ModelLoader class which is responsible for loading and
managing language models used in EMScribe.
"""
from langchain_community.llms import Ollama


class ModelLoader:
    """
    Class for loading language models.

    This class provides methods to load and manage language models.
    """

    def __init__(self, base_url, model_name):
        """
        Initialize the ModelLoader with the base URL and model name.

        Args:
            base_url (str): The base URL for the model.
            model_name (str): The name of the model.
        """
        self.base_url = base_url
        self.model_name = model_name
        self.model = self._load_model()

    def _load_model(self):
        """
        Load the language model.

        Returns:
            object: The loaded language model.
        """
        try:
            return Ollama.Model(base_url=self.base_url, model_name=self.model_name)
        except ImportError as exc:
            raise ImportError("The ollama module is not installed.") from exc

    def load_model(self):
        """
        Get the loaded language model.

        Returns:
            object: The loaded language model.
        """
        return self.model

    def generate(self, prompt):
        """
        Generate a response from the language model based on the given prompt.

        Args:
            prompt (str): The prompt to generate a response for.

        Returns:
            str: The generated response.
        """
        return self.model.generate(prompt)
