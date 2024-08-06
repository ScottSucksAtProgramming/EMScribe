# Transcript Extractor

The `transcript_extractor` module contains the `TranscriptExtractor` class, which is responsible for extracting information from EMS transcripts.

## Class: `TranscriptExtractor`

**Description:**
A class to extract information from an EMS transcript using an AI model.

### Attributes:
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

### Methods:

#### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `TranscriptExtractor` with a `ModelLoader` and `PromptManager` instance.

**Args:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

#### `extract(self, transcript: str) -> str`

**Description:**
Extracts information from the transcript using the specified prompts.

**Args:**
- `transcript (str)`: The transcript to extract information from.

**Returns:**
- `str`: A string containing the extracted information.
