import pytest
from modules.prompts.cleaning_prompts import cleaning_prompts


def test_cleaning_prompts_structure():
    """
    Test to ensure the structure of cleaning_prompts dictionary is correct.
    """
    assert isinstance(cleaning_prompts, dict), "cleaning_prompts should be a dictionary"
    assert (
        "clean_transcript" in cleaning_prompts
    ), "clean_transcript key should be present in cleaning_prompts"
    assert isinstance(
        cleaning_prompts["clean_transcript"], str
    ), "clean_transcript value should be a string"


def test_cleaning_prompt_content():
    """
    Test to ensure the content of the clean_transcript prompt contains essential placeholders.
    """
    prompt = cleaning_prompts["clean_transcript"]
    assert (
        "{transcript}" in prompt
    ), "clean_transcript prompt should contain the {transcript} placeholder"
