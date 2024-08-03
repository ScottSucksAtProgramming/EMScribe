from unittest.mock import MagicMock

import pytest

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner
from scripts.preprocess import TranscriptPreprocessor


@pytest.fixture(name="mock_model_loader")
def fixture_mock_model_loader():
    return MagicMock(spec=ModelLoader)


@pytest.fixture(name="mock_prompt_manager")
def fixture_mock_prompt_manager():
    return MagicMock(spec=PromptManager)


@pytest.fixture(name="preprocessor")
def fixture_preprocessor(mock_model_loader, mock_prompt_manager):
    return TranscriptPreprocessor(
        model_loader=mock_model_loader, prompt_manager=mock_prompt_manager
    )


def test_preprocess_cleaning(preprocessor):
    mock_cleaner = MagicMock(spec=TranscriptCleaner)
    mock_cleaner.clean.return_value = "Cleaned transcript."
    preprocessor.cleaner = mock_cleaner

    transcript = "Raw transcript."
    processed_transcript = preprocessor.preprocess(transcript)

    assert processed_transcript == "Cleaned transcript."
    mock_cleaner.clean.assert_called_once_with(transcript)


def test_preprocess_with_whitespace(preprocessor):
    mock_cleaner = MagicMock(spec=TranscriptCleaner)
    mock_cleaner.clean.return_value = "This   is   a   cleaned   transcript."
    preprocessor.cleaner = mock_cleaner

    transcript = "Raw transcript."
    processed_transcript = preprocessor.preprocess(transcript)

    assert processed_transcript == "This is a cleaned transcript."
    mock_cleaner.clean.assert_called_once_with(transcript)


def test_preprocess_empty_string(preprocessor):
    mock_cleaner = MagicMock(spec=TranscriptCleaner)
    mock_cleaner.clean.return_value = ""
    preprocessor.cleaner = mock_cleaner

    transcript = ""
    processed_transcript = preprocessor.preprocess(transcript)

    assert not processed_transcript
    mock_cleaner.clean.assert_called_once_with(transcript)


def test_preprocess_with_special_characters(preprocessor):
    mock_cleaner = MagicMock(spec=TranscriptCleaner)
    mock_cleaner.clean.return_value = (
        "Cleaned transcript with special characters! @#$%^&*()"
    )
    preprocessor.cleaner = mock_cleaner

    transcript = "Raw transcript with special characters! @#$%^&*()"
    processed_transcript = preprocessor.preprocess(transcript)

    assert (
        processed_transcript == "Cleaned transcript with special characters! @#$%^&*()"
    )
    mock_cleaner.clean.assert_called_once_with(transcript)
