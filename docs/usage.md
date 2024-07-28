# Usage

This guide will show you how to use EMScribe 2.0 for extracting and cleaning EMS transcripts, as well as generating comprehensive EMS narratives.

## Running the Extraction Script

The extraction script processes a transcript to extract detailed patient information.

### Command

To run the extraction script, use the following command:

```bash
python -m scripts.extraction
```

### Example Transcript Input

Here is an example of the input transcript:

```plaintext
Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes.
```

### Expected Output

The script will output detailed information extracted from the transcript, formatted into comprehensive EMS narratives.

```plaintext
Extracted Information:
incident_info: ...
patient_demographics: John Doe, 45, Male
patient_histories: Hypertension, Diabetes
...
```

## Running the Preprocess Script

The preprocess script cleans a transcript by removing repeated words and lines, correcting basic errors, and ensuring meaningful information is preserved.

### Command

To run the preprocess script, use the following command:

```bash
python -m scripts.preprocess
```

### Example Transcript Input

Here is an example of the input transcript:

```plaintext
The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain.
```

### Expected Output

The script will output a cleaned version of the transcript:

```plaintext
The patient is experiencing shortness of breath. The patient is also complaining of chest pain.
```

## Running the Narrative Generation Script

The narrative generation script creates a comprehensive EMS narrative from the extracted data.

### Command

To run the narrative generation script, use the following command:

```bash
python -m scripts.main
```

### Example Usage

The following example demonstrates how to use the `TranscriptCleaner`, `TranscriptExtractor`, and `NarrativeManager` classes to process a transcript and generate a narrative.

#### Code Example

```python
from modules.prompt_manager import PromptManager
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.transcript_extractor import TranscriptExtractor
from modules.narrative_manager import NarrativeManager

# Initialize PromptManager
prompt_manager = PromptManager()

# Initialize ModelLoader
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize TranscriptCleaner
cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)

# Initialize TranscriptExtractor
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

# Initialize NarrativeManager
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

# Example usage for generating a narrative
def example_generate_narrative():
    example_transcript = """
        This is Ambulance 292 responding emergent with a full crew and no delays from headquarter to the Kevorkian Clinic for a reported chest pain. During transport disptach informed us that the patient is alert and breathing.

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

    # Step 1: Extract information from the transcript
    extracted_data = extractor.extract(example_transcript)
    
    # Step 2: Use the extracted data to generate the narrative
    narrative = narrative_manager.generate_narrative("presoaped_format", data=extracted_data)
    
    print("Generated Narrative:")
    print(narrative)

# Example usage for cleaning a transcript
def example_clean_transcript():
    example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    cleaned_transcript = cleaner.clean(example_transcript)
    print("Cleaned Transcript:")
    print(cleaned_transcript)

# Example usage for extracting information from a transcript
def example_extract_information():
    example_transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
    extracted_data = extractor.extract(example_transcript)
    print("Extracted Information:")
    print(extracted_data)

if __name__ == "__main__":
    example_clean_transcript()
    example_extract_information()
    example_generate_narrative()
```

## Using the Scripts

### Extracting Information

1. Navigate to the project directory.

2. Run the extraction script:

   ```bash
   python -m scripts.extraction
   ```

3. The script will process the example transcript and print the extracted information.

### Cleaning a Transcript

1. Navigate to the project directory.

2. Run the preprocess script:

   ```bash
   python -m scripts.preprocess
   ```

3. The script will process the example transcript and print the cleaned transcript.

### Generating a Narrative

1. Navigate to the project directory.

2. Run the main script:

   ```bash
   python -m scripts.main
   ```

3. The script will process the example transcript, extract information, and generate a narrative.

## Conclusion

EMScribe 2.0 provides powerful tools for extracting, cleaning, and generating EMS narratives using AI models. By following the examples and commands provided, you can effectively utilize these tools to process your own transcripts. For more advanced usage and customization, refer to the [Development](development.md) and [API Reference](api_reference.md) sections of the documentation.