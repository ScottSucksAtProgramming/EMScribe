Your `development.md` document is quite comprehensive. Here are some suggested updates to keep it aligned with the README and enhance clarity:

1. Add emojis to make it more engaging.
2. Update the repository URL to a placeholder or actual URL.
3. Include the information about contacting for contributions.
4. Reflect any changes discussed, such as licensing and documentation links.

Here's the updated `development.md`:

```markdown
# Development 🛠️

This guide provides an overview of the development process for EMScribe 2.0, including setting up the development environment, adding new features, and writing tests.

## Setting Up the Development Environment 🖥️

### Prerequisites 📋

- Python 3.8 or higher 🐍
- Virtual Environment (venv) 🌐
- [Ollama](https://github.com/ollama/ollama) (running locally) 🦙
- VS Code (or any IDE) 🖥️
- Git 🌲

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ScottSucksAtProgramming/EMScribe.git
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

4. **Configure [Ollama](https://github.com/ollama/ollama):**

    Ensure Ollama is running locally and accessible at `http://localhost:11434`.

## Project Structure 🗂️

```plaintext
.
|-- README.md
|-- bin
|   `-- emscribe
|-- commands
|   |-- clean_command.py
|   |-- extract_command.py
|   |-- generate_command.py
|   `-- review_command.py
|-- data
|   |-- cleaned_transcript.txt
|   |-- extract.txt
|   |-- narrative.txt
|   `-- reviewed_extract.txt
|-- docs
|   |-- api_reference.md
|   |-- contributing.md
|   |-- development.md
|   |-- index.md
|   |-- installation.md
|   `-- usage.md
|-- images
|   `-- emscribe_logo.png
|-- modules
|   |-- extract_reviewer.py
|   |-- model_loader.py
|   |-- narrative_manager.py
|   |-- prompt_manager.py
|   |-- prompts
|   |   |-- cleaning_prompts.py
|   |   |-- extraction_prompts.py
|   |   |-- narrative_prompts.py
|   |   `-- review_prompts.py
|   |-- transcript_cleaner.py
|   `-- transcript_extractor.py
|-- requirements.txt
|-- scripts
|   |-- cli.py
|   |-- data
|   |   |-- cleaned_transcript.txt
|   |   `-- extract.txt
|   |-- extraction.py
|   |-- main.py
|   `-- preprocess.py
|-- tests
|   |-- conftest.py
|   |-- test_cli.py
|   |-- test_model_loader.py
|   |-- test_review_command.py
|   |-- test_transcript_cleaner.py
|   `-- test_transcript_extractor.py
|-- transcript.txt
`-- venv
```

## Adding New Features ✨

### Create a New Branch 🌿

Create a new branch for your feature:

```bash
git checkout -b feature/your-feature-name
```

### Make Changes 🔧

Implement your feature in the appropriate module or create new modules as needed. Ensure your code follows the project's coding standards.

### Write Tests 🧪

Write tests for your new feature in the `tests` directory. Ensure each test covers different scenarios and edge cases. Use `pytest` for testing.

### Commit Changes 💾

Commit your changes with a clear and concise commit message:

```bash
git add .
git commit -m "Add feature: your feature description"
```

### Push the Branch and Create a Pull Request 🔄

Push your branch to the remote repository and create a pull request:

```bash
git push origin feature/your-feature-name
```

## Running Tests 🏃‍♂️

To run all tests, use the following command:

```bash
pytest
```

Ensure all tests pass before submitting your pull request.

## Debugging 🐞

Use the built-in debugging tools in your IDE (e.g., VS Code) to set breakpoints and inspect variables. You can also use print statements for simple debugging.

## Contribution Guidelines 🤝

### Code Style 📏

- Follow PEP 8 for Python code style.
- Write clear, concise, and descriptive variable and function names.
- Include docstrings for all modules, classes, and functions.

### Commit Messages 📝

- Use the imperative mood in the subject line.
- Capitalize the first letter of the subject line.
- Keep the subject line to 50 characters or less.
- Use the body to explain what and why vs. how.

### Pull Requests 🚀

- Provide a clear and detailed description of the changes in the pull request.
- Link to any relevant issues.
- Ensure all tests pass and there are no conflicts with the base branch.

## Documentation 📚

Ensure your new features are well-documented. Update or add new documentation files in the `docs` directory as needed. Follow the existing documentation structure and style.

## Conclusion 🎯

Following these guidelines will help maintain the quality and consistency of the EMScribe 2.0 codebase. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).

---

If you're not currently looking for contributors but want to allow inquiries, you can add this section at the end of the document:

---

## Contributions

At this time, we are not actively seeking contributors. However, if you are interested in contributing or have ideas, feel free to contact us through [GitHub](https://github.com/ScottSucksAtProgramming). Your interest is appreciated!
```

This updated document should now match the tone and style of your README. If you need any further adjustments or additions, feel free to let me know!
