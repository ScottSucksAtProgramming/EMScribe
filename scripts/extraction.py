from langchain import Chain, Prompt

# Define prompts for different types of information
demographics_prompt = Prompt("Extract the patient's name, age, and gender from the transcript.")
medical_history_prompt = Prompt("List the patient's past medical conditions and medications mentioned in the transcript.")
chief_complaint_prompt = Prompt("Identify the patient's chief complaint from the transcript.")

# Define extraction functions
def extract_demographics(transcript):
    return demographics_prompt.run(transcript)

def extract_medical_history(transcript):
    return medical_history_prompt.run(transcript)

def extract_chief_complaint(transcript):
    return chief_complaint_prompt.run(transcript)

# Create a chain for information extraction
extraction_chain = Chain([extract_demographics, extract_medical_history, extract_chief_complaint])

# Example function to process the transcript
def process_transcript(transcript):
    cleaned_transcript = preprocess_transcript(transcript)
    extracted_data = extraction_chain.run(cleaned_transcript)
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
    print(extracted_data)