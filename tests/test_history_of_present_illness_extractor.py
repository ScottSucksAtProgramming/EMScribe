import pytest
from modules.pdf_extractors.history_of_present_illness_extractor import (
    HistoryOfPresentIllnessExtractor,
)


@pytest.fixture
def history_of_present_illness_extractor():
    return HistoryOfPresentIllnessExtractor()


def test_extract_associated_signs_and_symptoms(history_of_present_illness_extractor):
    text = "Associated Signs and Symptoms: Cough, Fever, Sore throat"
    result = (
        history_of_present_illness_extractor._extract_associated_signs_and_symptoms(
            text
        )
    )
    assert result == "Cough, Fever, Sore throat"


def test_extract_associated_signs_and_symptoms_no_info(
    history_of_present_illness_extractor,
):
    text = ""
    result = (
        history_of_present_illness_extractor._extract_associated_signs_and_symptoms(
            text
        )
    )
    assert result == "[No Info]"


def test_extract_onset(history_of_present_illness_extractor):
    text = "Onset: Sudden"
    result = history_of_present_illness_extractor._extract_onset(text)
    assert result == "Sudden"


def test_extract_onset_no_info(history_of_present_illness_extractor):
    text = ""
    result = history_of_present_illness_extractor._extract_onset(text)
    assert result == "[No Info]"


def test_extract_provocation(history_of_present_illness_extractor):
    text = "Provocation: Movement"
    result = history_of_present_illness_extractor._extract_provocation(text)
    assert result == "Movement"


def test_extract_provocation_no_info(history_of_present_illness_extractor):
    text = ""
    result = history_of_present_illness_extractor._extract_provocation(text)
    assert result == "[No Info]"


def test_extract_palliation(history_of_present_illness_extractor):
    text = "Palliation: Rest"
    result = history_of_present_illness_extractor._extract_palliation(text)
    assert result == "Rest"


def test_extract_palliation_no_info(history_of_present_illness_extractor):
    text = ""
    result = history_of_present_illness_extractor._extract_palliation(text)
    assert result == "[No Info]"


def test_extract_quality(history_of_present_illness_extractor):
    text = "Quality: Sharp pain"
    result = history_of_present_illness_extractor._extract_quality(text)
    assert result == "Sharp pain"


def test_extract_quality_no_info(history_of_present_illness_extractor):
    text = ""
    result = history_of_present_illness_extractor._extract_quality(text)
    assert result == "[No Info]"


def test_extract_radiation(history_of_present_illness_extractor):
    text = "Radiation: Left arm"
    result = history_of_present_illness_extractor._extract_radiation(text)
    assert result == "Left arm"


def test_extract_radiation_no_info(history_of_present_illness_extractor):
    text = ""
    result = history_of_present_illness_extractor._extract_radiation(text)
    assert result == "[No Info]"


def test_extract_severity(history_of_present_illness_extractor):
    text = "Severity: 8/10"
    result = history_of_present_illness_extractor._extract_severity(text)
    assert result == "8/10"


def test_extract_severity_no_info(history_of_present_illness_extractor):
    text = ""
    result = history_of_present_illness_extractor._extract_severity(text)
    assert result == "[No Info]"


def test_extract_time(history_of_present_illness_extractor):
    text = "Time: 2 hours ago"
    result = history_of_present_illness_extractor._extract_time(text)
    assert result == "2 hours ago"


def test_extract_time_no_info(history_of_present_illness_extractor):
    text = ""
    result = history_of_present_illness_extractor._extract_time(text)
    assert result == "[No Info]"


def test_extract_interventions(history_of_present_illness_extractor):
    text = "Interventions: Administered aspirin"
    result = history_of_present_illness_extractor._extract_interventions(text)
    assert result == "Administered aspirin"


def test_extract_interventions_no_info(history_of_present_illness_extractor):
    text = ""
    result = history_of_present_illness_extractor._extract_interventions(text)
    assert result == "[No Info]"


def test_extract_additional_history_of_present_illness(
    history_of_present_illness_extractor,
):
    text = "Additional History of Present Illness: Patient has a history of asthma"
    result = history_of_present_illness_extractor._extract_additional_history_of_present_illness(
        text
    )
    assert result == "Patient has a history of asthma"


def test_extract_additional_history_of_present_illness_no_info(
    history_of_present_illness_extractor,
):
    text = ""
    result = history_of_present_illness_extractor._extract_additional_history_of_present_illness(
        text
    )
    assert result == "[No Info]"
