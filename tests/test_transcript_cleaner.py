# tests/test_transcript_cleaner.py

import pytest
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner


@pytest.fixture
def cleaner():
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    prompt_manager = PromptManager()
    return TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)


@pytest.fixture
def cleaned_transcript(cleaner):
    transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    return cleaner.clean(transcript)


def test_clean_is_string(cleaned_transcript):
    assert isinstance(cleaned_transcript, str)


def test_no_repeating_experiencing(cleaned_transcript):
    assert "experiencing experiencing" not in cleaned_transcript


def test_no_repeating_patient_is(cleaned_transcript):
    assert "The patient is The patient is" not in cleaned_transcript
