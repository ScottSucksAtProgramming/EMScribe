# EMScribe Documentation 🚑

<div style="text-align: center;">
    <img src="images/emscribe_logo.png" alt="EMScribe Logo" width="300"/>
</div>

Welcome to the EMScribe documentation. This documentation covers everything you need to know about installing, using, and contributing to EMScribe.

## Table of Contents 📚

- [Overview](#overview)
- [Installation](installation.md)
- [Usage](usage.md)
- [Development](development.md)
- [API Reference](api_reference.md)
- [Contributing](contributing.md)

## Overview 🌟

EMScribe is a project designed to create comprehensive EMS narratives in a user-selected format. The application can extract information from text transcripts of patient interactions, providing detailed reports that include patient demographics, medical history, chief complaints, history of present illness, treatments done, objective assessment, treatment plans, transport information, and transfer of care.

### Features 🌟

- 🩺 Extracts detailed patient information from text transcripts.
- 🖋️ Generates comprehensive EMS narratives.
- 🔍 Reviews narratives for missing information or incongruencies.
- 🛡️ Provides medical-legal review and suggests changes to protect the user.
- 📄 Outputs the final narrative in plain text.
- 💻 CLI support for cleaning, extracting, and generating narratives.

### Directory Structure 📂

The project is organized as follows:

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
|   |-- test_transcript_extractor.py
|-- transcript.txt
`-- venv
```

### Getting Started 🚀

To get started with EMScribe, follow the [installation instructions](installation.md).

For usage examples and detailed instructions on how to run the scripts, refer to the [usage guide](usage.md).

For developers looking to contribute to EMScribe, see the [development guide](development.md) and the [contributing guidelines](contributing.md).

For detailed information about the API and how to use each module, see the [API reference](api_reference.md).

## Contact 📧

For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).
