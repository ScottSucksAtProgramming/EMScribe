# -*- coding: utf-8 -*-
"""
Unit tests for the ModelLoader class in the model_loader module.
"""

from modules.model_loader import ModelLoader


def test_model_loader_init(mock_ollama):
    """
    Test the initialization of the ModelLoader class.

    Args:
        mock_ollama (MagicMock): Mocked Ollama.Model class.
    """
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    assert model_loader.base_url == "http://localhost:11434"
    assert model_loader.model_name == "llama3.1"
    assert model_loader.model is mock_ollama


def test_model_loader_generate(mock_ollama):
    """
    Test the generate method of the ModelLoader class.

    Args:
        mock_ollama (MagicMock): Mocked Ollama.Model class.
    """
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    mock_ollama.generate.return_value = "Generated response"
    result = model_loader.generate("Test prompt")
    assert result == "Generated response"
    mock_ollama.generate.assert_called_once_with("Test prompt")
