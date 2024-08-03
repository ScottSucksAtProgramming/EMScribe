import pytest
from modules.prompts.narrative_prompts import narrative_prompts


def test_narrative_prompts_structure():
    # Ensure the 'narrative_prompts' dictionary is defined correctly
    assert isinstance(
        narrative_prompts, dict
    ), "narrative_prompts should be a dictionary"
    required_keys = [
        "presoaped_format",
    ]
    for key in required_keys:
        assert key in narrative_prompts, f"'{key}' key is missing in narrative_prompts"


def test_presoaped_format_structure():
    # Ensure the 'presoaped_format' dictionary is defined correctly
    presoaped_format = narrative_prompts["presoaped_format"]
    assert isinstance(
        presoaped_format, dict
    ), "'presoaped_format' should be a dictionary"
    required_keys = [
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
    for key in required_keys:
        assert key in presoaped_format, f"'{key}' key is missing in presoaped_format"


def test_prearrival_prompt():
    # Test that the 'prearrival' prompt is formatted correctly
    data_sample = "Sample data for prearrival"
    expected_prompt = """
            Act and an expert medical scribe. You will be generating the first section of an EMS narrative from provided data. This section is called the Pre-Arrival and it contains information about the ambulance response to an EMS incident before it arrives at the scene of the emergency.

            This section should include:
                - The Unit's identifier or ambulance number.
                - The mode of transportation- emergent, non-emergent, or otherwise.
                - The location where the unit started.
                - The Crew Type- light crew, driver only, full crew.
                - Any delays experienced during the response to the scene.
                - The location of the scene.
                - The dispatch complaint.
                - Any additional information related to the unit's response, such as other units responding, change in response mode, pre-arrival instructions. This section is commonly left empty.

            For Example:

                If this information is provided:

                    - Unit: 292
                    - Response Mode: Emergent
                    - Crew Type: Full Crew
                    - Delays: None
                    - Starting Location: Headquarters
                    - Incident Location: 123 Main Street in Levittown
                    - Dispatch Complaint: Stroke
                    - Additional information: The unit was told by dispatch to stand by until police arrived.

                The Pre-Arrival section might look like this:

                    PRE-ARRIVAL:
                    Unit 292 responded emergent from headquarters, with a full crew and no delay, to 123 Main Street in Levittown for a reported chest pain. Prior to arrival, dispatch notified the unit to stand by until police arrived.

            Pre-Arrival Template:

            PRE-ARRIVAL:
            Unit [unit] responded [response_mode] from [starting_location], with a [crew_type] and [delays], to [incident_location] for a [dispatch_complaint]. [additional_information].

            Rules for This Section
                - Use the heading 'PRE-ARRIVAL:'
                - Do not make any assumptions.
                - Ensure all information is factual and based on the pre-arrival scene without assumptions.
                - Do not respond with anything except the completed section. No explanation, No notes. Just the completed Pre-Arrival.

            Use the following data:
            (Sample data for prearrival)
            """.strip()

    actual_prompt = (
        narrative_prompts["presoaped_format"]["prearrival"]
        .strip()
        .format(data=data_sample)
        .strip()
    )
    assert (
        actual_prompt == expected_prompt
    ), "The formatted 'prearrival' prompt does not match the expected output"


if __name__ == "__main__":
    pytest.main()
