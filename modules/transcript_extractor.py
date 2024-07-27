from modules.model_loader import ModelLoader

class TranscriptExtractor:
    """
    A class to extract information from EMS transcripts using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
    """

    def __init__(self, model_loader):
        """
        Initializes the TranscriptExtractor with a ModelLoader instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        """
        self.model_loader = model_loader

    def extract(self, transcript):
        """
        Extracts relevant information from the EMS transcript.

        Args:
            transcript (str): The transcript from which to extract information.

        Returns:
            dict: A dictionary containing the extracted information.
        """
        prompts = {
            "Demographics": "Extract the patient's name, age, and gender from the transcript: {transcript}",
            "Medical History": "List the patient's past medical conditions and medications mentioned in the transcript: {transcript}",
            "Chief Complaint": "Identify the patient's chief complaint from the transcript: {transcript}",
            "History of Present Illness": "Describe the history of the present illness from the transcript: {transcript}",
            "Treatments Done": "List the treatments done by the sending facility or interventions the patient completed on his own: {transcript}",
            "Objective Assessment": "Provide an objective assessment of the patient by body system: {transcript}",
            "Treatment Plan": "Outline the treatment plan provided to the patient by the EMS crew: {transcript}",
            "Transport Information": "Detail how the patient was transported: {transcript}",
            "Transfer of Care": "Provide information about the transfer of care: {transcript}"
        }

        extracted_data = {}
        for key, prompt in prompts.items():
            full_prompt = prompt.format(transcript=transcript)
            response = self.model_loader.generate(full_prompt, stream=False)
            extracted_data[key] = response
        
        return extracted_data