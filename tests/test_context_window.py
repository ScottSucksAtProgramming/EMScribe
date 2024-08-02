import pytest
from unittest.mock import MagicMock, patch
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner
from modules.narrative_manager import NarrativeManager
from modules.extract_reviewer import ExtractReviewer


@pytest.fixture
def model_loader():
    return ModelLoader(model_name="test_model")

@pytest.fixture
def prompt_manager():
    return PromptManager()

@pytest.fixture
def cleaner(model_loader, prompt_manager):
    return TranscriptCleaner(model_loader, prompt_manager)

@pytest.fixture
def narrative_manager(model_loader, prompt_manager):
    return NarrativeManager(model_loader, prompt_manager)

@pytest.fixture
def reviewer(model_loader, prompt_manager):
    return ExtractReviewer(model_loader, prompt_manager)


def test_model_loader_context_window(model_loader):
    assert model_loader.context_window == 32768


@patch('langchain_community.llms.Ollama.generate')
def test_clean_transcript_context_window(mock_generate, cleaner, model_loader, prompt_manager):
    transcript = "This is a test transcript."
    prompt_key = "clean_transcript"
    prompt_manager.prompts[prompt_key] = "Clean the following: {transcript}"
    
    # Create a properly structured mock response
    mock_response = MagicMock()
    mock_response.generations = [[MagicMock(text="Cleaned response")]]
    mock_generate.return_value = mock_response

    cleaner.clean(transcript)

    mock_generate.assert_called_once_with(
        model="test_model",
        prompts=["Clean the following: This is a test transcript."],
        options={"num_ctx": 32768}
    )


@patch('langchain_community.llms.Ollama.generate')
def test_review_section_context_window(mock_generate, reviewer, model_loader, prompt_manager):
    section = "This is a section"
    prompt_manager.prompts["review_section"] = "Review: {section_data}"
    
    # Create a properly structured mock response
    mock_response = MagicMock()
    mock_response.generations = [[MagicMock(text="Reviewed response")]]
    mock_generate.return_value = mock_response

    reviewer.review_section(section)

    mock_generate.assert_called_with(
        model="test_model",
        prompts=["Review: This is a section"],
        options={"num_ctx": 32768}
    )


@patch('langchain_community.llms.Ollama.generate')
def test_final_review_context_window(mock_generate, reviewer, model_loader, prompt_manager):
    updated_section = "Updated section"
    prompt_manager.prompts["final_review"] = "Final Review: {updated_section}"
    
    # Create a properly structured mock response
    mock_response = MagicMock()
    mock_response.generations = [[MagicMock(text="Final review response")]]
    mock_generate.return_value = mock_response

    reviewer.final_review(updated_section)

    mock_generate.assert_called_with(
        model="test_model",
        prompts=["Final Review: Updated section"],
        options={"num_ctx": 32768}
    )