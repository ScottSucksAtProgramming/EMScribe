import pytest
from unittest.mock import MagicMock, patch
from modules.pdf_extractor import PDFExtractor
from modules.pdf_extractors.incident_information_extractor import (
    IncidentInformationExtractor,
)


@pytest.fixture
def pdf_extractor():
    # Mock the model_loader and prompt_manager as they are not used in this context
    return PDFExtractor(None, None)


def test_extract_text(pdf_extractor):
    with open("pdf_1.pdf", "rb") as file:
        content = file.read()
    text = pdf_extractor._extract_text(content)
    assert isinstance(text, str)
    assert len(text) > 0  # Ensure text is extracted


@patch.object(IncidentInformationExtractor, "extract")
def test_extract_overall(mock_extract, pdf_extractor):
    mock_extract.return_value = {
        "Unit": "5-41-19",
        "Response Mode": "Non-Emergent",
        "Crew Type": "Full Crew",
        "Response Delays": "None/No Delay",
        "Incident Location": "Nursing Home in Stony Brook",
        "Dispatch Complaint": "Transfer/Interfacility/Palliative Care",
    }

    with open("pdf_1.pdf", "rb") as file:
        content = file.read()

    data = pdf_extractor.extract(content)
    mock_extract.assert_called_once()  # Ensure the extract method of IncidentInformationExtractor was called
    assert "Incident Information" in data
    assert data["Incident Information"]["Unit"] == "5-41-19"
    assert data["Incident Information"]["Response Mode"] == "Non-Emergent"
    assert data["Incident Information"]["Crew Type"] == "Full Crew"
    assert data["Incident Information"]["Response Delays"] == "None/No Delay"
    assert (
        data["Incident Information"]["Incident Location"]
        == "Nursing Home in Stony Brook"
    )
    assert (
        data["Incident Information"]["Dispatch Complaint"]
        == "Transfer/Interfacility/Palliative Care"
    )
