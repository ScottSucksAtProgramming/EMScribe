# 🛠️ Installation Guide

Welcome to the EMScribe installation guide! Follow these steps to set up EMScribe on your local machine and start crafting comprehensive EMS narratives with ease.

## 📋 Prerequisites

Before you begin, make sure you have the following:

- Python 3.8 or higher
- Virtual Environment (venv)
- [Ollama](https://github.com/ollama/ollama) (running locally)
- VS Code (or any IDE)
- Git

## 🚀 Clone the Repository

First, clone the EMScribe repository from GitHub to your local machine.

```bash
git clone https://github.com/ScottSucksAtProgramming/EMScribe.git
cd EMScribe
```

## 🏗️ Set Up a Virtual Environment

Next, set up a virtual environment to manage dependencies. This helps avoid conflicts with other projects.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## 📦 Install Dependencies

With the virtual environment activated, install the required Python packages.

```bash
pip install -r requirements.txt
```

## ⚙️ Configure Ollama

Ensure that [Ollama](https://github.com/ollama/ollama) is running locally and accessible at `http://localhost:11434`.

### Starting Ollama

Refer to Ollama's documentation to start the server locally. Ensure it is running and accessible before proceeding.

## 📂 Directory Structure

Here's an overview of the EMScribe directory structure after installation:

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
|   |-- api_reference
|   |   |-- extract_reviewer.md
|   |   |-- index.md
|   |   |-- model_loader.md
|   |   |-- narrative_manager.md
|   |   |-- prompt_manager.md
|   |   |-- transcript_cleaner.md
|   |   `-- transcript_extractor.md
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

## ✅ Verify the Installation

To verify that everything is set up correctly, run the tests:

```bash
pytest
```

If all tests pass, congratulations! Your installation is successful, and you are ready to use EMScribe. 🎉

## 🔜 Next Steps

- **[Usage](usage.md)**: Learn how to use EMScribe for extracting and cleaning transcripts.
- **[Development](development.md)**: Understand the development workflow and how to contribute to EMScribe.
- **[API Reference](api_reference/index.md)**: Detailed information about the API and modules.
- **[Contributing](contributing.md)**: Guidelines for contributing to the project.