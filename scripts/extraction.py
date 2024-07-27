from modules.model_loader import ModelLoader
from modules.transcript_extractor import TranscriptExtractor
from modules.prompt_manager import PromptManager

# Initialize PromptManager
prompt_manager = PromptManager()

# Function to extract information from the transcript
def extract_information(transcript):
    # Initialize ModelLoader
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    
    # Initialize TranscriptExtractor with ModelLoader and PromptManager
    extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)
    
    # Extract information from the transcript
    extracted_data = extractor.extract(transcript)
    
    return extracted_data

# Example usage
if __name__ == "__main__":
    example_transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
    extracted_data = extract_information(example_transcript)
    print("Extracted Information:")
    for key, value in extracted_data.items():
        print(f"{key}: {value}")