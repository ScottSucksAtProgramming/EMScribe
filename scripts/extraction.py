from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.prompt_manager import PromptManager


class EMSExtractor:
    """
    EMSExtractor is a class responsible for cleaning and extracting information from EMS transcripts
    using AI models.

    Attributes:
        cleaner (TranscriptCleaner): An instance of TranscriptCleaner to clean transcripts.
        extractor (TranscriptExtractor): An instance of TranscriptExtractor to extract
        information from cleaned transcripts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the EMSExtractor with a ModelLoader and PromptManager instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.cleaner = TranscriptCleaner(
            model_loader=model_loader, prompt_manager=prompt_manager
        )
        self.extractor = TranscriptExtractor(
            model_loader=model_loader, prompt_manager=prompt_manager
        )

    def extract_information(self, transcript: str) -> str:
        """
        Cleans the transcript and extracts information from it.

        Args:
            transcript (str): The transcript to clean and extract information from.

        Returns:
            str: The extracted information from the cleaned transcript.
        """
        # Clean the transcript
        cleaned_transcript = self.cleaner.clean(transcript)
        # Extract information from the cleaned transcript
        extracted_data = self.extractor.extract(cleaned_transcript)
        return extracted_data


def main():
    # Initialize PromptManager and ModelLoader
    prompt_manager = PromptManager()
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

    # Create EMSExtractor
    ems_extractor = EMSExtractor(model_loader, prompt_manager)

    # Example usage
    example_transcript = """
        This is Ambulance 292 responding emergent with a full crew and no delays to the Kevorkian Clinic for a reported chest pain. During transport dispatch informed us that the patient is alert and breathing.

        Unit 292 arriving on scene.

        Our patient is Frederich Neizche he was born February 8th, 1986. He is a 38 year old male. Complaining for severe 10/10 chest pain. He is receiving oxygen via a nasal cannula and is lying on the exam table in room 1.

        Frederich can you tell me what's going on today?

        About two hours ago I was sitting and watching TV in my living room and I began to feel a sudden crushing pressure in my chest. 

        Do you have any shortness of breath? 

        No, but I do feel nauseous and dizzy. I've also been sweating a lot. I took one of my nitro tabs but it didn't help. Any time I stand up or try to do any activity the pain gets worse. I feel a little better when I'm laying down.

        Does the pain radiate or move?

        I also have pain to my jaw and down my left arm.

        On a scale of 1 to 10, with 10 being the worst pain you've ever felt in your life and 1 being almost no pain what is it right now. 

        It's a 10. It's really bad.

        According to the paperwork provided by the doctor here Frederich has a known medical history of coronary artery disease, hypertension, high cholesterol, type 2 diabetes, BPH, GERD and a previous MI in 2018 with two cardiac stents placed. 

        The doctor has placed an IV in the patients right arm, and gave them another dose of sublingual nitro. He also did an EKG which show ST Elevations in leads II, III, and aVF with a reciprocal ST Depression in aVL.

        Do you have any allergies?

        Only to cats and kiwi.

        What medications do you take?

        I take metoprolol for my blood pressure, eliquis, and  metformin.

        Okay great. I'm going to do a quick exam.

        Sure go ahead.

        patient is alert and oriented to person place time and event. He appears pale and diaphoretic and in obvious pain. He is dressed in normal clothes and appear to be well groomed. Frederich's skin is pale, cool and diaphoretic. skin is intact. There are no rashes or bleeding. Airways a patent with good air movement. he is able to speak in full sentence. Trachea is midline. The chest is atraumatic without bruising, implanted devices or flail segments. heart rate is rapid, regular and weak. Distal pulses are palpable but thready. No edema noted.

        Lung sounds a clear and equal bilaterally. Chest expansion is adequate and even. Respiratory pattern is regular and elevated with increased work of breathing.

        Frederich is calm and his behavior is appropriate to the situation. thought pattern and speech are organized no bizarre behavior noted.

        EKG shows Sinus Rhythm at 100 with PVCs.

        Blood sugar is 84.

        Vitals are 102/54, heart rate 100 weak and regular, 17 breaths per minutes regular and labored, SpO2 is 98%, EtCO2 is 33.
    """
    extracted_data = ems_extractor.extract_information(example_transcript)
    print("Extracted Information:")
    print(extracted_data)


if __name__ == "__main__":
    main()
