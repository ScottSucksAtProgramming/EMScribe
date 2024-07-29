narrative_prompts = {
    "presoaped_format": {
        "prearrival": """
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
            ({data})
            """,
        "subjective": """
            You will be generating the second section of an EMS narrative from provided data. This section is called the Subjective and it contains information about the patient's initial situation during a medical emergency.
            
            Subjective
            This section should include:
                - Information about the patient including their first name, age, and sex.
                - The initial impression or condition of the patient when the crew first encounters them. 
                - The location and position the patient is found.
                - If the patient has any medical equipment attached to them it should be noted as well.
                - The complaint the patient has (which might be different from the dispatch complaint), or the nature of the illness / injury as described by the EMS provider if the patient (or their family)  isn't able provide the information.

            Rules for This Section
                - Do not make any assumptions.
                - Do not respond with anything except the completed section. No explanation, No notes. Just the completed Subjective.

            For example:

                SUBJECTIVE:
                John is a 78 year old male found sitting at his living room table appearing pale and sweaty, receiving oxygen through a nasal cannula from his home condenser. He complains of chest pain.

            A template for this section may look like:

                SUBJECTIVE:
                [Patient Name] is a(n) [Age and Unit] old [Sex] found [how the patient was found]. [Medical Equipment in use by the patient]. He/She complains of [Patient's Complaint].

            Use the following data:
            ({data})""",
        "history_of_present_illness": """
            You will be generating the History of Present Illness subsection for an EMS narrative from provided data. This section contains information about story and events leading up to the patient's current illness.
            
            History of Present Illness Subsection
            This subsection must include:
                - The story of events which lead to the call for emergency medical services. This may be provided by the patient themselves, by bystanders or other first responders on scene, by witnesses or family, surmised or assumed by the responding EMS provider themselves. For transfer from one medical care center to another, (i.e. doctor's office to hospital, hospital to hospital) this information may also be obtained from medical staff, or patient documents.
                - This section should start with an overview of the patient's pertinent medical history summed up in a single sentence.
                - It may then continue to tell the patient's story. The treatments provided to the patient prior to ems arrival.
                - The length time the situation has been going on for.
                - The suspected conditions.
                - As well as any further information that can be gathered from the patient or another third party. 
                - This section is one of the most important and should be accurate. It should only contain information provided and no assumptions or inferences made by the EMS provider themselves.
                - Any direct quotes should be inside of quotation marks and given attribution to where they came from.
                - Other information in this section can vary from patient to patient as necessary but a common acronym to ensure a complete picture is presented in the narrative is OPQRSTI. 
                    - Onset: Whether the illness began suddenly, or if it has come on gradually.
                    - Provocation and Palliation: Anything which makes the condition worse, or better 
                    - Quality: When applicable, how the patient would describe what they are feeling.
                    - Radiation: Generally used for pain, but can be appropriate else where, if the symptoms start in one area and have radiated or moved to another area (such as chest pain which radiations to the left neck or left arm).
                    - Severity: How severe the illnesses is for the patient. This will often be provided on a scale from 1 to 10,  but there are numerous other ways this can be described as well.
                    - Time: How long this illness or issue has been going on for.
                    - Interventions: Any treatments or attempts by the patient to relieve the illness including previous medical visits.
                - This section should end with a sentence explaining if the patient has consented to treatment or transfer, or if they are unable to consent due to their illness, being a minor, or other conditions which prevent the patient from making clear decisions.


            Rules for this Section
                - Do not make any assumptions or inferences. Stick to documenting only the information is provided. If you are unsure, ask the user for additional information or how they would like the information they provided to be written out.
                - Do not respond with anything except the completed section. No explanation, No notes. Just the completed History of Present Illness subjection.
                - If the information is completely missing just respond with the -History of Present Illness- subheading.

            For Example:
                -History of Present Illness-
                John has a known medical history of hypertension, hyperlipidemia, heart attack (2007) with two cardiac stents placed, and diabetes. He states that he often has chest pain which is relieved with his prescribed nitroglycerin. 

                Today he has taken two nitro and the pain has not gone away. He states the pain started suddenly while he was sitting down watching television. It feels similar to the chest pain he experienced during his heart attack. He rates the pain currently as a constant 8/10 that feels like there is hand squeezing his heart. The pain radiates down his left arm and he has been profusely sweating. It started about 30 minutes prior to EMS arrival. 

            A template for this section may look like:

                -History of Present Illness-

                    All of the above information written clearly and succinctly in paragraph format. 

                    It is difficult to write a more specific template because this section will be different for most patients.

                    Consider following the following flow: The description and story of their illness up to the 911 call. Including the reason for the 911 call if the symptoms have been. Followed by information related to the OPQRST acronym. And end with the patient's consent, or refusal to be transported to the hospital.
            Use the following data:
            ({data})""",
        "patient_histories": """
            You will be generating the Patient Histories subsection for an EMS narrative from provided data. This section contains a bulleted list of the patient's medical history, surgical history, social history, family history, sexual history, prescribed medications and allergies.

            Patient Histories Sub-Section
                As opposed to the brief pertinent history given in the previous section this section lists out the patients full history. It must include the following if they are available:
                    - The patient's Medical History
                    - The patient's Surgical History
                    - The patient's Social History, 
                    - The patient's Family History 
                    - The patient's Sexual history (rarely provided)
                    - The patient's Medications and Allergies.

                Rules for this Section
                    - These must not be be formatted in to paragraphs, they must be listed out under each category. If no related information provided the section can be omitted from the narrative.
                    - NEVER make any assumptions or inferences. Stick to documenting only the information is provided. If you are unsure, ask the user for additional information or how they would like the information they provided to be written out.
                    - The subheading for this section should ALWAYS be -Patient Histories-. Provide the response in plain text.
                    - Never add any additional information, explanation or commentaries. Just give the completed Patient Histories Section.

                For Example:

                    -Patient Histories-
                    - Medical History: hypertension, hyperlipidemia, heart attack with stents, diabetes, chronic kidney disease, sleep apnea, depression, obesity, gastro-esophageal reflux disease
                    - Surgical History: Left knee replacement (2012), right shoulder surgery (1998)
                    - Social History: Former Smoker. Drinks socially. Denies recreational drug use.
                    - Family History: Father- deceased due to stroke. Mother- Deceased from heart attack.
                    - Medications: Labetalol, Cardizem, Tylenol, atorvastatin, nitroglycerine, escitalopram
                    - Allergies: Cat and dog dander. No know drug allergies.

                A template for this section may look like
                    - Medical History: [Medical History including dates when applicable or provided, separated by commas.] 
                    - Surgical History: [Surgical Procedure including dates and locations where performed when applicable or provided, separated by commas.]
                    - Social History: [Frequency of nicotine or vaporizer use, frequency of alcohol use, frequency of any other recreational drugs, separate by commas]
                    - Family History: [Status of parents, and siblings (alive or deceased, and any notable medical history they have.]
                    - Medications: [List of the medications the patient is prescribed, separated by commas.
                    - Allergies: [List of and food, drug, or environmental allergies the patient has, separated by commas.]

                Use the following data:
                    ({data})""",
        "objective": """
                You will generate the Objective section for an EMS narrative from the provided data. 

                Patient Histories Sub-Section
                    This section provides a list of objective physical exam finding broken down by the body systems: general, skin, heent (head ears eyes nose throat), neck, cardiovascular, respiratory, abdomen, genitourinary and gastrointestinal, spine, musculoskeletal, neurological, and psychiatric.

                Rules for this Section
                - Never make assumptions or add any information that is not explicitly provided in the data.
                - If no information is provided for a specific body system omit it from the response.
                - complete sentences are not needed, just include the information in short phrases separated by commas.
                - NEVER make any assumptions or inferences.
                - The heading for this section should ALWAYS be OBJECTIVE:. Provide the response in plain text.
                - Never provide any additional information, explanation or commentaries. Just give the completed Objective section.

                Here is an example Objective for a healthy patient:

                    OBJECTIVE:
                    - GENERAL: Awake and appropriately oriented to person, place, time, and event. Well appearing with no evidence of acute distress. Dressed appropriately. Well groomed.
                    - SKIN: Pink, warm, dry, and intact without rashes or lesions. Nail beds pink with no cyanosis. General coloration is appropriate.
                    - HEENT: The head is atraumatic without tenderness, visible or palpable masses, depressions, or scarring. Pupils are round, equal, and reactive to light. No nystagmus noted. Nares are patent bilaterally.
                    - NECK: Airways are patent. The patient speaks in full sentences. No stridor. No cough. The neck is supple. The trachea is midline. No jugular venous distention is noted.
                    - CARDIOVASCULAR: The external chest is normal in appearance without signs of trauma. No implanted devices were noted. Heart rate and rhythm are regular. Distal pulses are strong and regular. Capillary refill is less than 2 seconds. No edema noted.
                    - RESPIRATORY: The chest wall is symmetric and without deformity. No signs of trauma. The chest wall is non-tender. No signs of respiratory distress. Lung sounds are clear in all fields bilaterally without rales, rhonchi, or wheezes. Chest expansion is adequate and equal.
                    - ABDOMEN: The abdomen is soft, symmetric, and non-tender without distention. There are no visible lesions or scars. Umbilicus is midline without herniation.
                    - GU/GI: No external masses or lesions. External genitalia is normal in appearance without lesions, swelling, masses, or tenderness.
                    - SPINE: Neck and back are without deformity, external skin changes, or signs of trauma. Bony features of the shoulders and hips are of equal height bilaterally. Posture is upright; gait is smooth and steady. No tenderness was noted on palpation of the spinous processes. Spinous processes are midline. Cervical, thoracic, and lumbar paraspinal muscles are not tender and are without spasm. Full range of motion is noted
                    - MUSCULOSKELETAL: Upper and lower extremities are atraumatic in appearance without tenderness or deformity: no swelling or erythema. Full range of motion is noted in all joints. Muscle strength is equal bilaterally. Pulses palpable. Steady gait noted.
                    - NEUROLOGICAL: The patient is awake, alert, and oriented to person, place, and time with normal speech. Motor function is normal, with equal muscle strength bilaterally in the upper and lower extremities. Sensation is intact bilaterally. Memory is normal, and the thought process is intact. No gait abnormalities are appreciated.
                    - PSYCHIATRIC: Behavior and affect are appropriate to the situation.

                Use the following data:
                ({data})""",
        "labs_and_tests": """
            Act and an expert medical scribe. From the provided data, you will generate the Lab Values and Point of Care Test Results section for an EMS narrative. 

This section contains the results of any available vital signs, laboratory values, and point-of-care tests. It gives the reader specific information on the patient which helps find a diagnosis or impression. 

Many items may be contained within this section. Here are the most common:
- Initial Vital Signs: 
	- Blood Pressure; 
	- Heart Rate, Rhythm (regular/irregular), and Strength; 
	- Respiration Rate; 
	- Pulse Oximetry (SpO2) and whether the patient is on room air or oxygen; 
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
- X-Ray Chest @ 7/24 1907: No acute cardiopulmonary pathology.
And here is a cat scan:
- CT Brain without contrast @ 8/21 0706: No intracranial hemorrhage or masses seen.

Here is an example for reference:
**DO NOT USE THESE VALUES IN ANY RESPONSE**

	-Lab Values and Point of Care Testing-
	- Vital Signs: Blood Pressure: 110/86; Heart Rate: 82 Strong Regular; Respirations: 16; SpO2: 98% (Room Air);
	- Pain: 8/10;
	- Temperature: 98.6 F;
	- BGL: 98 mg/dl;
	- eTCO2: 37 mmHg;
	- EKG: Sinus Rhythm 70-100. Occasional PVCs. ST-segment elevation in leads II, III, and aVF with reciprocal changes in leads I and aVL.
	- Metabolic: Na: 135 (N); K: 3.7 (N); Cl: 107 (H); CO2: 28 (N); BUN: 18 (N); Cr: 6.55 (H); Gluc: 140 (H); Ca: 9.7 (N); Mg: 2.1 (N); Phos: 4.3 (N);
	- CT Brain without contrast @ 8/21 0706: No intracranial hemorrhage.
	
Rules
- Use this heading: -Lab Values and Point of Care Testing-
- Skip any items if no information is provided for them.
- Never add any values that were not present in the provided data.
- Use plain text format.
- Do not provide any notes or comments about the response.

Please provide the relevant findings based on the provided information from the following information: 
({data})""",
        "assessment": """

        Act and an expert medical scribe. From the provided data, you will generate the Assessment section for an EMS narrative. 

This section contains:
- The provider's primary and secondary (if applicable) impression of the patient's illness.
- The destination the patient is being transported to.
- The transport mode (emergent/non-emergent) for the ride to the destination.
- The patient is not always transported and is sometimes left on scene after refusing care, or if they have died. This should be included here as well.

Here is an example of a patient who was transported:

	ASSESSMENT:
	John was treated and transported, non-emergent, to St. John's Hospital with a primary impression of asthma exacerbation.

Here is an example of a patient who refused care:

	ASSESSMENT:
	Susan was assessed and refused further EMS care and transport to the emergency department.

Rules
- Use this heading: ASSESSMENT:
- Never add any information that was not provided in the data
- Use plain text format.
- Do not provide any notes or comments about the response.

Please provide the relevant findings based on the provided information from the following information: 
({data})""",
        "plan": """

        Act and an expert medical scribe. From the provided data, you will generate the Plan section for an EMS narrative. 

This section contains:
- A list of treatments provided by the EMS providers to the patient.
- Medications and fluids given, procedures performed, splinting, positioning, airway management, IV or IO access, etc.
- Any treatments were considered but unable to be completed for whatever reason. The reasons should be noted. This is uncommon.
- Full treatment details, such as route, time of administration, dose, or other details, do not need to be included. This should only be a brief list.
- A note at the end stating the full treatment details are documented elsewhere.


Here is an example:

	PLAN:
	- Oxygen administration
	- IV access
	- Normal Saline Bolus
	- Aspirin was considered by not given due to patient allergies.
	- Pain medication was deferred by the patient's request.
	
	Full treatment details as documented elsewhere.
	
Here is an example of a patient who refused care:

Rules
- Use this heading: PLAN:
- Never add any information that was not provided in the data.
- Do not make assumptions. Only list treatments explicitly mentioned in the provided data.
- Use plain text format.
- Do not provide any notes or comments about the response.
- Think critically and review the provided information multiple times to ensure you find all the treatments provided to the patient.

Please provide the relevant findings based on the provided information from the following information: 
({data})"""
    }
}   
