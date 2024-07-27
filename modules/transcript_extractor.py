from modules.model_loader import ModelLoader

class TranscriptExtractor:
    """
    A class to extract information from transcripts.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
    """

    def __init__(self, model_loader: ModelLoader):
        """
        Initializes the TranscriptExtractor with a ModelLoader instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        """
        self.model_loader = model_loader

    def extract(self, transcript: str) -> dict:
        """
        Extracts various sections from the given transcript.

        Args:
            transcript (str): The transcript from which to extract information.

        Returns:
            dict: A dictionary containing the extracted sections.
        """
        prompts = {
            "Demographics": "Extract the patient's name, age, and gender from the transcript: {}",
            "Medical History": "List the patient's past medical conditions and medications mentioned in the transcript: {}",
            "Chief Complaint": "Identify the patient's chief complaint from the transcript: {}",
            "History of Present Illness": "Describe the history of the present illness from the transcript: {}",
            "Treatments Done": "List the treatments done by the sending facility or interventions the patient completed on his own: {}",
            "Objective Assessment": "Provide an objective assessment of the patient by body system: {}",
            "Treatment Plan": "Outline the treatment plan provided to the patient by the EMS crew: {}",
            "Transport Information": "Detail how the patient was transported: {}",
            "Transfer of Care": "Provide information about the transfer of care: {}"
        }

        extracted_data = {}
        for key, prompt in prompts.items():
            extracted_data[key] = self.model_loader.generate(prompt.format(transcript))

        return extracted_data