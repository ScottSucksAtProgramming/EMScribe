# 🚀 Model Loader

Welcome to the Model Loader module documentation! The `ModelLoader` class is the heart of EMScribe's interaction with the AI model. This guide will walk you through its attributes, methods, and usage, ensuring you have all the details you need to harness its power.

## 📚 Class: `ModelLoader`

### **Description:**
The `ModelLoader` class handles the interaction with the AI model, facilitating communication and response generation.

### 🏗️ Attributes:

- `model_name (str)`: The name of the AI model to use.
- `base_url (str)`: The base URL of the model API. Defaults to `"http://localhost:11434"`.
- `context_window (int)`: The maximum context window size for the model.
- `client (Ollama)`: An instance of the Ollama client to communicate with the AI model.

### 🚀 Methods:

#### `__init__(self, model_name: str, client: Optional[Ollama] = None, base_url: str = "http://localhost:11434")`

**Description:**
Initializes the `ModelLoader` with the specified model name and base URL.

**Parameters:**
- `model_name (str)`: The name of the model to use.
- `client (Optional[Ollama])`: An instance of the Ollama client. Defaults to None.
- `base_url (str)`: The base URL of the model API. Defaults to `"http://localhost:11434"`.

**Example:**

```python
from modules.model_loader import ModelLoader

# Initialize ModelLoader
model_loader = ModelLoader(model_name="llama3.1")
```

#### `_get_options(self) -> Dict[str, int]`

**Description:**
Constructs the options for the model prompt.

**Returns:**
- `dict`: The options for the model prompt.

**Example:**

```python
options = model_loader._get_options()
print(options)  # Output: {'context_window': 2048}
```

#### `generate(self, prompt: str) -> str`

**Description:**
Generates a response from the AI model based on the provided prompt and context window.

**Parameters:**
- `prompt (str)`: The input prompt for the model.

**Returns:**
- `str`: The generated response from the model.

**Example:**

```python
prompt = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours."
response = model_loader.generate(prompt)
print(response)  # Output: Generated response from the model
```

## 🌟 Usage Examples

### Example 1: Initializing the ModelLoader

```python
from modules.model_loader import ModelLoader

# Initialize ModelLoader with a specific model name
model_loader = ModelLoader(model_name="llama3.1")
```

### Example 2: Generating a Response

```python
from modules.model_loader import ModelLoader

# Initialize ModelLoader
model_loader = ModelLoader(model_name="llama3.1")

# Define a prompt
prompt = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours."

# Generate a response
response = model_loader.generate(prompt)
print("Generated Response:")
print(response)
```

### Example 3: Custom Client and Base URL

```python
from modules.model_loader import ModelLoader
from ollama import Ollama

# Initialize a custom Ollama client
custom_client = Ollama(base_url="http://localhost:11434")

# Initialize ModelLoader with custom client and base URL
model_loader = ModelLoader(model_name="llama3.1", client=custom_client, base_url="http://localhost:11434")

# Generate a response
prompt = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours."
response = model_loader.generate(prompt)
print("Generated Response with Custom Client:")
print(response)
```

## 🎉 Conclusion

The `ModelLoader` class is a powerful tool for interacting with the AI model in EMScribe. By understanding its attributes and methods, you can effectively integrate AI capabilities into your EMS documentation workflow. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).