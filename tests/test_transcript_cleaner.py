from unittest.mock import MagicMock

import pytest

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner


@pytest.fixture(name="mock_model_loader")
def fixture_mock_model_loader():
    mock_loader = MagicMock(spec=ModelLoader)
    mock_loader.context_window = 32000
    return mock_loader


@pytest.fixture(name="mock_prompt_manager")
def fixture_mock_prompt_manager():
    return MagicMock(spec=PromptManager)


@pytest.fixture(name="transcript_cleaner")
def fixture_transcript_cleaner(mock_model_loader, mock_prompt_manager):
    return TranscriptCleaner(
        model_loader=mock_model_loader, prompt_manager=mock_prompt_manager
    )


def test_clean_transcript(transcript_cleaner, mock_prompt_manager, mock_model_loader):
    mock_prompt_manager.get_prompt.return_value = "cleaning prompt"
    mock_model_loader.generate.return_value = "cleaned transcript"

    transcript = "This is a test transcript."
    response = transcript_cleaner.clean(transcript)

    assert response == "cleaned transcript"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "clean_transcript", transcript=transcript
    )
    mock_model_loader.generate.assert_called_once_with("cleaning prompt")


def test_clean_transcript_with_chunks(
    transcript_cleaner, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = ["chunk1", "chunk2"]
    mock_model_loader.generate.side_effect = ["cleaned chunk1", "cleaned chunk2"]

    transcript = "This is a test transcript."
    response = transcript_cleaner.clean(transcript)

    assert response == "cleaned chunk1 cleaned chunk2"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "clean_transcript", transcript=transcript
    )
    mock_model_loader.generate.assert_any_call("chunk1")
    mock_model_loader.generate.assert_any_call("chunk2")


def test_clean_transcript_empty(
    transcript_cleaner, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = ""
    mock_model_loader.generate.return_value = "cleaned transcript"

    transcript = ""
    response = transcript_cleaner.clean(transcript)

    assert response == "cleaned transcript"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "clean_transcript", transcript=transcript
    )
    mock_model_loader.generate.assert_called_once_with("")


def test_clean_transcript_nonexistent_prompt_key(
    transcript_cleaner, mock_prompt_manager
):
    mock_prompt_manager.get_prompt.side_effect = KeyError("No prompt found")

    transcript = "This is a test transcript."
    with pytest.raises(KeyError):
        transcript_cleaner.clean(transcript)


def test_clean_transcript_model_error(
    transcript_cleaner, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = "cleaning prompt"
    mock_model_loader.generate.side_effect = RuntimeError("Model error")

    transcript = "This is a test transcript."
    with pytest.raises(RuntimeError):
        transcript_cleaner.clean(transcript)


def test_clean_transcript_special_characters(
    transcript_cleaner, mock_prompt_manager, mock_model_loader
):
    special_prompt = "Prompt with special characters: !@#$%^&*()"
    mock_prompt_manager.get_prompt.return_value = special_prompt
    mock_model_loader.generate.return_value = (
        "cleaned transcript with special characters: !@#$%^&*()"
    )

    transcript = "This is a test transcript with special characters: !@#$%^&*()"
    response = transcript_cleaner.clean(transcript)

    assert response == "cleaned transcript with special characters: !@#$%^&*()"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "clean_transcript", transcript=transcript
    )
    mock_model_loader.generate.assert_called_once_with(special_prompt)


def test_clean_transcript_large_input(
    transcript_cleaner, mock_prompt_manager, mock_model_loader
):
    large_transcript = "This is a large transcript. " * 1000
    large_prompt = "cleaning prompt for large input"
    mock_prompt_manager.get_prompt.return_value = large_prompt
    mock_model_loader.generate.return_value = "cleaned large transcript"

    response = transcript_cleaner.clean(large_transcript)

    assert response == "cleaned large transcript"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "clean_transcript", transcript=large_transcript
    )
    mock_model_loader.generate.assert_called_once_with(large_prompt)
