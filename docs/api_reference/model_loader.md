# Model Loader

The `model_loader` module contains the `ModelLoader` class, which is responsible for interacting with the AI model.

## Class: `ModelLoader`

**Description:**
A class to handle the interaction with the AI model.

### Attributes:
- `model_name (str)`: The name of the AI model to use.
- `base_url (str)`: The base URL of the model API.
- `context_window (int)`: The maximum context window size for the model.
- `client (Ollama)`: An instance of the Ollama client to communicate with the AI model.

### Methods:

#### `__init__(self, model_name: str, client: Optional[Ollama] = None, base_url: str = "http://localhost:11434")`

**Description:**
Initializes the `ModelLoader` with the specified model name and base URL.

**Args:**
- `model_name (str)`: The name of the model to use.
- `client (Optional[Ollama])`: An instance of the Ollama client. Defaults to None.
- `base_url (str)`: The base URL of the model API.

#### `_get_options(self) -> Dict[str, int]`

**Description:**
Constructs the options for the model prompt.

**Returns:**
- `dict`: The options for the model prompt.

#### `generate(self, prompt: str) -> str`

**Description:**
Generates a response from the AI model based on the provided prompt and context window.

**Args:**
- `prompt (str)`: The input prompt for the model.

**Returns:**
- `str`: The generated response from the model.
