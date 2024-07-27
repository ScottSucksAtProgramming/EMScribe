from modules.model_loader import ModelLoader

class TranscriptExtractor:
    """
    A class to extract specific information from an EMS transcript using an AI model.

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

    def extract_information(self, transcript: str) -> dict:
        """
        Extracts specific information from the transcript.

        Args:
            transcript (str): The cleaned EMS transcript.

        Returns:
            dict: A dictionary containing extracted information.
        """
        sections = [
            "Demographics",
            "Medical History",
            "Chief Complaint",
            "History of Present Illness",
            "Treatments Done",
            "Objective Assessment",
            "Treatment Plan",
            "Transport Information",
            "Transfer of Care"
        ]

        prompts = {
            "Demographics": f"Extract the patient's name, age, and gender from the transcript: {transcript}",
            "Medical History": f"List the patient's past medical conditions and medications mentioned in the transcript: {transcript}",
            "Chief Complaint": f"Identify the patient's chief complaint from the transcript: {transcript}",
            "History of Present Illness": f"Describe the history of the present illness from the transcript: {transcript}",
            "Treatments Done": f"List the treatments done by the sending facility or interventions the patient completed on his own: {transcript}",
            "Objective Assessment": f"Provide an objective assessment of the patient by body system: {transcript}",
            "Treatment Plan": f"Outline the treatment plan provided to the patient by the EMS crew: {transcript}",
            "Transport Information": f"Detail how the patient was transported: {transcript}",
            "Transfer of Care": f"Provide information about the transfer of care: {transcript}"
        }

        extracted_info = {}
        for section, prompt in prompts.items():
            response = self.model_loader.generate(
                model=self.model_loader.model_name,
                prompts=[prompt],
                stream=False
            )
            extracted_info[section] = response.generations[0][0].text.strip()

        return extracted_info