import pytest
from modules.prompt_manager import PromptManager


@pytest.fixture(name="sample_prompts")
def fixture_sample_prompts():
    return {
        "extraction_prompt": "Extract data for {field}",
        "cleaning_prompt": "Clean data in {format} format",
        "narrative_prompt": "Generate a narrative for {event}",
        "review_prompt": "Review the following: {content}",
        "multi_sub_prompt": "This is a {adjective} test for {field} with multiple {sub}.",
        "no_sub_prompt": "This prompt requires no substitutions.",
    }


@pytest.fixture(name="prompt_manager")
def fixture_prompt_manager(sample_prompts):
    return PromptManager(prompts=sample_prompts)


def test_get_prompt_existing_key(prompt_manager):
    result = prompt_manager.get_prompt("extraction_prompt", field="name")
    assert result == "Extract data for name"


def test_get_prompt_nonexistent_key(prompt_manager):
    with pytest.raises(KeyError):
        prompt_manager.get_prompt("nonexistent_key")


def test_get_prompt_with_long_prompt(prompt_manager):
    long_prompt = "A" * 35000
    prompt_manager.prompts["long_prompt"] = long_prompt
    result = prompt_manager.get_prompt("long_prompt")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == "A" * 32000
    assert result[1] == "A" * 3000


def test_get_prompt_with_dict(prompt_manager):
    prompt_manager.prompts["dict_prompt"] = {
        "part1": "Part 1 for {field}",
        "part2": "Part 2 for {field}",
    }
    result = prompt_manager.get_prompt("dict_prompt", field="test")
    assert result == {
        "part1": "Part 1 for test",
        "part2": "Part 2 for test",
    }


def test_multi_substitution_prompt(prompt_manager):
    result = prompt_manager.get_prompt(
        "multi_sub_prompt", adjective="simple", field="test", sub="substitutions"
    )
    assert result == "This is a simple test for test with multiple substitutions."


def test_no_substitution_prompt(prompt_manager):
    result = prompt_manager.get_prompt("no_sub_prompt")
    assert result == "This prompt requires no substitutions."


def test_prompt_with_missing_placeholder(prompt_manager):
    with pytest.raises(KeyError):
        prompt_manager.get_prompt("multi_sub_prompt", adjective="simple", field="test")


def test_prompt_with_incorrect_placeholder(prompt_manager):
    with pytest.raises(KeyError):
        prompt_manager.get_prompt("extraction_prompt", wrong_key="value")
