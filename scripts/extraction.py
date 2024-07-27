from model_loader import ModelLoader
from extractor import TranscriptExtractor

def extract_information(transcript):
    extractor = TranscriptExtractor(model_loader=ModelLoader(base_url="http://localhost:11434", model_name="llama3.1"))
    extracted_data = extractor.extract(transcript)
    return extracted_data

# Example usage
if __name__ == "__main__":
    example_transcript = "Patient name is John Doe. Age: 45. Gender: Male. Past medical history includes hypertension and diabetes. The chief complaint is chest pain that started two hours ago..."
    extracted_data = extract_information(example_transcript)
    for key, value in extracted_data.items():
        print(f"{key}: {value}")