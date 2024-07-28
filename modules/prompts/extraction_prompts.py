extraction_prompts = {
    "incident_info":"""
        Extract the following EMS incident information from the provided transcript: unit or vehicle number, response mode (emergent/non-emergent), crew type (full crew/paramedic only), any delays in response, starting location, incident location, dispatch complaint, and any additional information given to the crew by dispatch. Analyze the transcript carefully to find the most accurate answers for each item. If you are uncertain about any information, mark it with a 🚩 emoji.

        Present the extracted information in a clear, concise bulleted list format. If any fields lack information, write [No Info]. If there are multiple entries for the same field, prioritize the most likely correct entry and list the others as well, marking them clearly. Never make assumptions or add information this is not explicitly available in the transcript.

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

        Here is the transcript: {transcript}""",
    "patient_demographics": """
        Extract the following patient information: name, date of birth, age, gender, race or ethnicity, phone number, address or facility name, room number, and next of kin or family contact information. Calculate the age if necessary. Assume the gender if not explicitly stated based on the name provided.

        Present the extracted information in a concise bulleted list format. If some fields are empty, write [No Info]. If multiple entries are found for the same field, prioritize the one that is most likely correct, and list the others as well, marking them clearly. Never make assumptions or add information this is not explicitly available in the transcript.

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
    Extract the following medical history from the provided transcript of an EMS incident: medical history, surgical history, social history, family history, social history, patient medications, and patient allergies. Analyze the full transcript carefully to find the most accurate answers for each item. Never make assumptions or add information this is not explicitly available in the transcript. Translate any used medical abbreviations into the full term (HTN would become hypertension, GERD to gastro-esophageal reflux disease). If you are uncertain about any information, mark it with a 🚩 emoji.

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

        Here is the transcript: {transcript}""",
    "history_of_present_illness": """
        Extract the subjective and history of present illness information from the provided EMS medical transcript of a patient’s visit. Never make assumptions or add information this is not explicitly available in the transcript. Your task is to identify and extract the following elements:

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
    "objective": """
        You are an AI Agent tasked with extracting physical exam and objective assessment findings for EMS incidents from the provided information. You must critically review the information multiple times to ensure accuracy. Please use the following template to provide your response:

        OBJECTIVE:
        - GENERAL: [exam findings for the general body system]
        - SKIN: [exam findings for the skin body system]
        - HEENT: [exam findings for the head, ears, eyes, nose and throat]
        - NECK: [exam findings for the neck and airways]
        - CARDIOVASCULAR: [exam findings for the cardiovascular body system]
        - RESPIRATORY: [exam findings for the respiratory or pulmonary body system]
        - ABDOMEN: [exam findings for that patient's abdomen]
        - GU/GI: [exam findings for the genitourinary body system and the gastrointestinal body system]
        - SPINE: [exam findings for the patient's spine]
        - MUSCULOSKELETAL: [exam findings for the musculoskeletal body system including the extremities]
        - NEUROLOGICAL: [exam findings for the neurological body system]
        - PSYCHIATRIC: [exam findings for the psychiatric or behavioral body system]

        Rules:
        - Never make any assumptions or add any information not explicitly provided.
        - Only include the sections for body systems related to the patient's complaint or illness. Additional information is okay if it is included in the provided info; otherwise, the section can be omitted from the response.
        - Complete sentences are not required, short phrases with the appropriate information is okay.
        - Do not give any explanations or any other comments / information except for the completed section.

        Please provide the relevant findings based on the provided information from the following information: 
        {transcript}
    """,
    "labs_and_tests": """
         From the provided data, you will generate the Lab Values and Point of Care Test Results section for an EMS narrative. 

Lab Values Sub-Section
This section contains the results of any available vital signs, laboratory values, and point-of-care tests. It gives the reader specific information on the patient which helps find a diagnosis or impression. 

There are many items that may be contained within this section. Here are the most common:
- Initial Vital Signs: Blood Pressure, Heart Rate, Rhythm (regular/irregular), and Strength; Respiration Rate; Pulse Oximetry (SpO2) and whether the patient is on room air or oxygen;
- Pain Score out of 10.

Point-of-care test results may also be included. These are specific to each patient and will change frequently. Here are some common ones:
- Temperature
- Blood Glucose Level (BGL)
- EKG Interpretation: includes the rhythm, rate range, ectopy, and other important findings.
- End Tidal CO2 measurement (EtCO2)
- Cincinnati Stroke Exam
- LA Motor Score (LAMS)
- NIH Store Score (NIH/NIHSS)

Laboratory and blood work panels may also be included. Each panel should be on its own line containing the panel name, the individual tests, their values, and whether they fall in the normal range. For example here is a metabolic panel.
Metabolic - Na: 135 (N); K: 8.2 (H); Cl: 107 (H); CO2: 28 (N); BUN: 18 (N); Cr: 6.55 (H); Gluc: 34 (L); 9.7 (N); Mg: 2.1 (N); 4.3 (N)

Finally any imaging that was done on the patient should be included. Each imaging exam should be on it's own line with it's name, the date and or time it was performed, and it's impression. For example here is a normal chest x-ray:
X-Ray Chest @ 7/24 1907: No acute cardiopulmonary pathology.
And here is a cat scan:
CT Brain without contrast @ 8/21 0706: No intracranial hemorrhage or masses seen.


Rules
- Skip any tests not included in the provided data.
- Use plain text format.
- Use this heading: -Lab Values and Point of Care Testing-
- No not provide any notes or comments about the response.

Here is an example for reference.
	-Lab Values and Point of Care Testing-
	- Vital Signs - Blood Pressure: 110/86; Heart Rate: 82 Strong Regular; Respirations: 16; SpO2: 98% (Room Air);
	- Pain: 8/10;
	- BGL: 98 mg/dl;
	- eTCO2: 37 mmHg;
	- EKG: Sinus Rhythm 70-100. Occasional PVCs. ST-segment elevation in leads II, III, and aVF with reciprocal changes in leads I and aVL.
	- Metabolic: Na: 135 (N); K: 3.7 (N); Cl: 107 (H); CO2: 28 (N); BUN: 18 (N); Cr: 6.55 (H); Gluc: 140 (H); Ca: 9.7 (N); Mg: 2.1 (N); Phos: 4.3 (N);
	- Hematology: WBC: 7.6 (N); Hgb: 15 (N); Hct: 22 (L); Plat: 236 (N); Blood Type: A Pos;
	- CT Brain without contrast @ 8/21 0706: No intracranial hemorrhage.

    Please provide the relevant findings based on the provided information from the following information: 
    {transcript}
    """
    # "Treatment Plan": "Outline the treatment plan provided to the patient by the EMS crew: {transcript}",
    # "Transport Information": "Detail how the patient was transported: {transcript}",
    # "Transfer of Care": "Provide information about the transfer of care: {transcript}",
}
