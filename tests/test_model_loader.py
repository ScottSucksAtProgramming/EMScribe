from unittest.mock import MagicMock, patch

import pytest
from langchain_community.llms.ollama import Ollama

from modules.model_loader import ModelLoader


@pytest.fixture(name="mock_ollama")
def fixture_mock_ollama():
    return MagicMock(spec=Ollama)


@pytest.fixture(name="model_loader")
def fixture_model_loader(mock_ollama):
    return ModelLoader(model_name="test_model", client=mock_ollama)


def test_initialization_with_client(mock_ollama):
    """
    Test ModelLoader initialization with a provided client.
    """
    model_loader = ModelLoader(model_name="test_model", client=mock_ollama)
    assert model_loader.model_name == "test_model"
    assert model_loader.client == mock_ollama
    assert model_loader.base_url == "http://localhost:11434"
    assert model_loader.context_window == 32768


def test_initialization_without_client():
    """
    Test ModelLoader initialization without a provided client.
    """
    with patch("modules.model_loader.Ollama") as MockOllama:
        mock_instance = MockOllama.return_value
        model_loader = ModelLoader(model_name="test_model")
        MockOllama.assert_called_once_with(base_url="http://localhost:11434")
        assert model_loader.client == mock_instance


def test_generate(model_loader, mock_ollama):
    """
    Test the generate method of ModelLoader.
    """
    mock_response = MagicMock()
    mock_response.generations = [[MagicMock(text="Mocked response")]]
    mock_ollama.generate.return_value = mock_response

    response = model_loader.generate("test prompt")

    assert response == "Mocked response"
    mock_ollama.generate.assert_called_once_with(
        model="test_model", prompts=["test prompt"], options={"num_ctx": 32768}
    )


def test_generate_with_exception(model_loader, mock_ollama):
    """
    Test the generate method to handle exceptions.
    """
    mock_ollama.generate.side_effect = Exception("Test exception")

    with pytest.raises(RuntimeError, match="Error generating response: Test exception"):
        model_loader.generate("test prompt")
