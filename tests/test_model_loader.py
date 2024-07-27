import pytest
from modules.model_loader import ModelLoader

@pytest.fixture
def model_loader():
    return ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

def test_generate(model_loader):
    prompt = "Test prompt"
    response = model_loader.generate(prompt)
    assert isinstance(response, str)  # Check if the response is a string
    assert len(response) > 0  # Check if the response is not empty