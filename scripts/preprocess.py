from langchain_community.llms import Ollama  # Ensure this import is correct and the package is available
import re

# Initialize Ollama with your local configuration
ollama = Ollama(base_url="http://localhost:11434")

# Function to clean up the transcript using the specified prompt
def clean_transcript(transcript):
    prompt = f"""
    You will act as an expert in natural language processing to help me clean up a transcript of an EMS medical call. The transcript is in plain text format and may contain various transcription errors. Your primary task is to identify and remove any repeating words, phrases, or lines that do not contribute to the meaningful content of the transcript. Additionally, ensure that all meaningful information is preserved as much as possible.

    Here is the specific guidance:

    1. Remove Repeating Words and Phrases: If a word or phrase is repeated consecutively or within a short span without adding any value, remove the redundant parts.
    2. Remove Repeating Lines: If entire lines or segments of text are repeated, keep only one instance of each.
    3. Preserve Meaningful Information: Ensure that all critical information related to the medical call, such as patient details, medical conditions, and instructions, is retained and not inadvertently removed.
    4. Correct Basic Errors: While focusing on repetition, also correct any basic typographical errors if they are straightforward and do not require additional context to understand.

    Here is an example of a text with errors:

    “The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain.”

    After cleaning, it should read:

    “The patient is experiencing shortness of breath. The patient is also complaining of chest pain.”

    Once complete, provide the cleaned-up version of the transcript. Do not provide anything else.

    Please apply this process to the following transcript:

    {transcript}
    """
    response = ollama.generate(
        model="llama3",  # Specify the model name you're using
        prompts=[prompt],  # Wrap prompt in a list
        stream=False  # Stream is false to get a single response
    )
    # Extract the text from the LLMResult object
    cleaned_transcript = response.generations[0][0].text
    return cleaned_transcript.strip()

# Basic text cleaning function to preprocess the transcript
def preprocess_transcript(transcript):
    # Apply the cleaning function
    cleaned_transcript = clean_transcript(transcript)
    
    # Further basic preprocessing steps (if any)
    cleaned_transcript = re.sub(r'\s+', ' ', cleaned_transcript).strip()
    
    return cleaned_transcript

# Example usage
if __name__ == "__main__":
    example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    print(preprocess_transcript(example_transcript))