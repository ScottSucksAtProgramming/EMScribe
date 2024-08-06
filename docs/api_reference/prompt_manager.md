# 🚀 Prompt Manager

Welcome to the Prompt Manager module documentation! The `PromptManager` class is essential for managing and formatting prompts used across various EMScribe tasks such as extraction, cleaning, narrative generation, and quality control. This guide will provide detailed information about its attributes, methods, and usage examples.

## 📚 Class: `PromptManager`

### **Description:**
The `PromptManager` class is responsible for managing and formatting prompts for various tasks in EMScribe. It ensures that prompts are appropriately tailored for each specific function.

### 🏗️ Attributes:

- `prompts (Dict[str, Union[str, Dict[str, str]]])`: A dictionary of predefined prompts.
- `context_window_size (int)`: The maximum context window size for the prompts.

### 🚀 Methods:

#### `__init__(self, prompts: Dict[str, Union[str, Dict[str, str]]] = None, context_window_size: int = 32000)`

**Description:**
Initializes the `PromptManager` with a dictionary of prompts and a context window size.

**Parameters:**
- `prompts (Dict[str, Union[str, Dict[str, str]]], optional)`: A dictionary of prompts. Defaults to None.
- `context_window_size (int)`: The maximum context window size for the prompts.

**Example:**

```python
from modules.prompt_manager import PromptManager

# Initialize PromptManager
prompts = {
    "clean": "Clean the following text: {text}",
    "extract": "Extract information from the following text: {text}",
    # Add more prompts as needed
}
prompt_manager = PromptManager(prompts=prompts, context_window_size=32000)
```

#### `get_prompt(self, key: str, **kwargs: Any) -> Union[str, Dict[str, str], list[str]]`

**Description:**
Retrieves a prompt template and formats it with the provided keyword arguments.

**Parameters:**
- `key (str)`: The key for the prompt template.
- `**kwargs`: Keyword arguments to format the template.

**Returns:**
- `Union[str, Dict[str, str], list[str]]`: The formatted prompt.

**Raises:**
- `KeyError`: If no prompt is found for the given key.

**Example:**

```python
# Retrieve and format a prompt
formatted_prompt = prompt_manager.get_prompt("clean", text="Patient John Doe, 45 years old, male.")
print(formatted_prompt)
```

## 🌟 Usage Examples

### Example 1: Initializing the PromptManager

```python
from modules.prompt_manager import PromptManager

# Initialize PromptManager with predefined prompts
prompts = {
    "clean": "Clean the following text: {text}",
    "extract": "Extract information from the following text: {text}",
    "generate_narrative": "Generate a narrative from the following information: {info}",
}
prompt_manager = PromptManager(prompts=prompts, context_window_size=32000)
```

### Example 2: Formatting a Prompt

```python
from modules.prompt_manager import PromptManager

# Initialize PromptManager
prompts = {
    "clean": "Clean the following text: {text}",
}
prompt_manager = PromptManager(prompts=prompts, context_window_size=32000)

# Format a prompt
text_to_clean = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours."
formatted_prompt = prompt_manager.get_prompt("clean", text=text_to_clean)
print("Formatted Prompt:")
print(formatted_prompt)
```

### Example 3: Handling Multiple Prompts

```python
from modules.prompt_manager import PromptManager

# Initialize PromptManager with multiple prompts
prompts = {
    "clean": "Clean the following text: {text}",
    "extract": "Extract information from the following text: {text}",
}
prompt_manager = PromptManager(prompts=prompts, context_window_size=32000)

# Retrieve and format prompts
clean_prompt = prompt_manager.get_prompt("clean", text="Sample text to clean.")
extract_prompt = prompt_manager.get_prompt("extract", text="Sample text to extract information from.")
print("Clean Prompt:")
print(clean_prompt)
print("Extract Prompt:")
print(extract_prompt)
```

## 🎉 Conclusion

The `PromptManager` class is a versatile and essential component of EMScribe, ensuring that prompts are effectively managed and formatted for various tasks. By understanding its attributes and methods, you can enhance the functionality of EMScribe in your projects. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).