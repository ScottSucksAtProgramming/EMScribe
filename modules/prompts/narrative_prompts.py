narrative_prompts = {
    "presoaped_format": {
        "prearrival": """
            You will be generating the first section of an EMS narrative from provided data. This section is called the Pre-Arrival and it contains information about the ambulance response to an EMS incident before it arrives at the scene of the emergency.

            This section should include:
            - The Unit's identifier or ambulance number.
            - The mode of transportation- emergent, non-emergent, or otherwise.
            - The location where the unit started.
            - The Crew Type- light crew, driver only, full crew.
            - Any delays experienced during the response to the scene.
            - The location of the scene.
            - The dispatch complaint.
            - The Pre-Arrival section should also include any additional information which s provided that occurred before the unit got to the emergency scene. This can include but is not limited to a change in response mode, change in location or patient status, updated information about the location the unit is responding to, and other information provided to the crew.

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
                - Ensure all information is factual and based on the pre-arrival scene without assumptions.

            Use the following data:
            {data}
            """,
        "subjective": 
            """
            You will be generating the second section of an EMS narrative from provided data. This section is called the Subjective and it contains information about the patient's initial situation during a medical emergency.
            
            Subjective
            This section should include:
                - Information about the patient including their first name, age, and sex.
                - The initial impression or condition of the patient when the crew first encounters them. 
                - The location and position the patient is found.
                - If the patient has any medical equipment attached to them it should be noted as well.
                - The complaint the patient has (which might be different from the dispatch complaint), or the nature of the illness / injury as described by the EMS provider if the patient (or their family)  isn't able provide the information.

            Rules for This Section
                - If patient details are incomplete, ask the user to provide the missing information, such as age or specific complaint.

            For example:

                SUBJECTIVE:
                John is a 78 year old male found sitting at his living room table appearing pale and sweaty, receiving oxygen through a nasal cannula from his home condenser. He complains of chest pain.

            A template for this section may look like:

                SUBJECTIVE:
                [Patient Name] is a(n) [Age and Unit] old [Sex] found [how the patient was found]. [Medical Equipment in use by the patient]. He/She complains of [Patient's Complaint].

            Use the following data:
            {data}""",
    }
}   
