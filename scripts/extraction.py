import requests

# URL for the locally running Ollama instance
OLLAMA_URL = "http://localhost:11434/api/generate"  # Correct endpoint

# Define the model name you are using locally
MODEL_NAME = "llama3"

# Define prompts for different types of information
demographics_prompt = "Extract the patient's name, age, and gender from the transcript: {}"
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
        "Demographics": extract_demographics(cleaned_transcript),
        "Medical History": extract_medical_history(cleaned_transcript),
        "Chief Complaint": extract_chief_complaint(cleaned_transcript),
        "History of Present Illness": extract_history_of_present_illness(cleaned_transcript),
        "Treatments Done": extract_treatments_done(cleaned_transcript),
        "Objective Assessment": extract_objective_assessment(cleaned_transcript),
        "Treatment Plan": extract_treatment_plan(cleaned_transcript),
        "Transport Information": extract_transport_information(cleaned_transcript),
        "Transfer of Care": extract_transfer_of_care(cleaned_transcript)
    }
    return extracted_data

# Import the preprocessing function
from scripts.preprocess import preprocess_transcript

# Example usage
if __name__ == "__main__":
    transcript = """
    Patient name is John Doe. Age: 45. Gender: Male. 
    Past medical history includes hypertension and diabetes. 
    The chief complaint is chest pain that started two hours ago...
    """
    extracted_data = process_transcript(transcript)
    for category, info in extracted_data.items():
        print(f"{category}:\n{info}\n")