# -*- coding: utf-8 -*-
"""
Configuration file for pytest fixtures.
"""
from unittest.mock import MagicMock, patch
import pytest


@pytest.fixture
def mock_ollama():
    """
    Fixture to mock the Ollama.Model class.

    Returns:
        MagicMock: Mocked Ollama.Model class.
    """
    with patch("modules.model_loader.Ollama") as MockOllama:
        mock_ollama_model = MagicMock()
        MockOllama.Model.return_value = mock_ollama_model
        yield mock_ollama_model
