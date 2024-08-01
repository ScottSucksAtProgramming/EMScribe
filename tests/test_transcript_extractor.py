import pytest
from unittest.mock import MagicMock
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor


@pytest.fixture
def extractor():
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    prompt_manager = PromptManager()
    extractor = TranscriptExtractor(
        model_loader=model_loader, prompt_manager=prompt_manager
    )
    return extractor


@pytest.fixture
def mock_extracted_data():
    return (
        "Incident Information\n- Unit: 292\n- Response Mode: emergent\n- Crew Type: full crew\n"
        "Patient Demographics\n- Name: John Doe\n- Age: 45\n- Gender: male\n"
        "Patient Histories\n- Hypertension\n- Diabetes\n"
    )


def test_extracted_data_is_string(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert isinstance(extracted_data, str)


def test_extracted_data_contains_call_info(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert "incident information" in extracted_data.lower()


def test_extracted_data_contains_patient_demographics(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert "patient demographics" in extracted_data.lower()


def test_extracted_data_contains_patient_histories(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert "patient histories" in extracted_data.lower()


def test_patient_name(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert "john doe" in extracted_data.lower()


def test_patient_age(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert "45" in extracted_data.lower()


def test_patient_gender(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert "male" in extracted_data.lower()


def test_patient_hypertension(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert "hypertension" in extracted_data.lower()


def test_patient_diabetes(extractor, mock_extracted_data):
    extractor.extract = MagicMock(return_value=mock_extracted_data)
    extracted_data = extractor.extract("mock transcript")
    assert "diabetes" in extracted_data.lower()
