import pytest
from modules.prompts.narrative_prompts import narrative_prompts


@pytest.fixture(name="narrative_keys")
def fixture_narrative_keys():
    return [
        "prearrival",
        "subjective",
        "history_of_present_illness",
        "patient_histories",
        "objective_1",
        "labs_and_tests",
        "assessment",
        "plan",
        "delta",
        "hand_off",
    ]


def test_narrative_prompts_structure(narrative_keys):
    assert "presoaped_format" in narrative_prompts
    presoaped_format_keys = narrative_prompts["presoaped_format"].keys()
    for key in narrative_keys:
        assert key in presoaped_format_keys


def test_narrative_prompts_content(narrative_keys):
    for key in narrative_keys:
        assert "{data}" in narrative_prompts["presoaped_format"][key]


def test_narrative_prompts_no_extra_keys(narrative_keys):
    presoaped_format_keys = set(narrative_prompts["presoaped_format"].keys())
    expected_keys = set(narrative_keys)
    assert presoaped_format_keys == expected_keys
