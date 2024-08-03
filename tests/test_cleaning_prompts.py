import pytest
from modules.prompts.cleaning_prompts import cleaning_prompts


def test_cleaning_prompts_structure():
    # Ensure the 'cleaning_prompts' dictionary is defined correctly
    assert isinstance(cleaning_prompts, dict), "cleaning_prompts should be a dictionary"
    assert (
        "clean_transcript" in cleaning_prompts
    ), "'clean_transcript' key is missing in cleaning_prompts"


def test_clean_transcript_prompt():
    # Test that the 'clean_transcript' prompt is formatted correctly
    transcript_sample = "This is a sample transcript with errors and filler words."
    expected_prompt = """
You will act as an expert in Natural Language Processing (NLP) to help clean transcripts of recorded EMS incidents. The goal is to remove all 
transcription errors and unnecessary parts while ensuring that the shortest possible transcript still contains all essential medical and EMS 
incident information. 

Your task includes:
1. Removing filler words, false starts, irrelevant conversations, background noise transcriptions, and repeating words or phrases.
8. Comparing the cleaned transcript with the original version to ensure no important information has been left out.

When you provide your response only provide the cleaned transcript and nothing more. Do not summarize. 

Here is the transcript for you to clean:
This is a sample transcript with errors and filler words.
    """.strip()

    actual_prompt = (
        cleaning_prompts["clean_transcript"]
        .strip()
        .format(transcript=transcript_sample)
        .strip()
    )
    assert (
        actual_prompt == expected_prompt
    ), "The formatted 'clean_transcript' prompt does not match the expected output"


if __name__ == "__main__":
    pytest.main()
