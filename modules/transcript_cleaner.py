from modules.model_loader import ModelLoader

class TranscriptCleaner:
    """
    A class to clean up an EMS transcript using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
    """

    def __init__(self, model_loader: ModelLoader):
        """
        Initializes the TranscriptCleaner with a ModelLoader instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        """
        self.model_loader = model_loader

    def clean_transcript(self, transcript: str) -> str:
        """
        Cleans up the transcript by removing repeating words, phrases, or lines.

        Args:
            transcript (str): The original EMS transcript.

        Returns:
            str: The cleaned-up version of the transcript.
        """
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
        response = self.model_loader.generate(
            model=self.model_loader.model_name,
            prompts=[prompt],
            stream=False
        )
        cleaned_transcript = response.generations[0][0].text.strip()
        return cleaned_transcript