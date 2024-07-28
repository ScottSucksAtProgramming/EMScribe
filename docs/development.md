# Development

This guide provides an overview of the development process for EMScribe 2.0, including setting up the development environment, adding new features, and writing tests.

## Setting Up the Development Environment

### Prerequisites

- Python 3.8 or higher
- Virtual Environment (venv)
- Ollama (running locally)
- VS Code (or any IDE)
- Git

### Installation

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd emscribe
    ```

2. **Set Up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Ollama:**

    Ensure Ollama is running locally and accessible at `http://localhost:11434`.

## Project Structure

```plaintext
emscribe/
├── docs/
│   ├── api_reference.md
│   ├── contributing.md
│   ├── development.md
│   ├── index.md
│   ├── installation.md
│   └── usage.md
├── modules/
│   ├── __init__.py
│   ├── model_loader.py
│   ├── prompt_manager.py
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── cleaning_prompts.py
│   │   ├── extraction_prompts.py
│   └── transcript_cleaner.py
│   └── transcript_extractor.py
├── scripts/
│   ├── __init__.py
│   ├── extraction.py
│   ├── main.py
│   ├── preprocess.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_model_loader.py
│   ├── test_transcript_cleaner.py
│   └── test_transcript_extractor.py
├── README.md
├── requirements.txt
├── setup.py
└── venv/
```

## Running Tests

To run all tests, use the following command:

```bash
pytest
```

Ensure all tests pass before submitting your pull request.

## Debugging

Use the built-in debugging tools in your IDE (e.g., VS Code) to set breakpoints and inspect variables. You can also use print statements for simple debugging.

## Conclusion

Following these guidelines will help maintain the quality and consistency of the EMScribe 2.0 codebase. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).