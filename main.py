from scripts.preprocess import preprocess_transcript
from scripts.extraction import process_transcript

def main():
    # Example transcript text
    transcript = """
    Patient name is John Doe. Age: 45. Gender: Male. 
    Past medical history includes hypertension and diabetes. 
    The chief complaint is chest pain that started two hours ago...
    """
    
    # Process the transcript
    extracted_data = process_transcript(transcript)
    print("Extracted Data:")
    print(extracted_data)

if __name__ == "__main__":
    main()