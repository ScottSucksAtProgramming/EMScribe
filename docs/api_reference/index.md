# 🚀 EMScribe API Reference

Welcome to the EMScribe API Reference! This document provides a comprehensive overview of the EMScribe API, detailing the main modules, their classes, and methods. Whether you're a developer looking to extend EMScribe or a user wanting to understand its internals, you've come to the right place.

## 📑 Table of Contents

- [🚀 EMScribe API Reference](#-emscribe-api-reference)
   - [📑 Table of Contents](#-table-of-contents)
   - [📚 Modules](#-modules)
      - [Model Loader](#model-loader)
      - [Prompt Manager](#prompt-manager)
      - [Transcript Cleaner](#transcript-cleaner)
      - [Transcript Extractor](#transcript-extractor)
      - [Narrative Manager](#narrative-manager)
      - [Extract Reviewer](#extract-reviewer)
   - [🛠️ CLI](#️-cli)
      - [📜 Commands](#-commands)
      - [🔧 Example Usage](#-example-usage)
   - [🔍 Usage Examples](#-usage-examples)
      - [Example 1: Cleaning a Transcript](#example-1-cleaning-a-transcript)
      - [Example 2: Extracting Information from a Transcript](#example-2-extracting-information-from-a-transcript)
      - [Example 3: Generating an EMS Narrative](#example-3-generating-an-ems-narrative)
   - [🎉 Conclusion](#-conclusion)

## 📚 Modules

EMScribe is composed of several key modules, each serving a specific purpose in the workflow. Click on the links below for detailed documentation on each module.

### [Model Loader](model_loader.md)

Handles loading and managing AI models used throughout EMScribe.

### [Prompt Manager](prompt_manager.md)

Manages prompts used by the AI models to clean, extract, and review transcripts.

### [Transcript Cleaner](transcript_cleaner.md)

Cleans and preprocesses transcripts to ensure accurate extraction of information.

### [Transcript Extractor](transcript_extractor.md)

Extracts detailed information from transcripts, including patient demographics, medical history, and chief complaints.

### [Narrative Manager](narrative_manager.md)

Generates comprehensive EMS narratives from the extracted information.

### [Extract Reviewer](extract_reviewer.md)

Reviews and refines the extracted information to ensure accuracy and completeness.

## 🛠️ CLI

EMScribe also includes a powerful command-line interface (CLI) to streamline interactions with the application.

### 📜 Commands

1. **`clean`**
   - Cleans the provided transcript.
   - Usage: `emscribe clean <transcript_path> [--output <output_path>]`
   - Default output: `data/cleaned_transcript.txt`

2. **`extract`**
   - Extracts information from the provided transcript.
   - Usage: `emscribe extract <transcript_path> [--output <output_path>]`
   - Default input: `data/cleaned_transcript.txt`
   - Default output: `data/extract.txt`

3. **`generate`**
   - Generates a narrative from the extracted data.
   - Usage: `emscribe generate <transcript_path> [--output <output_path>]`
   - Default input: `data/reviewed_extract.txt`
   - Default output: `data/narrative.txt`

4. **`review`**
   - Reviews the extracted information.
   - Usage: `emscribe review <extracted_data_path> [--output <output_path>]`
   - Default input: `data/extract.txt`
   - Default output: `data/reviewed_extract.txt`

### 🔧 Example Usage

```sh
# Clean a transcript
emscribe clean ./transcript.txt --output ./cleaned_transcript.txt

# Extract information from a transcript
emscribe extract ./cleaned_transcript.txt --output ./extracted_data.txt

# Generate a narrative from the extracted data
emscribe generate ./extracted_data.txt --output ./narrative.txt

# Review extracted information
emscribe review ./extracted_data.txt --output ./reviewed_extract.txt

# Using pipes to combine commands
emscribe clean ./transcript.txt | emscribe extract - | emscribe review - | emscribe generate - --output ./narrative.txt
```

## 🔍 Usage Examples

### Example 1: Cleaning a Transcript

Here’s a Python example of how to clean a transcript using the EMScribe API:

```python
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.prompt_manager import PromptManager

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

### Example 2: Extracting Information from a Transcript

Here’s a Python example of how to extract information from a transcript:

```python
from modules.model_loader import ModelLoader
from modules.transcript_extractor import TranscriptExtractor
from modules.prompt_manager import PromptManager

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

### Example 3: Generating an EMS Narrative

Here’s a Python example of how to generate an EMS narrative from extracted data:

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.narrative_manager import NarrativeManager

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(model_name="llama3.1")
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

# Example data extracted from a transcript
extracted_data = {
    "incident_info": "...",
    "patient_demographics": "John Doe, 45, Male",
    "patient_histories": "Hypertension, Diabetes",
    # other extracted data
}

# Generate an EMS narrative
narrative = narrative_manager.generate_narrative("presoaped_format", extracted_data)
print("Generated Narrative:")
print(narrative)
```

## 🎉 Conclusion

This API reference provides detailed information on the main modules and their functionalities in the EMScribe project. For more details on how to use these modules, refer to the usage examples and the rest of the documentation.

For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).