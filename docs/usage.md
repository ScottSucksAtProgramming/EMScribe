# 🚀 Usage Guide

Welcome to the EMScribe usage guide! Here, you'll learn how to use EMScribe to extract and clean EMS transcripts, review extracted information, and generate comprehensive narratives.

## 📋 CLI Usage

The `emscribe` command-line tool allows you to clean transcripts, extract information, review extracted data, and generate narratives effortlessly.

### 🧼 Clean Transcript

To clean a transcript, use the following command:

```bash
emscribe clean path/to/transcript.txt --output path/to/cleaned_transcript.txt
```

### 📜 Extract Information

To extract information from a transcript, use the following command:

```bash
emscribe extract path/to/cleaned_transcript.txt --output path/to/extract.txt
```

### 🧐 Review Extracted Information

To review and make changes to the extracted information, use the following command:

```bash
emscribe review path/to/extract.txt --output path/to/reviewed_extract.txt
```

### 📄 Generate Narrative

To generate a narrative from the reviewed extracted information, use the following command:

```bash
emscribe generate path/to/reviewed_extract.txt --output path/to/narrative.txt
```

### ⛓️ Using Pipes

You can streamline the process by using pipes. Here’s an example of cleaning a transcript and generating a narrative in one command:

```bash
emscribe clean path/to/transcript.txt | emscribe extract - | emscribe review - | emscribe generate - --output path/to/narrative.txt
```

### 📝 Example Transcript Input

Here is an example of the input transcript:

```plaintext
Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes.
```

### 📋 Expected Output

The script will output detailed information extracted from the transcript, formatted into comprehensive EMS narratives.

```plaintext
Extracted Information:
incident_info: ...
patient_demographics: John Doe, 45, Male
patient_histories: Hypertension, Diabetes
...
```

## 🛠️ Example Usage

### 🧼 Cleaning a Transcript

The `TranscriptCleaner` class can be used to clean up a transcript using an AI model.

#### Code Example

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(model_name="llama3.1")
cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)

# Clean a transcript
example_transcript = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
cleaned_transcript = cleaner.clean(example_transcript)
print("Cleaned Transcript:")
print(cleaned_transcript)
```

### 📜 Extracting Information from a Transcript

The `TranscriptExtractor` class can be used to extract information from a transcript using an AI model.

#### Code Example

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(model_name="llama3.1")
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

# Extract information from a transcript
example_transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
extracted_data = extractor.extract(example_transcript)
print("Extracted Information:")
print(extracted_data)
```

### 🧐 Reviewing Extracted Information

The `ExtractReviewer` class can be used to review and modify the extracted information using an AI model.

#### Code Example

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.extract_reviewer import ExtractReviewer

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(model_name="llama3.1")
reviewer = ExtractReviewer(model_loader=model_loader, prompt_manager=prompt_manager)

# Review extracted information
extracted_data = "Incident Information\n- Unit: [No Info]\n- Response Mode: emergent\n..."
reviewed_data = reviewer.review_section(extracted_data)
print("Reviewed Information:")
print(reviewed_data)
```

### 📄 Generating a Narrative

The `NarrativeManager` class can be used to generate a narrative from the reviewed extracted information.

#### Code Example

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.narrative_manager import NarrativeManager

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(model_name="llama3.1")
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

# Generate a narrative
reviewed_data = "Incident Information\n- Unit: 292\n- Response Mode: emergent\n..."
narrative = narrative_manager.generate_narrative("narrative_format", reviewed_data)
print("Generated Narrative:")
print(narrative)
```

## 🎉 Conclusion

EMScribe provides powerful tools for extracting, cleaning, reviewing, and generating EMS transcripts using AI models. By following the examples and commands provided, you can effectively utilize these tools to process your own transcripts. For more advanced usage and customization, refer to the [Development](development.md) and [API Reference](api_reference.md) sections of the documentation.