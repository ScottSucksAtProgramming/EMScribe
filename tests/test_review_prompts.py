import pytest

from modules.prompts.review_prompts import review_prompts


@pytest.fixture(name="review_prompt_keys")
def fixture_review_prompt_keys():
    return [
        "review_section",
        "final_review",
    ]


def test_review_prompts_structure(review_prompt_keys):
    for key in review_prompt_keys:
        assert key in review_prompts
        assert "prompt" in review_prompts[key]
        assert (
            "{section_data}" in review_prompts[key]["prompt"]
            or "{updated_section}" in review_prompts[key]["prompt"]
        )
        assert (
            "{user_input}" in review_prompts[key]["prompt"]
            or "{updated_section}" in review_prompts[key]["prompt"]
        )


def test_no_extra_keys_in_review_prompts(review_prompt_keys):
    assert set(review_prompts.keys()) == set(review_prompt_keys)
