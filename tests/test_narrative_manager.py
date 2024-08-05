from unittest.mock import MagicMock

import pytest

from modules.model_loader import ModelLoader
from modules.narrative_manager import NarrativeManager
from modules.prompt_manager import PromptManager


@pytest.fixture(name="mock_model_loader")
def fixture_mock_model_loader():
    mock_loader = MagicMock(spec=ModelLoader)
    mock_loader.context_window = 32000
    return mock_loader


@pytest.fixture(name="mock_prompt_manager")
def fixture_mock_prompt_manager():
    return MagicMock(spec=PromptManager)


@pytest.fixture(name="narrative_manager")
def fixture_narrative_manager(mock_model_loader, mock_prompt_manager):
    return NarrativeManager(
        model_loader=mock_model_loader, prompt_manager=mock_prompt_manager
    )


def test_generate_narrative(narrative_manager, mock_prompt_manager, mock_model_loader):
    """
    Test generating a narrative with given data and format.
    """
    mock_prompt_manager.get_prompt.return_value = {
        "step1": "Prompt for step 1",
        "step2": "Prompt for step 2",
    }
    mock_model_loader.generate.side_effect = [
        "Response for step 1",
        "Response for step 2",
    ]

    data = {"key": "value"}
    response = narrative_manager.generate_narrative("narrative_format", data)

    assert response == "Response for step 1\n\nResponse for step 2"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "narrative_format", data=data
    )
    mock_model_loader.generate.assert_any_call("Prompt for step 1")
    mock_model_loader.generate.assert_any_call("Prompt for step 2")


def test_generate_narrative_with_long_prompt(
    narrative_manager, mock_prompt_manager, mock_model_loader
):
    """
    Test generating a narrative when the prompt exceeds the context window size.
    """
    long_prompt = "A" * 35000
    mock_prompt_manager.get_prompt.return_value = {"step1": long_prompt}
    mock_model_loader.generate.side_effect = ["Response part 1", "Response part 2"]

    data = {"key": "value"}
    response = narrative_manager.generate_narrative("narrative_format", data)

    assert response == "Response part 1 Response part 2"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "narrative_format", data=data
    )
    mock_model_loader.generate.assert_any_call("A" * 32000)
    mock_model_loader.generate.assert_any_call("A" * 3000)


def test_generate_narrative_empty_data(
    narrative_manager, mock_prompt_manager, mock_model_loader
):
    """
    Test generating a narrative with empty data.
    """
    mock_prompt_manager.get_prompt.return_value = {"step1": "Prompt for step 1"}
    mock_model_loader.generate.return_value = "Response for step 1"

    data = {}
    response = narrative_manager.generate_narrative("narrative_format", data)

    assert response == "Response for step 1"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "narrative_format", data=data
    )
    mock_model_loader.generate.assert_called_once_with("Prompt for step 1")


def test_generate_narrative_nonexistent_prompt_key(
    narrative_manager, mock_prompt_manager
):
    """
    Test generating a narrative with a nonexistent prompt key.
    """
    mock_prompt_manager.get_prompt.side_effect = KeyError("No prompt found")

    data = {"key": "value"}
    with pytest.raises(KeyError):
        narrative_manager.generate_narrative("narrative_format", data)


def test_generate_narrative_model_error(
    narrative_manager, mock_prompt_manager, mock_model_loader
):
    """
    Test handling an error from the model while generating a narrative.
    """
    mock_prompt_manager.get_prompt.return_value = {"step1": "Prompt for step 1"}
    mock_model_loader.generate.side_effect = RuntimeError("Model error")

    data = {"key": "value"}
    with pytest.raises(RuntimeError):
        narrative_manager.generate_narrative("narrative_format", data)


def test_generate_narrative_special_characters(
    narrative_manager, mock_prompt_manager, mock_model_loader
):
    """
    Test generating a narrative with special characters in the prompt.
    """
    special_prompt = "Prompt with special characters: !@#$%^&*()"
    mock_prompt_manager.get_prompt.return_value = {"step1": special_prompt}
    mock_model_loader.generate.return_value = (
        "Response with special characters: !@#$%^&*()"
    )

    data = {"key": "value"}
    response = narrative_manager.generate_narrative("narrative_format", data)

    assert response == "Response with special characters: !@#$%^&*()"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "narrative_format", data=data
    )
    mock_model_loader.generate.assert_called_once_with(special_prompt)
