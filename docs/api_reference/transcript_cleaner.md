# 🚀 Transcript Cleaner

Welcome to the Transcript Cleaner module documentation! The `TranscriptCleaner` class is a key component for preprocessing EMS transcripts to ensure accurate information extraction. This guide provides detailed information about its attributes, methods, and usage examples.

## 📚 Class: `TranscriptCleaner`

### **Description:**
The `TranscriptCleaner` class is responsible for cleaning up EMS transcripts using an AI model. It utilizes the `ModelLoader` and `PromptManager` classes to interact with the AI model and manage prompts effectively.

### 🏗️ Attributes:

- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

### 🚀 Methods:

#### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `TranscriptCleaner` with a `ModelLoader` and `PromptManager` instance.

**Parameters:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

**Example:**

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner

# Initialize ModelLoader and PromptManager
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"clean": "Clean the following text: {text}"})

# Initialize TranscriptCleaner
cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)
```

#### `clean(self, transcript: str) -> str`

**Description:**
Cleans the transcript using specified prompts.

**Parameters:**
- `transcript (str)`: The transcript to clean.

**Returns:**
- `str`: The cleaned transcript.

**Example:**

```python
transcript = "Patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
cleaned_transcript = cleaner.clean(transcript)
print("Cleaned Transcript:")
print(cleaned_transcript)
```

#### `_generate_cleaned_transcript(self, prompt: Union[str, list[str]]) -> str`

**Description:**
Generates the cleaned transcript based on the provided prompt.

**Parameters:**
- `prompt (Union[str, list[str]])`: The input prompt for the model.

**Returns:**
- `str`: The cleaned transcript.

**Example:**

```python
prompt = "Clean the following text: Patient is experiencing shortness of breath. The patient is also complaining of chest pain."
cleaned_transcript = cleaner._generate_cleaned_transcript(prompt)
print("Generated Cleaned Transcript:")
print(cleaned_transcript)
```

## 🌟 Usage Examples

### Example 1: Initializing the TranscriptCleaner

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner

# Initialize ModelLoader with a specific model name
model_loader = ModelLoader(model_name="llama3.1")

# Initialize PromptManager with predefined prompts
prompts = {
    "clean": "Clean the following text: {text}"
}
prompt_manager = PromptManager(prompts=prompts, context_window_size=32000)

# Initialize TranscriptCleaner
cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)
```

### Example 2: Cleaning a Transcript

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner

# Initialize components
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"clean": "Clean the following text: {text}"})
cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)

# Clean a transcript
transcript = "Patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
cleaned_transcript = cleaner.clean(transcript)
print("Cleaned Transcript:")
print(cleaned_transcript)
```

### Example 3: Generating a Cleaned Transcript

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_cleaner import TranscriptCleaner

# Initialize components
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"clean": "Clean the following text: {text}"})
cleaner = TranscriptCleaner(model_loader=model_loader, prompt_manager=prompt_manager)

# Generate a cleaned transcript from a prompt
prompt = "Clean the following text: Patient is experiencing shortness of breath. The patient is also complaining of chest pain."
cleaned_transcript = cleaner._generate_cleaned_transcript(prompt)
print("Generated Cleaned Transcript:")
print(cleaned_transcript)
```

## 🎉 Conclusion

The `TranscriptCleaner` class is an essential tool for preprocessing EMS transcripts, ensuring accurate information extraction. By understanding its attributes and methods, you can effectively clean transcripts and improve the overall accuracy of EMS documentation. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).