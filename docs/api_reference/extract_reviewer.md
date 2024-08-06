# Extract Reviewer

The `extract_reviewer` module contains the `ExtractReviewer` class, which is responsible for reviewing and refining extracted information.

## Class: `ExtractReviewer`

**Description:**
A class to review and refine the extracted data.

### Attributes:
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

### Methods:

#### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `ExtractReviewer` with a `ModelLoader` and `PromptManager` instance.

**Args:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

#### `review_section(self, section: str, user_input: str = None) -> str`

**Description:**
Reviews a section of extracted data using the AI model.

**Args:**
- `section (str)`: The section of extracted data to review.
- `user_input (str)`: The user's input for modifications (optional).

**Returns:**
- `str`: The AI model's response.

#### `final_review(self, updated_section: str) -> str`

**Description:**
Performs a final review of a section after changes have been made.

**Args:**
- `updated_section (str)`: The section of data after user modifications.

**Returns:**
- `str`: The AI model's response after final review.
```


