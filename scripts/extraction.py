from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.prompt_manager import PromptManager

# Initialize PromptManager
prompt_manager = PromptManager()

# Function to extract information from the transcript
def extract_information(transcript):
    # Initialize ModelLoader
    model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
    
    # Initialize TranscriptCleaner with ModelLoader and PromptManager
    cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)
    
    # Initialize TranscriptExtractor with ModelLoader and PromptManager
    extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)
    
    # Clean the transcript
    cleaned_transcript = cleaner.clean(transcript)
    
    # Extract information from the cleaned transcript
    extracted_data = extractor.extract(cleaned_transcript)
    
    return extracted_data

# Example usage
if __name__ == "__main__":
    example_transcript = """
        This is Ambulance 292 responding emergent with a full crew and no delays to the Kevorkian Clinic for a reported chest pain. During transport disptach informed us that the patient is alert and breathing.

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
    extracted_data = extract_information(example_transcript)
    print("Extracted Information:")
    print(extracted_data)
