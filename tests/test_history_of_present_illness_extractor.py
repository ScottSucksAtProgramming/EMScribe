import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from modules.pdf_extractors.history_of_present_illness_extractor import (
    HistoryOfPresentIllnessExtractor,
)


@pytest.fixture
def extractor():
    return HistoryOfPresentIllnessExtractor()


def test_extract_associated_signs_and_symptoms(extractor):
    mock_pdf_path = "mock_pdf.pdf"

    with patch("tabula.read_pdf") as mock_read_pdf:
        mock_read_pdf.return_value = [
            pd.DataFrame(
                {
                    "Unnamed: 0": [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "Signs & Symptoms",
                        "",
                    ],
                    "Unnamed: 1": [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ],
                    "Unnamed: 2": [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "Symptom A",
                    ],
                    "Unnamed: 3": [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "Symptom B",
                    ],
                }
            )
        ]

        result = extractor.extract(mock_pdf_path)
        assert result["Associated Signs and Symptoms"] == "Symptom A, Symptom B"


def test_extract_associated_signs_and_symptoms_no_info(extractor):
    mock_pdf_path = "mock_pdf.pdf"

    with patch("tabula.read_pdf") as mock_read_pdf:
        mock_read_pdf.return_value = [
            pd.DataFrame(
                {
                    "Unnamed: 0": [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ],
                    "Unnamed: 1": [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ],
                    "Unnamed: 2": [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ],
                    "Unnamed: 3": [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ],
                }
            )
        ]

        result = extractor.extract(mock_pdf_path)
        assert result["Associated Signs and Symptoms"] == "[No Info]"


def test_extract_associated_signs_and_symptoms_error(extractor):
    mock_pdf_path = "mock_pdf.pdf"

    with patch("tabula.read_pdf", side_effect=Exception("Error reading PDF")):
        result = extractor.extract(mock_pdf_path)
        assert (
            "Error extracting signs and symptoms"
            in result["Associated Signs and Symptoms"]
        )


def test_extract_placeholder_methods(extractor):
    assert extractor._extract_onset() == "[No Info]"
    assert extractor._extract_provocation() == "[No Info]"
    assert extractor._extract_palliation() == "[No Info]"
    assert extractor._extract_quality() == "[No Info]"
    assert extractor._extract_radiation() == "[No Info]"
    assert extractor._extract_severity() == "[No Info]"
    assert extractor._extract_time() == "[No Info]"
    assert extractor._extract_interventions() == "[No Info]"
    assert extractor._extract_additional_history_of_present_illness() == "[No Info]"


def test_extract_signs_symptoms(extractor):
    tables = [
        pd.DataFrame(
            {
                "Unnamed: 0": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Signs & Symptoms",
                    "",
                ],
                "Unnamed: 1": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 2": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Symptom A",
                ],
                "Unnamed: 3": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Symptom B",
                ],
            }
        )
    ]

    result = extractor._extract_signs_symptoms(tables)
    assert result == "Symptom A, Symptom B"


def test_extract_signs_symptoms_no_info(extractor):
    tables = [
        pd.DataFrame(
            {
                "Unnamed: 0": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 1": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 2": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 3": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
            }
        )
    ]

    result = extractor._extract_signs_symptoms(tables)
    assert result == "[No Info]"


def test_extract_signs_symptoms_varied_structure(extractor):
    tables = [
        pd.DataFrame(
            {
                "Unnamed: 0": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Signs & Symptoms",
                    "",
                ],
                "Unnamed: 1": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 2": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Symptom A",
                    "Symptom C",
                ],
                "Unnamed: 3": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Symptom B",
                    "Symptom D",
                ],
            }
        )
    ]

    result = extractor._extract_signs_symptoms(tables)
    assert result == "Symptom A, Symptom B, Symptom C, Symptom D"


@pytest.fixture
def mock_extractor():
    return HistoryOfPresentIllnessExtractor()


def test_no_signs_symptoms_found(mock_extractor):
    tables = [
        pd.DataFrame(
            {
                "Unnamed: 0": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 1": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 2": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 3": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
            }
        )
    ]

    result = mock_extractor._extract_signs_symptoms(tables)
    assert result == "[No Info]"


def test_signs_symptoms_found(mock_extractor):
    tables = [
        pd.DataFrame(
            {
                "Unnamed: 0": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Signs & Symptoms",
                    "",
                ],
                "Unnamed: 1": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "Unnamed: 2": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Symptom A",
                ],
                "Unnamed: 3": [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Symptom B",
                ],
            }
        )
    ]

    result = mock_extractor._extract_signs_symptoms(tables)
    assert result == "Symptom A, Symptom B"
