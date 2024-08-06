# 🚀 Transcript Extractor

Welcome to the Transcript Extractor module documentation! The `TranscriptExtractor` class is essential for extracting detailed information from EMS transcripts. This guide provides detailed information about its attributes, methods, and usage examples.

## 📚 Class: `TranscriptExtractor`

### **Description:**
The `TranscriptExtractor` class is responsible for extracting detailed information from EMS transcripts using an AI model. It utilizes the `ModelLoader` and `PromptManager` classes to interact with the AI model and manage prompts effectively.

### 🏗️ Attributes:

- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

### 🚀 Methods:

#### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `TranscriptExtractor` with a `ModelLoader` and `PromptManager` instance.

**Parameters:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

**Example:**

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor

# Initialize ModelLoader and PromptManager
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"extract": "Extract information from the following text: {text}"})

# Initialize TranscriptExtractor
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)
```

#### `extract(self, transcript: str) -> str`

**Description:**
Extracts information from the transcript using specified prompts.

**Parameters:**
- `transcript (str)`: The transcript to extract information from.

**Returns:**
- `str`: A string containing the extracted information.

**Example:**

```python
transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
extracted_info = extractor.extract(transcript)
print("Extracted Information:")
print(extracted_info)
```

## 🌟 Usage Examples

### Example 1: Initializing the TranscriptExtractor

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor

# Initialize ModelLoader with a specific model name
model_loader = ModelLoader(model_name="llama3.1")

# Initialize PromptManager with predefined prompts
prompts = {
    "extract": "Extract information from the following text: {text}"
}
prompt_manager = PromptManager(prompts=prompts, context_window_size=32000)

# Initialize TranscriptExtractor
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)
```

### Example 2: Extracting Information from a Transcript

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.transcript_extractor import TranscriptExtractor

# Initialize components
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"extract": "Extract information from the following text: {text}"})
extractor = TranscriptExtractor(model_loader=model_loader, prompt_manager=prompt_manager)

# Extract information from a transcript
transcript = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
extracted_info = extractor.extract(transcript)
print("Extracted Information:")
print(extracted_info)
```

## 🎉 Conclusion

The `TranscriptExtractor` class is an essential tool for extracting detailed information from EMS transcripts. By understanding its attributes and methods, you can effectively extract critical data and improve the overall accuracy of EMS documentation. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).