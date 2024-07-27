from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor

def main(transcript):
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    
    # Clean the transcript
    cleaner = TranscriptCleaner(model_loader=model_loader)
    cleaned_transcript = cleaner.clean(transcript)
    
    # Extract information
    extractor = TranscriptExtractor(model_loader=model_loader)
    extracted_data = extractor.extract(cleaned_transcript)
    
    return extracted_data

# Example usage
if __name__ == "__main__":
    example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain. Patient name is John Doe. Age: 45. Gender: Male. Past medical history includes hypertension and diabetes. The chief complaint is chest pain that started two hours ago..."
    extracted_data = main(example_transcript)
    for key, value in extracted_data.items():
        print(f"{key}: {value}")