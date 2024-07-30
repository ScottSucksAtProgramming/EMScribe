extraction_prompts = {
    "incident_info": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for the unit number, ambulance number or other unit identifier for the unit that is responding to the medical emergency.
2. Review the entire document looking for the response mode (emergent or non-emergent) used. 
3. Review the entire document looking for the crew type for this response (full crew, driver only, medic only, EMT only)
4. Review the entire document looking for any delays which occurred during the response.
5. Review the entire document looking for the location where the ambulance or vehicle was when they began their response.
6. Review the entire document looking for the location of the medical emergency.
7. Review the entire document looking for the medical complaint provided during dispatch, or prior to the crew meeting the patient.

Once you have obtained all the information give your response using the following template. If information is missing leave an answer of '[No Info]'.
Use Plain text. Do not add any comments or additional information.

Template

Incident Information

- Unit: 
- Response Mode: 
- Crew Type: 
- Response Delays: 
- Incident Location: 
- Dispatch Complaint: 

Example:
DO NOT USE THIS INFORMATION IN YOUR RESPONSE IT IS ONLY FOR REFERENCE
- Unit: 5-41-16
- Response Mode: non-emergent
- Crew Type: full crew
- Response Delays: none
- Incident Location: residence in new york
- Dispatch Complaint: knee pain

Here is the information: ({transcript})""",
    "patient_demographics": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for the patient's first name.
2. Review the entire document looking for the patient's date of birth.
3. Review the entire document looking for the patient's age.
4. Review the entire document looking for the patient's gender

Once you have obtained all the information give your response using the following template. If information is missing leave an answer of '[No Info]'.
Use Plain text. Do not add any comments or additional information.

Template

Patient Demographics

- Name: 
- Date of Birth: 
- Age:
- Gender: 

Example:
DO NOT USE THIS INFORMATION IN YOUR RESPONSE IT IS ONLY FOR REFERENCE
- Name: Scott
- Date of Birth: January 2nd, 1986
- Age: 38
- Gender: male

Here is the information: ({transcript})""",
    "subjective_info": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for the patient's address or facility name, unit and room where the patient is currently located.
2. Review the entire document looking for the location and position in which the patient was found.
3. Review the entire document looking for an initial description of the patient's appearance.
4. Review the entire document looking any medical equipment the patient is using or connected to when first encountered by the EMS crew. Do not include any equipment that was later placed by EMS.
5. Review the entire document looking for the patient's chief complaint.


Once you have obtained all the information give your response using the following template. This information will not always be provided. If no information is provided for a section, answer '[No Info]'.
Use Plain text. Do not add any comments or additional information.

Template

Subjective Information

- Address or Facility Name: 
- Patient Location and Position: 
- Patient Appearance: 
- Medical Equipment:
- Patient Chief Complaint: 

Here is the information: ({transcript})""",
    "history_of_present_illness": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for any other complaints, signs or symptoms mentioned by the patient.
2. Review the entire document looking for the onset of the patient's complaints (sudden, gradual, episodic, other).
3. Review the entire document looking for any information on what makes the patient's condition worse.
4. Review the entire document looking for any information on what makes the patient's condition better.
5. Review the entire document looking for how the patient describes their chief complaint.
6. Review the entire document looking for any mention of movement or radiation of the patient's complaint.
7. Review the entire document looking for the severity of the patient's complaint.
8. Review the entire document looking for when the complaints started.
9. Review the entire document looking for any actions or treatments completed before the EMS crew arrived.
10. Review the entire document looking for any further information on the history of the patient's present illness.

Once you have obtained all the information give your response using the following template. This information will not always be provided. If no information is provided for a section, answer '[No Info]'.
Use Plain text. Do not add any comments or additional information.

Template

History of Present Illness
- Associated Signs and Symptoms: 
- Onset:
- Provocation: 
- Palliation: 
- Quality: 
- Radiation: 
- Severity: 
- Time: 
- Interventions: 
- Additional History of Present Illness: 

Here is the information: ({transcript})""",
    "patient_histories": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for the patient's medical history.
2. Review the entire document looking for the patient's surgical history.
3. Review the entire document looking for the patient's social history.
4. Review the entire document looking for the patient's family history.
5. Review the entire document looking for the patient's sexual history.
6. Review the entire document looking for the patient's prescribed medications.
7. Review the entire document looking for the patient's allergies.

Once you have obtained all the information give your response using the following template. This information will not always be provided. If no information is provided for a section, answer '[No Info]'.
Use Plain text. Do not add any comments or additional information.

Template

Patient Histories

- Medical History:  
- Surgical History: 
- Social History: 
- Family History: 
- Sexual History: 
- Medications: 
- Allergies: 

Here is the information: ({transcript})""",
    "objective_1": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for objective exam findings related to the patient's general body system. This should include the patients level of consciousness (alert, verbal, painful, unresponsive) and the patients orientation status.
2. Review the entire document looking for objective exam findings related to the patient's skin.
3. Review the entire document looking for objective exam findings related to the patient's head.
4. Review the entire document looking for objective exam findings related to the patient's ears.
5. Review the entire document looking for objective exam findings related to the patient's eyes.
6. Review the entire document looking for objective exam findings related to the patient's nose.
7. Review the entire document looking for objective exam findings related to the patient's throat.
8. Review the entire document looking for objective exam findings related to the patient's neck, including the status of the patient's airways.

Once you have obtained all the information give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Objective Assessment
- GENERAL: 
- SKIN: 
- HEAD: 
- EARS: 
- EYES: 
- NOSE: 
- THROAT: 
- NECK: 

Here is the information: ({transcript})""",
    "objective_2": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for objective exam findings related to the patient's cardiovascular body system.
2. Review the entire document looking for objective exam findings related to the patient's respiratory body system.
3. Review the entire document looking for objective exam findings related to the patient's abdomen.
4. Review the entire document looking for objective exam findings related to the patient's genitourinal body system.
5. Review the entire document looking for objective exam findings related to the patient's gastrointestinal body system.
6. Review the entire document looking for objective exam findings related to the patient's spine.
7. Review the entire document looking for objective exam findings related to the patient's musculoskeletal body system.
8. Review the entire document looking for objective exam findings related to the patient's neurologic body system.
9. Review the entire document looking for objective exam findings related to the patient's phsychiatric body system.

Once you have obtained all the information give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Objective Assessment (Cont)
- CARDIOVASCULAR: 
- RESPIRATORY: 
- ABDOMEN: 
- GENITOURINARY: 
- GASTROINTESTINAL: 
- SPINE: 
- MUSCULOSKELETAL: 
- NEUROLOGICAL: 
- PSYCHIATRIC: 

Here is the information: ({transcript})""",
    "vitals": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for the patient's initial blood pressure.
2. Review the entire document looking for the patient's initial heart rate, rhythm (regular/irregular) and quality (strong, weak, bounding, thready.
3. Review the entire document looking for the patient's initial respiration rate, regularity (regular/irregular) and quality (slow, rapid, weak, assisted, mechanically ventilated).
4. Review the entire document looking for the patient's initial pulse oximetry (SpO2) percentage and whether the patient was on room air (RA) or oxygen (O2).
5. Review the entire document looking for the patient's initial pain level (0-10).
6. Review the entire document looking for the patient's initial temperature.

Once you have obtained all the information give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Vital Signs

- Blood Pressure: 
- Heart Rate: 
- Respiratory Rate: 
- SpO2: 
- Pain: 
- Temperature: 

Here is the information: ({transcript})""",
    "poc_tests": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for the patient's initial blood glucose level.
2. Review the entire document looking for the patient's initial EKG Interpretation (Rhythm name, rate range. Any Ectopy. Other Findings.)
3. Review the entire document looking for the patient's initial End Tidal CO2 (EtCO2) reading.
4. Review the entire document looking for the patient's initial Cincinnati Stroke Exam score (Positive/Negative).
5. Review the entire document looking for the patient's initial Los Angeles Motor Scale (LAMS) score (0-4).
6. Review the entire document looking for the patient's initial NIH Stroke Score (NIHSS).

Once you have obtained all the information give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Point of Care Testing
- Capillary Blood Glucose: 
- EKG: 
- EtCO2:
- Cincinnati: 
- LA Motor Scale: 
- NIHSS: 

Here is the information: ({transcript})""",
    "labs": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for lab results for a metabolic panel (Sodium (Na); Potassium (K); Chloride(Cl); Carbon Dioxide (CO2); Blood Urea Nitrogen (BUN); Creatinine (Cr); Glucose (Gluc); Calcium (Ca); Magnesium (Mg); Phosphorus (Phos)).
2. Review the entire document looking for lab results for a hematology panel (White Blood Count (WBC); Hemoglobin (Hgb); Hematocrit (Hct); Platelets (Plat))
3. Review the entire document looking for lab results for a hepatic panel (Total Bilirubin (Tot. Bilirubin); Alanine Transaminase (ALT); Aspartate Aminotransferase (AST); Alkaline Phosphatase (ALP))
4. Review the entire document looking for lab results for a coagulation panel (Prothrombin Time (PT); Partial Thromboplastin Time ((a)PTT); International Normalized Ratio (INR))
5. Review the entire document looking for lab results for a cardiac panel (Troponin; Creatinine Kinase (CK); Creatine Kinase-MB (CK-MB); Creatine Phosphokinase (CPK); B-Type Natriuretic Peptide (BNP))
6. Review the entire document looking for any other lab results.
Once you have obtained all the information, give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Laboratory Results
Metabolic - 
Hematology - 
Hepatic - 
Coagulation - 
Cardiac - 
Other - 

Here is the information: ({transcript})""",
    "imaging": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. There may be multiple imaging tests of the same type. If so each one should be listed individually. Follow the steps below to find the required information and then provide your response.

1. Review the entire document looking for X-ray results. 
2. Review the entire document looking for CAT Scan (CT) results. 
3. Review the entire document, looking for MRI results. 
4. Review the entire document, looking for Ultrasound results.
5. Review the entire document, looking for other imaging results.

Once you have obtained all the information, give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Imaging Reports
[List all X-Ray Results using this format: X-Ray (Target) @ (Date / Time): (Impression)]
[List all CT Results using this format: CT (Target) (with/without) contrast @ (Date / Time): (Impression)]
[List all MRI/MRA results using this format: MRI (or MRA) (Target) (with/without) contrast @ (Date / Time): (Impression)]
[List all Ultrasound results using this format: Ultrasound (Target)  @ (Date / Time): (Impression)]
[List all other imaging reports]

Here is the information: ({transcript})""",
    "impressions": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. If so each one should be listed individually. Follow the steps below to find the required information and respond.

1. Review the entire document for the EMS provider's primary impression or diagnosis.
2. Review the entire document for the EMS provider's secondary impressions or diagnoses.
3. Review the entire document for the destination the patient was transferred to.
4. Review the entire document for the transport mode (emergent/non-emergent) used to get to the destination.
5. Review the entire document to see if the patient refused further care or transport (yes/no).

Once you have obtained all the information, give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Impression Information
- Primary Impression:
- Secondary Impressions:
- Destination Name: 
- Transport Mode to Destination: 
- Patient Refusal: 

Here is the information: ({transcript})""",
    "treatments": """
As an expert in Natural Language Processing (NLP), your job is to pull out relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. If so each one should be listed individually. Follow the steps below to find the required information and respond.

1. Review the entire document for the medications given to the patient by the EMS provider.
2. Review the entire document for the procedures performed on the patient by the EMS provider.
3. Review the entire document for the IVs or IOs started on the patient.
4. Review the entire document for the point-of-care tests performed by the EMS provider.
5. Review the entire document for any treatments that were unsuccessful.
6. Review the entire document for any treatments that were considered but not given and the reasons why.


Once you have obtained all the information, give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Treatments
- Medications Given to Patient:
- Procedures Performed on Patient:
- IV or IO Access: 
- Point-of-Care Testing Performed on Patient: 
- Unsuccessful Treatments: 
- Deferred Treatments: 

Here is the information: ({transcript})""",
    "packaging": """
As an expert in Natural Language Processing (NLP), your job is to extract relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. If so, each one should be listed individually. Follow the steps below to find the required information and respond.

1. Review the entire document for any important events that happened before the patient was transported to the destination.
2. Review the entire document for any events that delayed transport to the destination.
3. Review the entire document for information on how the patient was moved to the transport stretcher.
4. Review the entire document for the safety equipment used to secure the patient to the transport stretcher.
5. Review the entire document for the monitoring equipment that was connected to the patient.

Once you have obtained all the information, give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Patient Packaging
- On-Scene Events:
- Scene Delays:
- Patient Movement to Stretcher: 
- Safety Equipment Used: 

Here is the information: ({transcript})""",
    "transport": """
As an expert in Natural Language Processing (NLP), your job is to extract relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. If so, each one should be listed individually. Follow the steps below to find the required information and respond.

1. Review the entire document for any notifications made to the destination.
2. Review the entire document for any events that occurred during transport.
3. Review the entire document for any delays which occurred during transport.
4. Review the entire document for changes to the patient's clinical condition.
5. Review the entire document for changes to the patient's vital signs or monitoring status.



Once you have obtained all the information, give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Transport Info
- Hospital Notifications: 
- Transport Events:
- Transport Delays:
- Clinical Changes: 
- Vitals and Monitoring Changes: 

Here is the information: ({transcript})""",
    "transfer_of_care": """
As an expert in Natural Language Processing (NLP), your job is to extract relevant medical information from documents provided to you. These documents will all be about EMS medical incidents. This information will not always be provided. If no information is provided for a section, answer '[No Info]'. If so, each one should be listed individually. Follow the steps below to find the required information and respond.

1. Review the entire document for the name and medical license of the person who received a report at the destination.
2. Review the entire document for the specific room, bed, unit, or department where the patient was transferred to at the destination.
3. Review the entire document to see how the patient was moved off the transport stretcher and into the destination's bed or chair.
4. Review the entire document for the safety measures used to protect the patient at the destination's bed or chair.
5. Review the entire document for any delays in the transfer of care.
6. Review the entire document for delays in the unit returning to service.
7. Review the entire document for any actions taken by the crew or events after the transfer of care and before the unit returned to service.



Once you have obtained all the information, give your response using the following template. Use Plain text. Do not add any comments or additional information.

Template

Transfer of Care
- Transfer of Care Personnel: 
- Bed or Room Patient Transferred to:
- How the Patient was Moved to the Destination Bed:
- Safety Measures Used: 
- Transfer of Care Delays: 
- Turn Around Delays: 
- Events Prior to Returning to Service: 

Here is the information: ({transcript})""",
}
