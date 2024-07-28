# tests/test_transcript_extractor.py

import pytest
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor

@pytest.fixture
def extractor():
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    prompt_manager = PromptManager()
    return TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

@pytest.fixture
def extracted_data(extractor):
    transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
    return extractor.extract(transcript)

def test_extracted_data_is_string(extracted_data):
    assert isinstance(extracted_data, str)

def test_extracted_data_contains_call_info(extracted_data):
    assert "call information" in extracted_data.lower()

def test_extracted_data_contains_patient_demographics(extracted_data):
    assert "patient demographics" in extracted_data.lower()

def test_extracted_data_contains_patient_histories(extracted_data):
    assert "patient histories" in extracted_data.lower()

def test_patient_name(extracted_data):
    assert "john doe" in extracted_data.lower()

def test_patient_age(extracted_data):
    assert "45" in extracted_data.lower()

def test_patient_gender(extracted_data):
    assert "male" in extracted_data.lower()

def test_patient_hypertension(extracted_data):
    assert "hypertension" in extracted_data.lower()

def test_patient_diabetes(extracted_data):
    assert "diabetes" in extracted_data.lower()