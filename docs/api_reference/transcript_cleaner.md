# Transcript Cleaner

The `transcript_cleaner` module contains the `TranscriptCleaner` class, which is responsible for cleaning up EMS transcripts.

## Class: `TranscriptCleaner`

**Description:**
A class to clean up an EMS transcript using an AI model.

### Attributes:
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

### Methods:

#### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `TranscriptCleaner` with a `ModelLoader` and `PromptManager` instance.

**Args:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

#### `clean(self, transcript: str) -> str`

**Description:**
Cleans the transcript using the specified prompt.

**Args:**
- `transcript (str)`: The transcript to clean.

**Returns:**
- `str`: The cleaned transcript.
```
