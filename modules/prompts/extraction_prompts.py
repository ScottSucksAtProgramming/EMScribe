extraction_prompts = {
    "incident_info:"
    """
Extract the following EMS incident information from the provided transcript: unit or vehicle number, response mode (emergent/non-emergent), crew type (full crew/paramedic only), any delays in response, starting location, incident location, dispatch complaint, and any additional information given to the crew by dispatch. Analyze the transcript carefully to find the most accurate answers for each item. If you are uncertain about any information, mark it with a 🚩 emoji.

Present the extracted information in a clear, concise bulleted list format. If any fields lack information, write [No Info]. If there are multiple entries for the same field, prioritize the most likely correct entry and list the others as well, marking them clearly.

Here is an example result:

### Call Information

- Unit: 5-41-27
- Response Mode: Emergent
- Crew Type: Full Crew
- Delays: None
- Starting Location: Headquarters
- Incident Location: A Residence
- Dispatch Complaint: Stroke
- Additional information: Unit was told to stand-by until police arrived.

Here is the transcript: {transcript}
"""
    "patient_demographics": """
Extract the following patient information: name, date of birth, age, gender, race or ethnicity, phone number, address or facility name, room number, and next of kin or family contact information. Calculate the age if necessary. Assume the gender if not explicitly stated based on the name provided.

Present the extracted information in a concise bulleted list format. If some fields are empty, write [No Info]. If multiple entries are found for the same field, prioritize the one that is most likely correct, and list the others as well, marking them clearly.

Here is an example result:

### Patient Demographics

- Name: John Blue
- Date of Birth: June 6th, 1986
- Age: 38
- Gender: Male
- Race or Ethnicity: [No Info]
- Phone Number: (333) 462-2345
- Address or Facility Name: Stony Brook Cancer Center, Level 5, Room E2
- Next of Kin or Family Contact Information: [No Info]

Here is the transcript: {transcript}""",
    "patient_histories": """
    Extract the following medical history from the provided transcript of an EMS incident: medical history, surgical history, social history, family history, social history, patient medications, and patient allergies. Analyze the full transcript carefully to find the most accurate answers for each item. It is okay to assume medical history based on the context in the transcript or known patient medications. Translate any used medical abbreviations into the full term (HTN would become hypertension, GERD to gastro-esophageal reflux disease). If you are uncertain about any information, mark it with a 🚩 emoji.

Present the extracted information in a clear, concise, bulleted list format. If any fields lack information, write [No Info]; if there are no allergies, write 'No Known Allergies'. If there are multiple entries for the same field, list them alphabetically.

Here is an example result:

### Patient Histories

- Medical History: anxiety, coronary artery disease, hyperlipidemia, hypertension 
- Surgical History: left below knee amputation, cardiac stent placement
- Social History: fifteen year smoker, quite one year ago, social drinker
- Family History: father: alive, mother: deceased due to heart attack
- Sexual History: [No Info]
- Medications: atorvastatin, Eliquis, metoprolol
- Allergies: No Known Allergies

Here is the transcript: {}""",
    "history_of_present_illness": """Extract the subjective and history of present illness information from the provided EMS medical transcript of a patient’s visit. Your task is to identify and extract the following elements:

- Chief Complaint (CC) and its duration
- Any associated signs, symptoms or other complaints
- History of Present Illness (HPI), including details from the patient, family, or other medical providers
    - Utilize the OPQRSTI method for HPI when applicable:
    - Onset of complaint, sudden gradual episodic or other along with any related details
    - Provocation/Palliation, anything that makes the symptoms better or worse
    - Quality
    - Radiation
    - Severity
    - Time
    - Interventions or treatments attempted prior to EMS arrival

Carefully analyze the transcript to provide the most accurate and complete information for each element. Translate any medical abbreviations into their full terms (e.g., SOB to shortness of breath, CP to chest pain). If information is unclear or ambiguous, denote it with a 🚩 emoji. If any element lacks information, indicate with [No Info]. If conflicting information is found, review all available context to resolve it. Present the extracted details in a clear, concise, bulleted list and include any additional context or details that might help in understanding the patient’s condition.

Here is an example format for your response:

## Subjective

- Chief Complaint: Chest pain for the past hour
- Associated signs and Symptoms: shortness of breath, sweating, dizziness

### History of Present Illness:
- Onset: Sudden onset while watching television
- Provocation/Palliation: worse with activity, better when lying down and after taking prescribed nitroglycerine
- Quality: crushing
- Radiation: to the left arm, neck, and jaw
- Severity: 8/10
- Time: starting twenty minutes ago
- Interventions: patient took his prescrbed nitroglycerine
- Additional Context: [No Info]

Here is the transcript: {transcript}""",
    "Treatments Done": "List the treatments done by the sending facility or interventions the patient completed on his own: {transcript}",
    "Objective Assessment": "Provide an objective assessment of the patient by body system: {transcript}",
    "Treatment Plan": "Outline the treatment plan provided to the patient by the EMS crew: {transcript}",
    "Transport Information": "Detail how the patient was transported: {transcript}",
    "Transfer of Care": "Provide information about the transfer of care: {transcript}",
}
