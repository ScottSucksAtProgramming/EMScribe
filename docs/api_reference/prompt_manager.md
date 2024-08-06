# Prompt Manager

The `prompt_manager` module contains the `PromptManager` class, which is responsible for managing and formatting prompts.

## Class: `PromptManager`

**Description:**
A class to manage and format prompts for various tasks such as extraction, cleaning, narrative generation, and quality control.

### Attributes:
- `prompts (Dict[str, Union[str, Dict[str, str]]])`: A dictionary of predefined prompts.
- `context_window_size (int)`: The maximum context window size for the prompts.

### Methods:

#### `__init__(self, prompts: Dict[str, Union[str, Dict[str, str]]] = None, context_window_size: int = 32000)`

**Description:**
Initializes the `PromptManager` with a dictionary of prompts and a context window size.

**Args:**
- `prompts (Dict[str, Union[str, Dict[str, str]]], optional)`: A dictionary of prompts. Defaults to None.
- `context_window_size (int)`: The maximum context window size for the prompts.

#### `get_prompt(self, key: str, **kwargs: Any) -> Union[str, Dict[str, str], list[str]]`

**Description:**
Retrieves a prompt template and formats it with the provided keyword arguments.

**Args:**
- `key (str)`: The key for the prompt template.
- `**kwargs`: Keyword arguments to format the template.

**Returns:**
- `Union[str, Dict[str, str], list[str]]`: The formatted prompt.

**Raises:**
- `KeyError`: If no prompt is found for the given key.
