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

#### `review_section(self, section: str, user_input: Optional[str] = None) -> str`

**Description:**
Reviews a section of extracted data using the AI model.

**Args:**
- `section (str)`: The section of extracted data to review.
- `user_input (Optional[str])`: The user's input for modifications, if any.

**Returns:**
- `str`: The AI model's response.

#### `final_review(self, updated_section: str) -> str`

**Description:**
Performs a final review of a section after changes have been made.

**Args:**
- `updated_section (str)`: The section of data after user modifications.

**Returns:**
- `str`: The AI model's response after final review.

#### `_get_review_prompt(self, prompt_key: str, section: str, user_input: Optional[str] = None) -> str`

**Description:**
Retrieves and formats the review prompt.

**Args:**
- `prompt_key (str)`: The key for the review prompt.
- `section (str)`: The section of extracted data.
- `user_input (Optional[str])`: The user's input for modifications, if any.

**Returns:**
- `str`: The formatted review prompt.

#### `_generate_response(self, prompt: str) -> str`

**Description:**
Generates a response from the AI model based on the provided prompt.

**Args:**
- `prompt (str)`: The input prompt for the model.

**Returns:**
- `str`: The AI model's response.
