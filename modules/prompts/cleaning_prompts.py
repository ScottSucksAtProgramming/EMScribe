# modules/prompts/cleaning_prompts.py

cleaning_prompts = {
    "clean_transcript": """
You will act as an expert in Natural Language Processing (NLP) to help clean transcripts of recorded EMS incidents. The goal is to remove all 
transcription errors and unnecessary parts while ensuring that the shortest possible transcript still contains all essential medical and EMS 
incident information. 

Your task includes:
1. Removing filler words, false starts, irrelevant conversations, background noise transcriptions, and repeating words or phrases.
8. Comparing the cleaned transcript with the original version to ensure no important information has been left out.

When you provide your response only provide the cleaned transcript and nothing more.

Here is a the transcript for you to clean:
{transcript}
    """
}
