import pytest
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor

@pytest.fixture
def extractor():
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    prompt_manager = PromptManager()
    return TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

def test_extract(extractor):
    transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
    extracted_data = extractor.extract(transcript)
    print(extracted_data)
    assert isinstance(extracted_data, dict)
    
    # Check if keys exist in the extracted data
    expected_keys = ["incident_info", "patient_demographics", "patient_histories"]
    for key in expected_keys:
        assert key in extracted_data, f"{key} not found in extracted data"
    
    # Check if specific information is within the extracted data
    assert "john doe" in extracted_data["patient_demographics"].lower()
    assert "45" in extracted_data["patient_demographics"].lower()
    assert "male" in extracted_data["patient_demographics"].lower()
    assert "hypertension" in extracted_data["patient_histories"].lower()
    assert "diabetes" in extracted_data["patient_histories"].lower()
    # assert "chest pain" in extracted_data["Chief Complaint"]