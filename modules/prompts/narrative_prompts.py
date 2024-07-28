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

            Rules for this section:
                - Do not make any assumptions.
                - Do not respond with anything except the completed section. No explanation, No notes. Just the completed Pre-Arrival.

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
            {data}""",
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
            {data}""",
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
            {data}"""
    }
}   
