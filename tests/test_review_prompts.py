import pytest
from modules.prompts.review_prompts import review_prompts


def test_review_prompts_structure():
    # Ensure the 'review_prompts' dictionary is defined correctly
    assert isinstance(review_prompts, dict), "review_prompts should be a dictionary"
    required_keys = [
        "review_section",
        "final_review",
    ]
    for key in required_keys:
        assert key in review_prompts, f"'{key}' key is missing in review_prompts"


def test_review_section_prompt():
    # Test that the 'review_section' prompt is formatted correctly
    section_data_sample = "Sample section data"
    user_input_sample = "Sample user input"
    expected_prompt = (
        "Here is a section of data: Sample section data\n"
        "Please make the following changes: Sample user input"
        "Do not add any additional details. Use plain text format."
    )

    actual_prompt = review_prompts["review_section"].format(
        section_data=section_data_sample, user_input=user_input_sample
    )
    assert (
        actual_prompt == expected_prompt
    ), "The formatted 'review_section' prompt does not match the expected output"


def test_final_review_prompt():
    # Test that the 'final_review' prompt is formatted correctly
    updated_section_sample = "Sample updated section"
    expected_prompt = (
        "Here is the updated section after making changes: Sample updated section. "
        "If everything is correct, type 'done'. Otherwise, provide further modifications."
    )

    actual_prompt = review_prompts["final_review"].format(
        updated_section=updated_section_sample
    )
    assert (
        actual_prompt == expected_prompt
    ), "The formatted 'final_review' prompt does not match the expected output"


if __name__ == "__main__":
    pytest.main()
