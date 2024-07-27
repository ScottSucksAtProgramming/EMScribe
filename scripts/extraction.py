import requests

# URL for the locally running Ollama instance
OLLAMA_URL = "http://localhost:11434/api/generate"  # Correct endpoint

# Define the model name you are using locally
MODEL_NAME = "llama3"

# Define prompts for different types of information
call_info_prompt = """Extract the following EMS incident information from the provided transcript: unit or vehicle number, response mode (emergent/non-emergent), crew type (full crew/paramedic only), any delays in response (otherwise assume none), starting location, incident location, dispatch complaint, and any additional information given to the crew by dispatch. Analyze the transcript carefully to find the most accurate answers for each item. If you are uncertain about any information, mark it with a 🚩 emoji.

Present the extracted information in a clear, concise list. If any fields lack information, write only [No Info] (for Delays just write: None). Do not use any additional formatting.

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

Here is the transcript: {}"""
demographics_prompt = """Extract the following patient information: name, date of birth, age, gender, race or ethnicity, phone number, address or facility name, room number, and next of kin or family contact information. Calculate the age if necessary. Assume the gender if not explicitly stated based on the name provided.

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

Here is the transcript: {}
"""
medical_history_prompt = "List the patient's past medical conditions and medications mentioned in the transcript: {}"
chief_complaint_prompt = "Identify the patient's chief complaint from the transcript: {}"
history_of_present_illness_prompt = "Describe the history of the present illness from the transcript: {}"
treatments_done_prompt = "List the treatments done by the sending facility or interventions the patient completed on his own: {}"
objective_assessment_prompt = "Provide an objective assessment of the patient by body system: {}"
treatment_plan_prompt = "Outline the treatment plan provided to the patient by the EMS crew: {}"
transport_information_prompt = "Detail how the patient was transported: {}"
transfer_of_care_prompt = "Provide information about the transfer of care: {}"

def call_ollama_local(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False  # Setting stream to False for a single response object
        }
    )
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()['response'].strip()  # Adjusting the parsing to match the API response format

# Define extraction functions

def extract_call_information(transcript):
    return call_ollama_local(call_info_prompt.format(transcript))

def extract_demographics(transcript):
    return call_ollama_local(demographics_prompt.format(transcript))

def extract_medical_history(transcript):
    return call_ollama_local(medical_history_prompt.format(transcript))

def extract_chief_complaint(transcript):
    return call_ollama_local(chief_complaint_prompt.format(transcript))

def extract_history_of_present_illness(transcript):
    return call_ollama_local(history_of_present_illness_prompt.format(transcript))

def extract_treatments_done(transcript):
    return call_ollama_local(treatments_done_prompt.format(transcript))

def extract_objective_assessment(transcript):
    return call_ollama_local(objective_assessment_prompt.format(transcript))

def extract_treatment_plan(transcript):
    return call_ollama_local(treatment_plan_prompt.format(transcript))

def extract_transport_information(transcript):
    return call_ollama_local(transport_information_prompt.format(transcript))

def extract_transfer_of_care(transcript):
    return call_ollama_local(transfer_of_care_prompt.format(transcript))

# Define a function to process the transcript using all prompts
def process_transcript(transcript):
    cleaned_transcript = preprocess_transcript(transcript)
    extracted_data = {
        "Call Information": extract_call_information(cleaned_transcript),
        "Demographics": extract_demographics(cleaned_transcript),
        # "Medical History": extract_medical_history(cleaned_transcript),
        # "Chief Complaint": extract_chief_complaint(cleaned_transcript),
        # "History of Present Illness": extract_history_of_present_illness(cleaned_transcript),
        # "Treatments Done": extract_treatments_done(cleaned_transcript),
        # "Objective Assessment": extract_objective_assessment(cleaned_transcript),
        # "Treatment Plan": extract_treatment_plan(cleaned_transcript),
        # "Transport Information": extract_transport_information(cleaned_transcript),
        # "Transfer of Care": extract_transfer_of_care(cleaned_transcript)
    }
    return extracted_data

# Import the preprocessing function
from scripts.preprocess import preprocess_transcript

# Example usage
if __name__ == "__main__":
    transcript = """This is Unit 5-41-16 responding emergent from Stony Brook University Hospital we have a full crew, heading to the
Stony Brook Cancer Center for a reported fever.

Unit 5-41-16 on scene at the Stony Brook Cancer Center,

marked level 5, hallway E, room E2 for a patient with a high white count.

So we have paperwork and everything for him?

I can print it for you.

Awesome.

You guys are so fast.

I got a 20 to 60, perfect.

Yeah, we're going to hook up the--

Our time is 60 minutes from now.

OK.

Hi, John.

My name is Scott.

I'm going to be taking you over to the ER at Stony Brook,

all the way around the other side of the building.

And then I'll print out his last progress, and then we'll--

Yeah, so that's it.
That's it, OK.

I think that has the meds and the vitals.
Perfect.
Yeah, that's all I need.

Okay, let me set that for you.

How are you feeling?

Not that bad.
Okay.

Did you come in today because you weren't feeling well or is this normal?

No, it was an appointment.

It was an appointment?
Okay.
Awesome.
OK, so I'm going to go ahead and get you a little bit of a massage.

This patient is John Smith, 
date of birth 4/6/1960, MRN is 34612345.

A 20-gauge IV was placed in his left AC with a 500-milliliter bag of normal saline running
to gravity.

It's more important to get them over there.
Yeah.

John, you need a little walk at all?

Yeah, okay.
I'm less dizzy on the way in.
Okay, you still feeling dizzy now?

No, I wasn't that way.

This is your jacket, did you tell him?

Yeah, it's your jacket.

I'm just going to put it on my stretcher so we have it, okay?

Do you have anything else that needs to come with this?

I think there's the phones in there.
Yeah, the phones in the pocket.

I'm going to put it back here for you once the seat's down.
I need your help with this.
Okay.

In the back, it looks tough.
So whenever you're ready we'll just have you stand up and take a seat right on there.
Yeah, that would be great, thank you.
Alright.
Can we hold that for you?
Thank you guys.
No problem.

Just going to run the blood pressure and we are good to go.

history of hypertension, BPH.
Relapse, refactory, CLL slash SLL.
Complicated by extensive lymphadenopathy and refractory transfusion.
Chemistry, sodium 140, potassium 3.8, chloride 99, bicarb 31, glucose high at 149, BUN high at 41, creatinine high
at 2.17, calcium critically high at 15.5, total bilirubin 0.7, direct bilirubin 0.2, ALT 8,
"""
    extracted_data = process_transcript(transcript)
    for category, info in extracted_data.items():
        print(f"{category}:\n{info}\n")
