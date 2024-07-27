def preprocess_transcript(transcript):
    """
    Clean the transcribed text to make it easier for information extraction.
    This can include removing unnecessary symbols, correcting common transcription errors, etc.
    """
    # Replace newline characters with spaces
    cleaned_transcript = transcript.replace('\n', ' ')
    # Remove extra spaces
    cleaned_transcript = ' '.join(cleaned_transcript.split())
    # You can add more preprocessing steps as needed
    return cleaned_transcript

# Example usage
if __name__ == "__main__":
    transcript = """
    Patient name is John Doe. Age: 45. Gender: Male. 
    Past medical history includes hypertension and diabetes. 
    The chief complaint is chest pain that started two hours ago...
    """
    cleaned_transcript = preprocess_transcript(transcript)
    print(cleaned_transcript)