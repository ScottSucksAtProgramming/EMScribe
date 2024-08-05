from unittest.mock import MagicMock

import pytest

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor


@pytest.fixture(name="mock_model_loader")
def fixture_mock_model_loader():
    mock_loader = MagicMock(spec=ModelLoader)
    mock_loader.context_window = 32000
    return mock_loader


@pytest.fixture(name="mock_prompt_manager")
def fixture_mock_prompt_manager():
    return MagicMock(spec=PromptManager)


@pytest.fixture(name="transcript_extractor")
def fixture_transcript_extractor(mock_model_loader, mock_prompt_manager):
    return TranscriptExtractor(
        model_loader=mock_model_loader, prompt_manager=mock_prompt_manager
    )


def test_extract_transcript(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    """
    Test extracting information from a transcript with multiple prompts.
    """
    prompt_keys = [
        "incident_info",
        "patient_demographics",
        "subjective_info",
        "history_of_present_illness",
        "patient_histories",
        "objective_1",
        "objective_2",
        "vitals",
        "poc_tests",
        "labs",
        "imaging",
        "impressions",
        "treatments",
        "packaging",
        "transport",
        "transfer_of_care",
    ]
    mock_prompt_manager.get_prompt.side_effect = (
        lambda key, transcript: f"prompt for {key}"
    )
    mock_model_loader.generate.side_effect = lambda prompt: f"response for {prompt}"

    transcript = "This is a test transcript."
    response = transcript_extractor.extract(transcript)

    expected_response = "\n\n".join(
        [f"response for prompt for {key}" for key in prompt_keys]
    ).strip()
    assert response == expected_response
    assert mock_prompt_manager.get_prompt.call_count == len(prompt_keys)
    assert mock_model_loader.generate.call_count == len(prompt_keys)


def test_extract_from_prompt_with_string(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    """
    Test extracting information from a transcript with a single string prompt.
    """
    prompt_key = "incident_info"
    mock_prompt_manager.get_prompt.return_value = "string prompt"
    mock_model_loader.generate.return_value = "response for string prompt"

    transcript = "This is a test transcript."
    response = transcript_extractor._extract_from_prompt(prompt_key, transcript)

    assert response == "response for string prompt"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        prompt_key, transcript=transcript
    )
    mock_model_loader.generate.assert_called_once_with("string prompt")


def test_extract_from_prompt_with_list(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    """
    Test extracting information from a transcript with a list of prompts.
    """
    prompt_key = "incident_info"
    mock_prompt_manager.get_prompt.return_value = ["prompt1", "prompt2"]
    mock_model_loader.generate.side_effect = [
        "response for prompt1",
        "response for prompt2",
    ]

    transcript = "This is a test transcript."
    response = transcript_extractor._extract_from_prompt(prompt_key, transcript)

    assert response == "response for prompt1 response for prompt2"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        prompt_key, transcript=transcript
    )
    mock_model_loader.generate.assert_any_call("prompt1")
    mock_model_loader.generate.assert_any_call("prompt2")


def test_extract_from_prompt_key_error(transcript_extractor, mock_prompt_manager):
    """
    Test handling KeyError in _extract_from_prompt method.
    """
    prompt_key = "nonexistent_key"
    mock_prompt_manager.get_prompt.side_effect = KeyError("No prompt found")

    transcript = "This is a test transcript."
    with pytest.raises(KeyError, match=f"No prompt found for key: {prompt_key}"):
        transcript_extractor._extract_from_prompt(prompt_key, transcript)


def test_extract_from_prompt_generic_error(transcript_extractor, mock_prompt_manager):
    """
    Test handling a generic error in _extract_from_prompt method.
    """
    prompt_key = "incident_info"
    mock_prompt_manager.get_prompt.side_effect = Exception("Generic error")

    transcript = "This is a test transcript."
    with pytest.raises(
        RuntimeError, match="Error extracting information: Generic error"
    ):
        transcript_extractor._extract_from_prompt(prompt_key, transcript)
