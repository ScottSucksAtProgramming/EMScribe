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
    }
}
