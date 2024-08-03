# conftest.py
from unittest.mock import MagicMock
import pytest
from langchain_community.llms import Ollama
from modules.model_loader import ModelLoader


@pytest.fixture(name="mock_ollama")
def fixture_mock_ollama():
    return MagicMock(spec=Ollama)


@pytest.fixture(name="model_loader")
def fixture_model_loader(mock_ollama):
    return ModelLoader(model_name="test_model", client=mock_ollama)
