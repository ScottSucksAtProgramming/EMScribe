from unittest.mock import MagicMock, patch

import pytest

from modules.model_loader import ModelLoader


@pytest.fixture(name="mock_httpx_client")
def fixture_mock_httpx_client():
    return MagicMock()


@pytest.fixture(name="model_loader")
def fixture_model_loader(mock_httpx_client):
    return ModelLoader(model_name="test_model", client=mock_httpx_client)


def test_initialization_with_client(mock_httpx_client):
    """
    Test ModelLoader initialization with a provided client.
    """
    model_loader = ModelLoader(model_name="test_model", client=mock_httpx_client)
    assert model_loader.model_name == "test_model"
    assert model_loader.client == mock_httpx_client
    assert model_loader.base_url == "http://localhost:1234"
    assert model_loader.context_window == 32768


def test_initialization_without_client():
    """
    Test ModelLoader initialization without a provided client.
    """
    with patch("modules.model_loader.httpx.Client") as MockClient:
        mock_instance = MockClient.return_value
        model_loader = ModelLoader(model_name="test_model")
        MockClient.assert_called_once_with(
            base_url="http://localhost:1234", timeout=60.0
        )
        assert model_loader.client == mock_instance


def test_generate(model_loader, mock_httpx_client):
    """
    Test the generate method of ModelLoader.
    """
    mock_resp = MagicMock()
    mock_resp.json.return_value = {
        "choices": [
            {
                "message": {
                    "content": "Mocked response",
                }
            }
        ]
    }
    mock_resp.raise_for_status.return_value = None
    model_loader.client.post.return_value = mock_resp

    response = model_loader.generate("test prompt")

    assert response == "Mocked response"
    model_loader.client.post.assert_called_once()


def test_generate_with_exception(model_loader, mock_httpx_client):
    """
    Test the generate method to handle exceptions.
    """
    model_loader.client.post.side_effect = Exception("Test exception")

    with pytest.raises(RuntimeError, match="Error generating response: Test exception"):
        model_loader.generate("test prompt")
