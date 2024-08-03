from unittest.mock import MagicMock

import pytest

from modules.extract_reviewer import ExtractReviewer
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager


@pytest.fixture(name="mock_model_loader")
def fixture_mock_model_loader():
    mock_loader = MagicMock(spec=ModelLoader)
    mock_loader.context_window = 32000
    return mock_loader


@pytest.fixture(name="mock_prompt_manager")
def fixture_mock_prompt_manager():
    return MagicMock(spec=PromptManager)


@pytest.fixture(name="extract_reviewer")
def fixture_extract_reviewer(mock_model_loader, mock_prompt_manager):
    return ExtractReviewer(
        model_loader=mock_model_loader, prompt_manager=mock_prompt_manager
    )


def test_review_section_with_user_input(
    extract_reviewer, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = "formatted prompt"
    mock_model_loader.generate.return_value = "model response"

    response = extract_reviewer.review_section("test section", user_input="user input")

    assert response == "model response"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "review_section", section_data="test section", user_input="user input"
    )
    mock_model_loader.generate.assert_called_once_with("formatted prompt")


def test_review_section_without_user_input(
    extract_reviewer, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = "formatted prompt"
    mock_model_loader.generate.return_value = "model response"

    response = extract_reviewer.review_section("test section")

    assert response == "model response"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "review_section", section_data="test section"
    )
    mock_model_loader.generate.assert_called_once_with("formatted prompt")


def test_final_review(extract_reviewer, mock_prompt_manager, mock_model_loader):
    mock_prompt_manager.get_prompt.return_value = "formatted prompt"
    mock_model_loader.generate.return_value = "model response"

    response = extract_reviewer.final_review("updated section")

    assert response == "model response"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "final_review", updated_section="updated section"
    )
    mock_model_loader.generate.assert_called_once_with("formatted prompt")


def test_review_section_with_long_prompt(
    extract_reviewer, mock_prompt_manager, mock_model_loader
):
    long_prompt = "A" * 35000
    mock_prompt_manager.get_prompt.return_value = long_prompt
    mock_model_loader.generate.side_effect = ["response part 1", "response part 2"]

    response = extract_reviewer.review_section("test section")

    assert response == "response part 1 response part 2"
    assert mock_model_loader.generate.call_count == 2
    mock_model_loader.generate.assert_any_call("A" * 32000)
    mock_model_loader.generate.assert_any_call("A" * 3000)


def test_final_review_with_long_prompt(
    extract_reviewer, mock_prompt_manager, mock_model_loader
):
    long_prompt = "B" * 35000
    mock_prompt_manager.get_prompt.return_value = long_prompt
    mock_model_loader.generate.side_effect = ["response part 1", "response part 2"]

    response = extract_reviewer.final_review("updated section")

    assert response == "response part 1 response part 2"
    assert mock_model_loader.generate.call_count == 2
    mock_model_loader.generate.assert_any_call("B" * 32000)
    mock_model_loader.generate.assert_any_call("B" * 3000)


def test_review_section_nonexistent_prompt_key(extract_reviewer, mock_prompt_manager):
    mock_prompt_manager.get_prompt.side_effect = KeyError("No prompt found")

    with pytest.raises(KeyError):
        extract_reviewer.review_section("test section", user_input="user input")


def test_final_review_nonexistent_prompt_key(extract_reviewer, mock_prompt_manager):
    mock_prompt_manager.get_prompt.side_effect = KeyError("No prompt found")

    with pytest.raises(KeyError):
        extract_reviewer.final_review("updated section")


def test_review_section_empty_string(
    extract_reviewer, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = ""
    mock_model_loader.generate.return_value = "model response"

    response = extract_reviewer.review_section("")

    assert response == "model response"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "review_section", section_data=""
    )
    mock_model_loader.generate.assert_called_once_with("")


def test_final_review_empty_string(
    extract_reviewer, mock_prompt_manager, mock_model_loader
):
    mock_prompt_manager.get_prompt.return_value = ""
    mock_model_loader.generate.return_value = "model response"

    response = extract_reviewer.final_review("")

    assert response == "model response"
    mock_prompt_manager.get_prompt.assert_called_once_with(
        "final_review", updated_section=""
    )
    mock_model_loader.generate.assert_called_once_with("")
