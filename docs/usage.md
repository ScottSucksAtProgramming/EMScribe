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
    example_transcript = "Unit 5-41-16 responding emergent to Dermatology office in Levittown. Dispatch reports a male patient with an unknown complaint. Unit has a full crew and experiences no delays. Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."

    # Step 1: Extract information from the transcript
    extracted_data = extractor.extract(example_transcript)
    
    # Step 2: Use the extracted data to generate the narrative
    narrative = narrative_manager.generate_narrative("presoaped_format", extracted_data)
    
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