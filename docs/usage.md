# Usage

This guide will show you how to use EMScribe 2.0 for extracting and cleaning EMS transcripts.

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

## Example Usage

### Cleaning a Transcript

The `TranscriptCleaner` class can be used to clean up a transcript using an AI model.

#### Code Example

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner

# Initialize PromptManager
prompt_manager = PromptManager()

# Initialize ModelLoader
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize TranscriptCleaner
cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)

# Clean a transcript
example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
cleaned_transcript = cleaner.clean(example_transcript)
print("Cleaned Transcript:")
print(cleaned_transcript)
```

### Extracting Information from a Transcript

The `TranscriptExtractor` class can be used to extract information from a transcript using an AI model.

#### Code Example

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor

# Initialize PromptManager
prompt_manager = PromptManager()

# Initialize ModelLoader
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")

# Initialize TranscriptExtractor
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

# Extract information from a transcript
example_transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
extracted_data = extractor.extract(example_transcript)
print("Extracted Information:")
for key, value in extracted_data.items():
    print(f"{key}: {value}")
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

## Conclusion

EMScribe 2.0 provides powerful tools for extracting and cleaning EMS transcripts using AI models. By following the examples and commands provided, you can effectively utilize these tools to process your own transcripts. For more advanced usage and customization, refer to the [Development](development.md) and [API Reference](api_reference.md) sections of the documentation.