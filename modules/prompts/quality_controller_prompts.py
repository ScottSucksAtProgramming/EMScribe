# modules/prompts/quality_controller_prompts.py

quality_controller_prompts = {
    "review_and_improve_narrative": """
        Compare the following EMS narrative with the provided transcript. Identify any discrepancies or missing information and provide an improved narrative.

        Narrative:
        {narrative}

        Transcript:
        {transcript}

        Improved Narrative:
    """,
    "check_required_information": """
        Compare the following EMS narrative with the required information list for each section based on the narrative format. Identify any missing sections or details.

        Narrative:
        {narrative}

        Required Information:
        {required_information_list}

        Missing Information:
    """
}
