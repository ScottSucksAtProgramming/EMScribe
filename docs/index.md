# EMScribe Documentation

<div style="text-align: center;">
    <img src="images/emscribe_logo.png" alt="EMScribe Logo" width="300"/>
</div>

Welcome to the EMScribe documentation! Here you'll find everything you need to know about installing, using, and contributing to EMScribe. Whether you're a new user or a seasoned developer, we've got you covered.

## 📑 Table of Contents

- [Overview](#overview)
- [Installation](installation.md)
- [Usage](usage.md)
- [Development](development.md)
- [API Reference](api_reference/index.md)
- [Contributing](contributing.md)
- [Contact](#contact)

## 🚀 Overview

EMScribe is your ultimate tool for creating comprehensive EMS narratives in a user-selected format. Designed to streamline the documentation process, EMScribe extracts detailed information from text transcripts of patient interactions, providing thorough reports that include:

- Patient demographics
- Medical history
- Chief complaints
- History of present illness
- Treatments performed
- Objective assessments
- Treatment plans
- Transport information
- Transfer of care details

### ✨ Features

- **🔍 Detailed Information Extraction**: Extracts comprehensive patient information from text transcripts.
- **📋 Narrative Generation**: Creates thorough EMS narratives.
- **🧐 Narrative Review**: Reviews narratives for missing information or inconsistencies (coming soon).
- **⚖️ Medical-Legal Review**: Suggests changes to protect users from legal issues (coming soon).
- **📄 Plain Text Output**: Outputs the final narrative in an easily readable format.
- **💻 CLI Support**: Command-line interface for cleaning, extracting, and generating narratives.

### 📂 Directory Structure

Here's a peek into how EMScribe is organized:

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

### 🏃‍♂️ Getting Started

Ready to jump in? Here’s how to get started with EMScribe:

1. **[Installation Instructions](installation.md)**: Set up EMScribe on your machine.
2. **[Usage Guide](usage.md)**: Learn how to run scripts and make the most out of EMScribe.
3. **[Development Guide](development.md)**: For developers looking to contribute, this guide covers everything you need to know.
4. **[API Reference](api_reference/index.md)**: Detailed information about the API and how to use each module.
5. **[Contributing Guidelines](contributing.md)**: Learn how to contribute to the project.

## 📧 Contact

Have questions or need support? Reach out to [ScottSucks](https://github.com/ScottSucksAtProgramming).