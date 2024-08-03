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


def test_extract_standard_prompts(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.side_effect = lambda key, transcript: f"{key} prompt"
    mock_model_loader.generate.side_effect = lambda prompt: f"response for {prompt}"

    transcript = "This is a test transcript."
    response = transcript_extractor.extract(transcript)

    expected_response = "\n\n".join(
        [
            f"response for {key} prompt"
            for key in [
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
        ]
    ).strip()

    assert response == expected_response
    assert mock_prompt_manager.get_prompt.call_count == 16
    assert mock_model_loader.generate.call_count == 16


def test_extract_with_chunks(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.side_effect = lambda key, transcript: [
        f"{key} chunk1",
        f"{key} chunk2",
    ]
    mock_model_loader.generate.side_effect = lambda prompt: f"response for {prompt}"

    transcript = "This is a test transcript."
    response = transcript_extractor.extract(transcript)

    expected_response = "\n\n".join(
        [
            "response for incident_info chunk1 response for incident_info chunk2",
            "response for patient_demographics chunk1 response for patient_demographics chunk2",
            "response for subjective_info chunk1 response for subjective_info chunk2",
            (
                "response for history_of_present_illness "
                "chunk1 response for history_of_present_illness chunk2"
            ),
            "response for patient_histories chunk1 response for patient_histories chunk2",
            "response for objective_1 chunk1 response for objective_1 chunk2",
            "response for objective_2 chunk1 response for objective_2 chunk2",
            "response for vitals chunk1 response for vitals chunk2",
            "response for poc_tests chunk1 response for poc_tests chunk2",
            "response for labs chunk1 response for labs chunk2",
            "response for imaging chunk1 response for imaging chunk2",
            "response for impressions chunk1 response for impressions chunk2",
            "response for treatments chunk1 response for treatments chunk2",
            "response for packaging chunk1 response for packaging chunk2",
            "response for transport chunk1 response for transport chunk2",
            "response for transfer_of_care chunk1 response for transfer_of_care chunk2",
        ]
    ).strip()

    assert response == expected_response
    assert mock_prompt_manager.get_prompt.call_count == 16
    assert mock_model_loader.generate.call_count == 32


def test_extract_empty_transcript(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = "empty prompt"
    mock_model_loader.generate.return_value = "empty response"

    transcript = ""
    response = transcript_extractor.extract(transcript)

    expected_response = "\n\n".join(["empty response"] * 16).strip()

    assert response == expected_response
    assert mock_prompt_manager.get_prompt.call_count == 16
    assert mock_model_loader.generate.call_count == 16


def test_extract_nonexistent_prompt_key(transcript_extractor, mock_prompt_manager):
    mock_prompt_manager.get_prompt.side_effect = KeyError("No prompt found")

    transcript = "This is a test transcript."
    with pytest.raises(KeyError):
        transcript_extractor.extract(transcript)


def test_extract_model_error(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = "standard prompt"
    mock_model_loader.generate.side_effect = RuntimeError("Model error")

    transcript = "This is a test transcript."
    with pytest.raises(RuntimeError):
        transcript_extractor.extract(transcript)


def test_extract_special_characters(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    special_prompt = "Prompt with special characters: !@#$%^&*()"
    mock_prompt_manager.get_prompt.return_value = special_prompt
    mock_model_loader.generate.return_value = (
        "response with special characters: !@#$%^&*()"
    )

    transcript = "This is a test transcript with special characters: !@#$%^&*()"
    response = transcript_extractor.extract(transcript)

    expected_response = "\n\n".join(
        ["response with special characters: !@#$%^&*()"] * 16
    ).strip()

    assert response == expected_response
    assert mock_prompt_manager.get_prompt.call_count == 16
    assert mock_model_loader.generate.call_count == 16


def test_extract_large_transcript(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    large_transcript = "This is a large transcript. " * 1000
    mock_prompt_manager.get_prompt.return_value = "large prompt"
    mock_model_loader.generate.return_value = "large response"

    response = transcript_extractor.extract(large_transcript)

    expected_response = "\n\n".join(["large response"] * 16).strip()

    assert response == expected_response
    assert mock_prompt_manager.get_prompt.call_count == 16
    assert mock_model_loader.generate.call_count == 16


def test_extract_mixed_chunks_and_single(
    transcript_extractor, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.side_effect = lambda key, transcript: (
        [f"{key} chunk1", f"{key} chunk2"]
        if key in ["incident_info", "patient_demographics"]
        else f"{key} prompt"
    )
    mock_model_loader.generate.side_effect = lambda prompt: f"response for {prompt}"

    transcript = "This is a test transcript."
    response = transcript_extractor.extract(transcript)

    expected_response = "\n\n".join(
        [
            "response for incident_info chunk1 response for incident_info chunk2",
            "response for patient_demographics chunk1 response for patient_demographics chunk2",
            "response for subjective_info prompt",
            "response for history_of_present_illness prompt",
            "response for patient_histories prompt",
            "response for objective_1 prompt",
            "response for objective_2 prompt",
            "response for vitals prompt",
            "response for poc_tests prompt",
            "response for labs prompt",
            "response for imaging prompt",
            "response for impressions prompt",
            "response for treatments prompt",
            "response for packaging prompt",
            "response for transport prompt",
            "response for transfer_of_care prompt",
        ]
    ).strip()

    assert response == expected_response
    assert mock_prompt_manager.get_prompt.call_count == 16
    assert mock_model_loader.generate.call_count == 18
