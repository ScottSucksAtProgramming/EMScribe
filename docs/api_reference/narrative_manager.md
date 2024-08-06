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

#### `generate_narrative(self, narrative_format: str, data: dict) -> str`

**Description:**
Generates an EMS narrative based on the provided narrative format and extracted data.

**Args:**
- `narrative_format (str)`: The format to use for the narrative.
- `data (dict)`: The extracted data to include in the narrative.

**Returns:**
- `str`: The generated EMS narrative.
```


