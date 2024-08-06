import pytest
from modules.prompts.extraction_prompts import extraction_prompts


def test_extraction_prompts_structure():
    """
    Test to ensure the structure of extraction_prompts dictionary is correct.
    """
    assert isinstance(
        extraction_prompts, dict
    ), "extraction_prompts should be a dictionary"

    required_keys = [
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

    for key in required_keys:
        assert (
            key in extraction_prompts
        ), f"{key} key should be present in extraction_prompts"
        assert isinstance(
            extraction_prompts[key], str
        ), f"{key} value should be a string"


def test_extraction_prompts_content():
    """
    Test to ensure the content of each prompt contains essential placeholders.
    """
    for key, prompt in extraction_prompts.items():
        assert (
            "{transcript}" in prompt
        ), f"{key} prompt should contain the {{transcript}} placeholder"


# Additional tests to verify prompt formatting can be added here
