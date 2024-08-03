from unittest.mock import MagicMock

import pytest

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from scripts.extraction import EMSExtractor


@pytest.fixture(name="mock_model_loader")
def fixture_mock_model_loader():
    mock_loader = MagicMock(spec=ModelLoader)
    return mock_loader


@pytest.fixture(name="mock_prompt_manager")
def fixture_mock_prompt_manager():
    return MagicMock(spec=PromptManager)


@pytest.fixture(name="ems_extractor_instance")
def fixture_ems_extractor(mock_model_loader, mock_prompt_manager):
    return EMSExtractor(
        model_loader=mock_model_loader, prompt_manager=mock_prompt_manager
    )


def test_extract_information(ems_extractor_instance):
    # Arrange
    transcript = "This is a test transcript."
    cleaned_transcript = "Cleaned transcript."
    extracted_data = "Extracted data."

    mock_cleaner = MagicMock(spec=TranscriptCleaner)
    mock_cleaner.clean.return_value = cleaned_transcript
    ems_extractor_instance.cleaner = mock_cleaner

    mock_extractor = MagicMock(spec=TranscriptExtractor)
    mock_extractor.extract.return_value = extracted_data
    ems_extractor_instance.extractor = mock_extractor

    # Act
    result = ems_extractor_instance.extract_information(transcript)

    # Assert
    assert result == extracted_data
    mock_cleaner.clean.assert_called_once_with(transcript)
    mock_extractor.extract.assert_called_once_with(cleaned_transcript)


if __name__ == "__main__":
    pytest.main()
