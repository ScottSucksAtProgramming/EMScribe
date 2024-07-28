# Usage

This guide will show you how to use EMScribe 2.0 for extracting and cleaning EMS transcripts and generating narratives.

## CLI Usage

The `emscribe` command can be used to clean transcripts, extract information, and generate narratives.

### Clean Transcript

To clean a transcript, use the following command:

```bash
emscribe clean path/to/transcript.txt
```

### Extract Information

To extract information from a transcript, use the following command:

```bash
emscribe extract path/to/transcript.txt
```

### Generate Narrative

To generate a narrative from a transcript, use the following command:

```bash
emscribe generate path/to/transcript.txt --output path/to/output.txt
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

### Example Usage

#### Cleaning a Transcript

The `TranscriptCleaner` class can be used to clean up a transcript using an AI model.

#### Code Example

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)

# Clean a transcript
example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
cleaned_transcript = cleaner.clean(example_transcript)
print("Cleaned Transcript:")
print(cleaned_transcript)
```

#### Extracting Information from a Transcript

The `TranscriptExtractor` class can be used to extract information from a transcript using an AI model.

#### Code Example

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

# Extract information from a transcript
example_transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
extracted_data = extractor.extract(example_transcript)
print("Extracted Information:")
for key, value in extracted_data.items():
    print(f"{key}: {value}")
```

## Conclusion

EMScribe 2.0 provides powerful tools for extracting and cleaning EMS transcripts using AI models. By following the examples and commands provided, you can effectively utilize these tools to process your own transcripts. For more advanced usage and customization, refer to the [Development](development.md) and [API Reference](api_reference.md) sections of the documentation.