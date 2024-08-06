# Narrative Manager

The `narrative_manager` module contains the `NarrativeManager` class, which is responsible for generating EMS narratives from extracted data.

## Class: `NarrativeManager`

**Description:**
A class to generate EMS narratives using extracted data and an AI model.

### Attributes:
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

### Methods:

#### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `NarrativeManager` with a `ModelLoader` and `PromptManager` instance.

**Args:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

#### `generate_narrative(self, narrative_format: str, data: Dict) -> str`

**Description:**
Generates a narrative based on the specified format and data.

**Args:**
- `narrative_format (str)`: The key for the desired narrative format.
- `data (Dict)`: The extracted information in a dictionary.

**Returns:**
- `str`: The generated narrative.

#### `_generate_response(self, prompt: str) -> str`

**Description:**
Generates a response from the AI model based on the provided prompt.

**Args:**
- `prompt (str)`: The input prompt for the model.

**Returns:**
- `str`: The AI model's response.
