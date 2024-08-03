# Prompt Manager

The `prompt_manager` module contains the `PromptManager` class, which is responsible for managing and formatting prompts.

## Class: `PromptManager`

### Description:
A class to manage and format prompts for various tasks.

### Attributes:
- `prompts (dict)`: A dictionary of predefined prompts.

### Methods:

#### `__init__(self)`

**Description:**
Initializes the `PromptManager` with a dictionary of prompts.

#### `get_prompt(self, key: str, **kwargs) -> str`

**Description:**
Returns a formatted prompt based on the key and provided keyword arguments.

**Args:**
- `key (str)`: The key for the desired prompt.
- `**kwargs`: Keyword arguments to format the prompt.

**Returns:**
- `str`: The formatted prompt.
