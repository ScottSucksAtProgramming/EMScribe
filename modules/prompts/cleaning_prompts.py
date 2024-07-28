# modules/prompts/cleaning_prompts.py

cleaning_prompts = {
    "clean_transcript": """
You will act as an expert in Natural Language Processing (NLP) to help clean transcripts of recorded EMS incidents. The goal is to remove all transcription errors and unnecessary parts while ensuring that the shortest possible transcript still contains all essential medical and EMS incident information. 

Your task includes:
1. Removing filler words, false starts, irrelevant conversations, background noise transcriptions, and repeating words or phrases.
2. Ensuring the cleaned transcript remains concise yet retains all important information and context related to the medical and EMS incident.
3. Preserving medical terms, abbreviations, and phrases critical to understanding the incident, even if not explicitly listed here.
4. Formatting the output into bullet points for clarity.
5. Reviewing and correcting any transcription errors that may alter the meaning or accuracy of the incident details.
6. Prioritizing clarity and accuracy over brevity in cases of ambiguity.
7. Organizing the cleaned transcript in chronological order.
8. Comparing the cleaned transcript with the original version to ensure no important information has been left out.
9. Never provide any commentary or notes. Just the clean version of the transcript.

Here is a the transcript for you to clean:
{transcript}
    """
}
