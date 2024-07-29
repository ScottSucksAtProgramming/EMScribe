# Installation

This guide will help you set up EMScribe 2.0 on your local machine.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.8 or higher
- Virtual Environment (venv)
- Ollama (running locally)
- VS Code (or any IDE)
- Git

## Clone the Repository

First, clone the EMScribe 2.0 repository from GitHub to your local machine.

```bash
git clone <repository_url>
cd EMScribe
```

## Set Up a Virtual Environment

Next, set up a virtual environment to manage dependencies. This helps to avoid conflicts with other projects.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Install Dependencies

With the virtual environment activated, install the required Python packages.

```bash
pip install -r requirements.txt
```

## Configure Ollama

Ensure that Ollama is running locally and accessible at `http://localhost:11434`.

### Starting Ollama

Refer to Ollama's documentation to start the server locally. Ensure it is running and accessible before proceeding.

## Directory Structure

Here is an overview of the EMScribe 2.0 directory structure after installation:

```plaintext
emscribe/
├── docs/
│   ├── index.md
│   ├── installation.md
│   ├── usage.md
│   ├── development.md
│   ├── api_reference.md
│   ├── contributing.md
├── modules/
│   ├── __init__.py
│   ├── model_loader.py
│   ├── narrative_manager.py
│   ├── prompt_manager.py
│   ├── transcript_cleaner.py
│   ├── transcript_extractor.py
│   └── prompts/
│       ├── __init__.py
│       ├── extraction_prompts.py
│       ├── cleaning_prompts.py
│       └── narrative_prompts.py
├── scripts/
│   ├── __init__.py
│   ├── main.py
│   ├── extraction.py
│   ├── preprocess.py
│   ├── cli.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_model_loader.py
│   ├── test_transcript_cleaner.py
│   ├── test_transcript_extractor.py
│   ├── test_cli.py
├── images/
│   ├── emscribe_logo_small.jpg
├── README.md
├── requirements.txt
└── venv/
```

## Verify the Installation

To verify that everything is set up correctly, run the tests:

```bash
pytest
```

If all tests pass, your installation is successful and you are ready to use EMScribe 2.0.

## Next Steps

- [Usage](usage.md): Learn how to use EMScribe 2.0 for extracting and cleaning transcripts.
- [Development](development.md): Understand the development workflow and how to contribute to EMScribe 2.0.
- [API Reference](api_reference.md): Detailed information about the API and modules.
- [Contributing](contributing.md): Guidelines for contributing to the project.
