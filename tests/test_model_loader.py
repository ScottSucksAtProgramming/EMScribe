# tests/test_model_loader.py

import pytest
from modules.model_loader import ModelLoader

@pytest.fixture
def model_loader():
    return ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

@pytest.fixture
def response(model_loader):
    prompt = "Test prompt"
    return model_loader.generate(prompt)

def test_generate_is_string(response):
    assert isinstance(response, str)  # Check if the response is a string

def test_generate_not_empty(response):
    assert len(response) > 0  # Check if the response is not empty