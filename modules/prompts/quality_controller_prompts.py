# modules/prompts/quality_controller_prompts.py

quality_controller_prompts = {
    "compare_narrative_to_transcript": """
    Review the following narrative in the context of the provided transcript. Identify any discrepancies or missing information and return an improved narrative. Ensure the narrative is accurate and complete.

    Transcript:
    {transcript}

    Narrative:
    {narrative}

    Improved Narrative:
    """,

    "check_missing_information": """
    Compare the provided narrative against a list of required information for each section based on the narrative format. Identify any missing sections or details and return a list of the missing elements.

    Narrative:
    {narrative}

    Required Information:
    {required_info}

    Missing Elements:
    """
}
