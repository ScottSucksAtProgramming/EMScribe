import pytest
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner

@pytest.fixture
def cleaner():
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    prompt_manager = PromptManager()
    return TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)

def test_clean(cleaner):
    transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    cleaned_transcript = cleaner.clean(transcript)
    assert isinstance(cleaned_transcript, str)
    assert "experiencing experiencing" not in cleaned_transcript
    assert "The patient is The patient is" not in cleaned_transcript