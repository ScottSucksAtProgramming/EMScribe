The provided `api_reference.md` looks comprehensive and well-structured. It covers all the major modules, their classes, methods, and attributes. Additionally, it provides usage examples to help users understand how to implement the functionalities. Below is the final version for `api_reference.md`:

```markdown
# API Reference

This document provides a comprehensive reference for the EMScribe 2.0 API, including details on the main modules, their classes, and methods.

## Modules

### 1. `model_loader`

The `model_loader` module contains the `ModelLoader` class, which is responsible for interacting with the AI model.

#### Class: `ModelLoader`

**Description:**
A class to handle the interaction with the AI model.

**Attributes:**
- `base_url (str)`: The base URL for the AI model server.
- `model_name (str)`: The name of the AI model to use.

**Methods:**

##### `__init__(self, base_url: str, model_name: str)`

**Description:**
Initializes the `ModelLoader` with the base URL and model name.

**Args:**
- `base_url (str)`: The base URL for the AI model server.
- `model_name (str)`: The name of the AI model to use.

##### `generate(self, prompt: str) -> str`

**Description:**
Generates a response from the AI model based on the provided prompt.

**Args:**
- `prompt (str)`: The prompt to send to the AI model.

**Returns:**
- `str`: The response generated by the AI model.

### 2. `prompt_manager`

The `prompt_manager` module contains the `PromptManager` class, which is responsible for managing and formatting prompts.

#### Class: `PromptManager`

**Description:**
A class to manage and format prompts for various tasks.

**Attributes:**
- `prompts (dict)`: A dictionary of predefined prompts.

**Methods:**

##### `__init__(self)`

**Description:**
Initializes the `PromptManager` with a dictionary of prompts.

##### `get_prompt(self, key: str, **kwargs) -> str`

**Description:**
Returns a formatted prompt based on the key and provided keyword arguments.

**Args:**
- `key (str)`: The key for the desired prompt.
- `**kwargs`: Keyword arguments to format the prompt.

**Returns:**
- `str`: The formatted prompt.

### 3. `transcript_cleaner`

The `transcript_cleaner` module contains the `TranscriptCleaner` class, which is responsible for cleaning up EMS transcripts.

#### Class: `TranscriptCleaner`

**Description:**
A class to clean up an EMS transcript using an AI model.

**Attributes:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

**Methods:**

##### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `TranscriptCleaner` with a `ModelLoader` and `PromptManager` instance.

**Args:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

##### `clean(self, transcript: str) -> str`

**Description:**
Cleans the transcript using the specified prompt.

**Args:**
- `transcript (str)`: The transcript to clean.

**Returns:**
- `str`: The cleaned transcript.

### 4. `transcript_extractor`

The `transcript_extractor` module contains the `TranscriptExtractor` class, which is responsible for extracting information from EMS transcripts.

#### Class: `TranscriptExtractor`

**Description:**
A class to extract information from an EMS transcript using an AI model.

**Attributes:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

**Methods:**

##### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `TranscriptExtractor` with a `ModelLoader` and `PromptManager` instance.

**Args:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

##### `extract(self, transcript: str) -> str`

**Description:**
Extracts information from the transcript using the specified prompts.

**Args:**
- `transcript (str)`: The transcript to extract information from.

**Returns:**
- `str`: A string containing the extracted information.

### 5. `narrative_manager`

The `narrative_manager` module contains the `NarrativeManager` class, which is responsible for generating EMS narratives from extracted data.

#### Class: `NarrativeManager`

**Description:**
A class to generate EMS narratives using extracted data and an AI model.

**Attributes:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

**Methods:**

##### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `NarrativeManager` with a `ModelLoader` and `PromptManager` instance.

**Args:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

##### `generate_narrative(self, narrative_format: str, data: str) -> str`

**Description:**
Generates an EMS narrative based on the provided narrative format and extracted data.

**Args:**
- `narrative_format (str)`: The format to use for the narrative.
- `data (str)`: The extracted data to include in the narrative.

**Returns:**
- `str`: The generated EMS narrative.

## Usage Examples

### Example 1: Cleaning a Transcript

```python
from modules.model_loader import ModelLoader
from modules.transcript_cleaner import TranscriptCleaner
from modules.prompt_manager import PromptManager

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

### Example 2: Extracting Information from a Transcript

```python
from modules.model_loader import ModelLoader
from modules.transcript_extractor import TranscriptExtractor
from modules.prompt_manager import PromptManager

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

# Extract information from a transcript
example_transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
extracted_data = extractor.extract(example_transcript)
print("Extracted Information:")
print(extracted_data)
```

### Example 3: Generating an EMS Narrative

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.narrative_manager import NarrativeManager

# Initialize components
prompt_manager = PromptManager()
model_loader = ModelLoader(base_url="http://localhost:11434", model_name="llama3.1")
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

# Example data extracted from a transcript
extracted_data = """
incident_info: ...
patient_demographics: John Doe, 45, Male
patient_histories: Hypertension, Diabetes
...
"""

# Generate an EMS narrative
narrative = narrative_manager.generate_narrative("presoaped_format", extracted_data)
print("Generated Narrative:")
print(narrative)
```

## Conclusion

This API reference provides detailed information on the main modules and their functionalities in the EMScribe 2.0 project. For more details on how to use these modules, refer to the usage examples and the rest of the documentation.

For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).
```

This document should now provide clear and detailed information about the API and how to use it effectively.