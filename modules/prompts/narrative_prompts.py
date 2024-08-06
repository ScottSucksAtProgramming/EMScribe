narrative_prompts = {
    "presoaped_format": {
        "prearrival": """
        Act as an expert medical scribe. You will be generating the first section of an EMS narrative from the provided data. This section is called the Pre-Arrival and contains information about the ambulance response to an EMS incident before arriving at the scene.

        This section should include:
        - Unit identifier or ambulance number
        - Mode of transportation (emergent, non-emergent, or otherwise)
        - Location where the unit started
        - Crew type (light crew, driver only, full crew)
        - Any delays experienced during the response
        - Location of the scene
        - Dispatch complaint
        - Any additional information related to the unit's response (commonly left empty)

        Example:

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
        Unit 292 responded emergent from headquarters, with a full crew and no delay, to 123 Main Street in Levittown for a reported stroke. Prior to arrival, dispatch notified the unit to stand by until police arrived.

        Template:
        PRE-ARRIVAL:
        Unit [unit] responded [response_mode] from [starting_location], with a [crew_type] and [delays], to [incident_location] for a [dispatch_complaint]. [additional_information].

        Rules:
        - Use the heading 'PRE-ARRIVAL:'
        - Do not make any assumptions.
        - Ensure all information is factual and based on the pre-arrival scene without assumptions.
        - Respond only with the completed section. No explanation or notes.

        Use the following data:
        ({data})
        """,
        "subjective": """
        You will be generating the second section of an EMS narrative from the provided data. This section is called the Subjective and contains information about the patient's initial situation during a medical emergency.

        This section should include:
        - Patient's first name, age, and sex
        - Initial impression or condition of the patient when first encountered
        - Location and position the patient is found
        - Any medical equipment attached to the patient
        - Patient's complaint or nature of the illness/injury as described by the EMS provider

        Example:

        SUBJECTIVE:
        John is a 78-year-old male found sitting at his living room table appearing pale and sweaty, receiving oxygen through a nasal cannula from his home condenser. He complains of chest pain.

        Template:
        SUBJECTIVE:
        [Patient Name] is a(n) [Age and Unit] old [Sex] found [how the patient was found]. [Medical Equipment in use by the patient]. He/She complains of [Patient's Complaint].

        Rules:
        - Do not make any assumptions.
        - Respond only with the completed section. No explanation or notes.

        Use the following data:
        ({data})
        """,
        "history_of_present_illness": """
        You will be generating the History of Present Illness subsection for an EMS narrative from the provided data. This section contains information about the story and events leading up to the patient's current illness.

        This subsection must include:
        - The story of events leading to the call for emergency medical services
        - An overview of the patient's pertinent medical history
        - Treatments provided to the patient prior to EMS arrival
        - The length of time the situation has been ongoing
        - Suspected conditions
        - Any further information from the patient or another third party
        - The OPQRSTI acronym (Onset, Provocation, Palliation, Quality, Radiation, Severity, Time, Interventions)
        - Patient consent to treatment or transfer

        Example:

        -History of Present Illness-
        John has a known medical history of hypertension, hyperlipidemia, heart attack (2007) with two cardiac stents placed, and diabetes. He states that he often has chest pain which is relieved with his prescribed nitroglycerin. Today he has taken two nitro and the pain has not gone away. He states the pain started suddenly while he was sitting down watching television. It feels similar to the chest pain he experienced during his heart attack. He rates the pain currently as a constant 8/10 that feels like there is a hand squeezing his heart. The pain radiates down his left arm and he has been profusely sweating. It started about 30 minutes prior to EMS arrival.

        Rules:
        - Do not make any assumptions or inferences. Stick to the provided information.
        - Respond only with the completed section. No explanation or notes.
        - If the information is missing, respond with the -History of Present Illness- subheading.

        Use the following data:
        ({data})
        """,
        "patient_histories": """
        You will be generating the Patient Histories subsection for an EMS narrative from the provided data. This section contains a bulleted list of the patient's medical history, surgical history, social history, family history, sexual history, prescribed medications, and allergies.

        Patient Histories Subsection:
        - Medical History
        - Surgical History
        - Social History
        - Family History
        - Sexual History
        - Medications
        - Allergies

        Example:

        -Patient Histories-
        - Medical History: hypertension, hyperlipidemia, heart attack with stents, diabetes, chronic kidney disease, sleep apnea, depression, obesity, gastro-esophageal reflux disease
        - Surgical History: Left knee replacement (2012), right shoulder surgery (1998)
        - Social History: Former Smoker. Drinks socially. Denies recreational drug use.
        - Family History: Father- deceased due to stroke. Mother- Deceased from heart attack.
        - Medications: Labetalol, Cardizem, Tylenol, atorvastatin, nitroglycerine, escitalopram
        - Allergies: Cat and dog dander. No known drug allergies.

        Rules:
        - Use the heading 'Patient Histories'
        - List information under each category. If no related information is provided, omit the section.
        - Do not make any assumptions or inferences. Stick to the provided information.
        - Respond only with the completed section. No explanation or notes.

        Use the following data:
        ({data})
        """,
        "objective_1": """
        You will generate the Objective section for an EMS narrative from the provided data. This section provides a list of objective physical exam findings broken down by body systems: general, skin, HEENT (head, ears, eyes, nose, throat), neck, cardiovascular, respiratory, abdomen, genitourinary, gastrointestinal, spine, musculoskeletal, neurological, and psychiatric.

        Example:

        OBJECTIVE:
        - GENERAL: Awake and oriented to person, place, time, and event. Well-appearing with no acute distress. Dressed appropriately. Well-groomed.
        - SKIN: Pink, warm, dry, and intact without rashes or lesions. Nail beds pink with no cyanosis.
        - HEENT: The head is atraumatic without tenderness, visible or palpable masses, depressions, or scarring. Pupils are round, equal, and reactive to light. No nystagmus noted. Nares are patent bilaterally.
        - NECK: Airways are patent. The patient speaks in full sentences. No stridor. No cough. The neck is supple. The trachea is midline. No jugular venous distention is noted.
        - CARDIOVASCULAR: Heart rate and rhythm are regular. Distal pulses are strong and regular. Capillary refill is less than 2 seconds. No edema noted.
        - RESPIRATORY: Lung sounds are clear in all fields bilaterally without rales, rhonchi, or wheezes. Chest expansion is adequate and equal.
        - ABDOMEN: Soft, symmetric, and non-tender without distention. No visible lesions or scars.
        - GU/GI: No external masses or lesions. External genitalia normal in appearance without lesions, swelling, masses, or tenderness.
        - SPINE: Neck and back are without deformity, external skin changes, or signs of trauma. Bony features are of equal height bilaterally. Posture is upright; gait is smooth and steady. No tenderness on palpation of the spinous processes. Spinous processes are midline. Cervical, thoracic, and lumbar paraspinal muscles are not tender and are without spasm. Full range of motion noted.
        - MUSCULOSKELETAL: Upper and lower extremities are atraumatic in appearance without tenderness or deformity. No swelling or erythema. Full range of motion noted in all joints. Muscle strength is equal bilaterally. Pulses palpable. Steady gait noted.
        - NEUROLOGICAL: Awake, alert, and oriented to person, place, and time with normal speech. Motor function normal, with equal muscle strength bilaterally in the upper and lower extremities. Sensation intact bilaterally. Memory normal, thought process intact. No gait abnormalities appreciated.
        - PSYCHIATRIC: Behavior and affect appropriate to the situation.

        Rules:
        - Use the heading 'OBJECTIVE:'
        - Do not make any assumptions or add any information not provided.
        - If no information is provided for a specific body system, omit it.
        - Use short phrases separated by commas. Complete sentences are not needed.
        - Respond only with the completed section. No explanation or notes.
            Use the following data:
    ({data})
    """,
        "labs_and_tests": """
    Act as an expert medical scribe. From the provided data, generate the Lab Values and Point of Care Test Results section for an EMS narrative.

    This section should include results of any available vital signs, laboratory values, and point-of-care tests. It gives specific information on the patient to help find a diagnosis or impression.

    Example:

    -Lab Values and Point of Care Testing-
    - Vital Signs: Blood Pressure: 110/86; Heart Rate: 82 Strong Regular; Respirations: 16; SpO2: 98% (Room Air);
    - Pain: 8/10;
    - Temperature: 98.6 F;
    - BGL: 98 mg/dl;
    - eTCO2: 37 mmHg;
    - EKG: Sinus Rhythm 70-100. Occasional PVCs. ST-segment elevation in leads II, III, and aVF with reciprocal changes in leads I and aVL.
    - Metabolic: Na: 135 (N); K: 3.7 (N); Cl: 107 (H); CO2: 28 (N); BUN: 18 (N); Cr: 6.55 (H); Gluc: 140 (H); Ca: 9.7 (N); Mg: 2.1 (N); Phos: 4.3 (N);
    - CT Brain without contrast @ 8/21 0706: No intracranial hemorrhage.

    Rules:
    - Use the heading '-Lab Values and Point of Care Testing-'
    - Skip any items if no information is provided for them.
    - Do not add any values not present in the provided data.
    - Use plain text format.
    - Respond only with the completed section. No explanation or notes.

    Use the following data:
    ({data})
    """,
        "assessment": """
    Act as an expert medical scribe. From the provided data, generate the Assessment section for an EMS narrative.

    This section should include:
    - Provider's primary and secondary (if applicable) impression of the patient's illness
    - Destination the patient is being transported to
    - Transport mode (emergent/non-emergent) for the ride to the destination
    - Note if the patient refused care or was not transported

    Example:

    ASSESSMENT:
    John was treated and transported, non-emergent, to St. John's Hospital with a primary impression of asthma exacerbation.

    Example for refusal of care:

    ASSESSMENT:
    Susan was assessed and refused further EMS care and transport to the emergency department.

    Rules:
    - Use the heading 'ASSESSMENT:'
    - Do not add any information not provided.
    - Use plain text format.
    - Respond only with the completed section. No explanation or notes.

    Use the following data:
    ({data})
    """,
        "plan": """
    Act as an expert medical scribe. From the provided data, generate the Plan section for an EMS narrative.

    This section should include:
    - List of treatments provided by the EMS providers to the patient
    - Medications and fluids given, procedures performed, splinting, positioning, airway management, IV or IO access, etc.
    - Treatments considered but unable to be completed (uncommon)
    - A note stating the full treatment details are documented elsewhere

    Example:

    PLAN:
    - Oxygen administration
    - IV access
    - Normal Saline Bolus
    - Aspirin was considered but not given due to patient allergies
    - Pain medication deferred at the patient's request

    Full treatment details are documented elsewhere.

    Rules:
    - Use the heading 'PLAN:'
    - Do not add any information not provided.
    - Do not make assumptions.
    - Use plain text format.
    - Respond only with the completed section. No explanation or notes.

    Use the following data:
    ({data})
    """,
        "delta": """
    Act as an expert medical scribe. From the provided data, generate the Delta section of an EMS narrative. Delta stands for change and discusses the rest of the emergency call.

    This section should include:
    - How the patient was moved and secured to the ambulance stretcher
    - Monitoring equipment used
    - Any delays on scene
    - Notifications made to the hospital
    - Changes to the patient's clinical status, including responses to treatments, new complaints, worsening symptoms, or new findings during transport
    - Changes to the transport

    Example:

    DELTA:
    Following assessment and 12-lead EKG, John was given aspirin, and an IV was established with fluids started. John was given fentanyl for his pain, reducing it from an 8/10 to a 4/10. He also stated relief from nausea. John was transferred to the transport stretcher via pull-sheet and secured with three straps. Transport was begun without delay. John's wife, Abagail, accompanied him during transport in the patient compartment, secured to the bench seat with a harness.

    A notification was given to St. Michael's Hospital with a request to activate the cath lab team. During transport, John's clinical status remained unchanged. His pain stayed around a 4/10. He denied any worsening complaints or new symptoms. Ongoing reassessments were unremarkable. Serial 12-Lead EKGs showed no changes.

    Template:

    DELTA:
    [Paragraph discussing events on the scene, including how the patient was moved to the stretcher/ambulance and secured.]

    [Paragraph discussing events during transport, including patient response to treatments, new complaints, clinical changes, and findings from further assessments or point-of-care testing.]

    Rules:
    - Use the heading 'DELTA:'
    - Do not add any information not provided.
    - Do not make assumptions.
    - Use plain text format.
    - Respond only with the completed section. No explanation or notes.

    Use the following data:
    ({data})
    """,
        "hand_off": """
    Act as an expert medical scribe. From the provided data, generate the Hand Off subsection of an EMS narrative.

    This section should include:
    - Who the hand-off report was given to, including their license
    - Specific location the patient was transported to
    - How the patient was transferred into their bed or chair
    - Any safety measures taken
    - Any delays in transferring care
    - Actions the crew took following transfer of care

    Example:

    -Hand Off-
    Upon arrival at St. Michael's Hospital, a full report and paperwork were given to Ratchett, RN. The patient was moved into the resuscitation room where the report was also given to the emergency physician and cath lab team, with all questions answered. Transfer of care was completed, and the patient-care report was signed by the nurse.

    John was transferred to the emergency department stretcher via pull-sheet and left in the bed with wheels locked, rails up, in staff presence, and with all therapies continued. John's belongings were given to his wife.

    The unit was cleaned, restocked, and returned to service.

    Template:

    -Hand Off-
    [Paragraph discussing the transfer of care.]

    [Paragraph discussing where the patient was left.]

    [Paragraph discussing any actions taken after the transfer of care.]

    Rules:
    - Use the heading '-Hand Off-'
    - Do not add any information not provided.
    - Do not make assumptions.
    - Use plain text format.
    - Respond only with the completed section. No explanation or notes.

    Use the following data:
    ({data})
    """,
    }
}
