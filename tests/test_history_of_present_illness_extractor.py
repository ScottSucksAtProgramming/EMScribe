import pytest
from modules.pdf_extractors.history_of_present_illness_extractor import (
    HistoryOfPresentIllnessExtractor,
)


@pytest.fixture
def extractor():
    return HistoryOfPresentIllnessExtractor()


def test_extract(extractor):
    text = "Sample text"
    result = extractor.extract(text)
    expected = {
        "Associated Signs and Symptoms": "[No Info]",
        "Onset": "[No Info]",
        "Provocation": "[No Info]",
        "Palliation": "[No Info]",
        "Quality": "[No Info]",
        "Radiation": "[No Info]",
        "Severity": "[No Info]",
        "Time": "[No Info]",
        "Interventions": "[No Info]",
        "Additional History of Present Illness": "[No Info]",
    }
    assert result == expected


def test_extract_field(extractor):
    text = "Sample text"
    field = "Sample field"
    result = extractor._extract_field(text, field)
    assert result == "[No Info]"


def test_extract_associated_signs_and_symptoms(extractor):
    text = "Sample text"
    result = extractor._extract_associated_signs_and_symptoms(text)
    assert result == "[No Info]"


def test_extract_onset(extractor):
    text = "Sample text"
    result = extractor._extract_onset(text)
    assert result == "[No Info]"


def test_extract_provocation(extractor):
    text = "Sample text"
    result = extractor._extract_provocation(text)
    assert result == "[No Info]"


def test_extract_palliation(extractor):
    text = "Sample text"
    result = extractor._extract_palliation(text)
    assert result == "[No Info]"


def test_extract_quality(extractor):
    text = "Sample text"
    result = extractor._extract_quality(text)
    assert result == "[No Info]"


def test_extract_radiation(extractor):
    text = "Sample text"
    result = extractor._extract_radiation(text)
    assert result == "[No Info]"


def test_extract_severity(extractor):
    text = "Sample text"
    result = extractor._extract_severity(text)
    assert result == "[No Info]"


def test_extract_time(extractor):
    text = "Sample text"
    result = extractor._extract_time(text)
    assert result == "[No Info]"


def test_extract_interventions(extractor):
    text = "Sample text"
    result = extractor._extract_interventions(text)
    assert result == "[No Info]"


def test_extract_additional_history_of_present_illness(extractor):
    text = "Sample text"
    result = extractor._extract_additional_history_of_present_illness(text)
    assert result == "[No Info]"
