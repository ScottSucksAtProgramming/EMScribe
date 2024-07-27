from scripts.preprocess import preprocess_transcript

def main():
    # Example transcript text
    transcript = """
    Patient name is John Doe. Age: 45. Gender: Male. 
    Past medical history includes hypertension and diabetes. 
    The chief complaint is chest pain that started two hours ago...
    """
    
    # Preprocess the transcript
    cleaned_transcript = preprocess_transcript(transcript)
    print("Cleaned Transcript:")
    print(cleaned_transcript)
    
    # Add further processing and extraction steps here

if __name__ == "__main__":
    main()