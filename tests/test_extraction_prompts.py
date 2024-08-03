import pytest
from modules.prompts.extraction_prompts import extraction_prompts


def test_extraction_prompts_structure():
    # Ensure the 'extraction_prompts' dictionary is defined correctly
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
        ), f"'{key}' key is missing in extraction_prompts"


def test_incident_info_prompt():
    # Test that the 'incident_info' prompt is formatted correctly
    transcript_sample = "This is a sample transcript with incident information."
    expected_prompt = """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for the unit number, ambulance number or other unit identifier for the unit that is responding to the medical emergency.
2. Review the entire document looking for the response mode (emergent or non-emergent) used. 
3. Review the entire document looking for the crew type for this response (full crew, driver only, medic only, EMT only)
4. Review the entire document looking for any delays which occurred during the response.
5. Review the entire document looking for the location where the ambulance or vehicle was when they began their response.
6. Review the entire document looking for the location of the medical emergency.
7. Review the entire document looking for the medical complaint provided during dispatch, or prior to the crew meeting the patient.

Once you have obtained all the information give your response using the following template. If information is missing leave an answer of '[No Info]'.
Use Plain text. Do not add any comments or additional information.

Template

Incident Information
- Unit: 
- Response Mode: 
- Crew Type: 
- Response Delays: 
- Incident Location: 
- Dispatch Complaint: 

Example:
DO NOT USE THIS INFORMATION IN YOUR RESPONSE IT IS ONLY FOR REFERENCE
- Unit: 5-41-16
- Response Mode: non-emergent
- Crew Type: full crew
- Response Delays: none
- Incident Location: residence in new york
- Dispatch Complaint: knee pain

Here is the information: (This is a sample transcript with incident information.)""".strip()

    actual_prompt = (
        extraction_prompts["incident_info"]
        .strip()
        .format(transcript=transcript_sample)
        .strip()
    )
    assert (
        actual_prompt == expected_prompt
    ), "The formatted 'incident_info' prompt does not match the expected output"


if __name__ == "__main__":
    pytest.main()
