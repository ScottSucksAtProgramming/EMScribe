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
│   │   ├── narrative_prompts.py
│   ├── transcript_cleaner.py
│   ├── transcript_extractor.py
│   ├── narrative_manager.py
├── scripts/
│   ├── __init__.py
│   ├── cli.py
│   ├── extraction.py
│   ├── main.py
│   ├── preprocess.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_model_loader.py
│   ├── test_transcript_cleaner.py
│   ├── test_transcript_extractor.py
│   ├── test_cli.py
├── README.md
├── requirements.txt
├── setup.py
└── venv/
```

## Adding New Features

### Create a New Branch

Create a new branch for your feature:

```bash
git checkout -b feature/your-feature-name
```

### Make Changes

Implement your feature in the appropriate module or create new modules as needed. Ensure your code follows the project's coding standards.

### Write Tests

Write tests for your new feature in the `tests` directory. Ensure each test covers different scenarios and edge cases. Use `pytest` for testing.

### Commit Changes

Commit your changes with a clear and concise commit message:

```bash
git add .
git commit -m "Add feature: your feature description"
```

### Push the Branch and Create a Pull Request

Push your branch to the remote repository and create a pull request:

```bash
git push origin feature/your-feature-name
```

## Running Tests

To run all tests, use the following command:

```bash
pytest
```

Ensure all tests pass before submitting your pull request.

## Debugging

Use the built-in debugging tools in your IDE (e.g., VS Code) to set breakpoints and inspect variables. You can also use print statements for simple debugging.

## Contribution Guidelines

### Code Style

- Follow PEP 8 for Python code style.
- Write clear, concise, and descriptive variable and function names.
- Include docstrings for all modules, classes, and functions.

### Commit Messages

- Use the imperative mood in the subject line.
- Capitalize the first letter of the subject line.
- Keep the subject line to 50 characters or less.
- Use the body to explain what and why vs. how.

### Pull Requests

- Provide a clear and detailed description of the changes in the pull request.
- Link to any relevant issues.
- Ensure all tests pass and there are no conflicts with the base branch.

## Documentation

Ensure your new features are well-documented. Update or add new documentation files in the `docs` directory as needed. Follow the existing documentation structure and style.

## Conclusion

Following these guidelines will help maintain the quality and consistency of the EMScribe 2.0 codebase. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).
