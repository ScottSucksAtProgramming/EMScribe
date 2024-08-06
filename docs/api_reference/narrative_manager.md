# 🚀 Extract Reviewer

Welcome to the Extract Reviewer module documentation! The `ExtractReviewer` class is essential for reviewing and refining extracted information, ensuring its accuracy and completeness. This guide provides detailed information about its attributes, methods, and usage examples.

## 📚 Class: `ExtractReviewer`

### **Description:**
The `ExtractReviewer` class is responsible for reviewing and refining the extracted information from EMS transcripts. It leverages the `ModelLoader` and `PromptManager` classes to interact with the AI model and manage prompts effectively.

### 🏗️ Attributes:

- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

### 🚀 Methods:

#### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `ExtractReviewer` with a `ModelLoader` and `PromptManager` instance.

**Parameters:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

**Example:**

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.extract_reviewer import ExtractReviewer

# Initialize ModelLoader and PromptManager
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"review": "Review and refine the following information: {info}"})

# Initialize ExtractReviewer
reviewer = ExtractReviewer(model_loader=model_loader, prompt_manager=prompt_manager)
```

#### `review_section(self, section: str, user_input: Optional[str] = None) -> str`

**Description:**
Reviews a section of extracted data using the AI model.

**Parameters:**
- `section (str)`: The section of extracted data to review.
- `user_input (Optional[str])`: The user's input for modifications, if any.

**Returns:**
- `str`: The AI model's response.

**Example:**

```python
section = "Incident Information\n- Unit: [No Info]\n- Response Mode: emergent\n..."
reviewed_section = reviewer.review_section(section)
print("Reviewed Section:")
print(reviewed_section)
```

#### `final_review(self, updated_section: str) -> str`

**Description:**
Performs a final review of a section after changes have been made.

**Parameters:**
- `updated_section (str)`: The section of data after user modifications.

**Returns:**
- `str`: The AI model's response after final review.

**Example:**

```python
updated_section = "Incident Information\n- Unit: 123\n- Response Mode: emergent\n..."
final_reviewed_section = reviewer.final_review(updated_section)
print("Final Reviewed Section:")
print(final_reviewed_section)
```

#### `_get_review_prompt(self, prompt_key: str, section: str, user_input: Optional[str] = None) -> str`

**Description:**
Retrieves and formats the review prompt.

**Parameters:**
- `prompt_key (str)`: The key for the review prompt.
- `section (str)`: The section of extracted data.
- `user_input (Optional[str])`: The user's input for modifications, if any.

**Returns:**
- `str`: The formatted review prompt.

**Example:**

```python
prompt_key = "review"
section = "Incident Information\n- Unit: [No Info]\n- Response Mode: emergent\n..."
user_input = "Unit: 123"
formatted_prompt = reviewer._get_review_prompt(prompt_key, section, user_input)
print("Formatted Prompt:")
print(formatted_prompt)
```

#### `_generate_response(self, prompt: str) -> str`

**Description:**
Generates a response from the AI model based on the provided prompt.

**Parameters:**
- `prompt (str)`: The input prompt for the model.

**Returns:**
- `str`: The AI model's response.

**Example:**

```python
prompt = "Review and refine the following information: Incident Information\n- Unit: 123\n- Response Mode: emergent\n..."
response = reviewer._generate_response(prompt)
print("Generated Response:")
print(response)
```

## 🌟 Usage Examples

### Example 1: Initializing the ExtractReviewer

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.extract_reviewer import ExtractReviewer

# Initialize ModelLoader with a specific model name
model_loader = ModelLoader(model_name="llama3.1")

# Initialize PromptManager with predefined prompts
prompts = {
    "review": "Review and refine the following information: {info}"
}
prompt_manager = PromptManager(prompts=prompts, context_window_size=32000)

# Initialize ExtractReviewer
reviewer = ExtractReviewer(model_loader=model_loader, prompt_manager=prompt_manager)
```

### Example 2: Reviewing a Section of Extracted Data

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.extract_reviewer import ExtractReviewer

# Initialize components
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"review": "Review and refine the following information: {info}"})
reviewer = ExtractReviewer(model_loader=model_loader, prompt_manager=prompt_manager)

# Review a section of extracted data
section = "Incident Information\n- Unit: [No Info]\n- Response Mode: emergent\n..."
reviewed_section = reviewer.review_section(section)
print("Reviewed Section:")
print(reviewed_section)
```

### Example 3: Performing a Final Review of a Section

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.extract_reviewer import ExtractReviewer

# Initialize components
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"review": "Review and refine the following information: {info}"})
reviewer = ExtractReviewer(model_loader=model_loader, prompt_manager=prompt_manager)

# Perform a final review of a section after user modifications
updated_section = "Incident Information\n- Unit: 123\n- Response Mode: emergent\n..."
final_reviewed_section = reviewer.final_review(updated_section)
print("Final Reviewed Section:")
print(final_reviewed_section)
```

## 🎉 Conclusion

The `ExtractReviewer` class is an essential tool for reviewing and refining extracted information, ensuring its accuracy and completeness. By understanding its attributes and methods, you can effectively improve the quality of extracted data in EMS documentation. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).