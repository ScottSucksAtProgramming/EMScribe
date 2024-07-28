# EMScribe 2.0 Documentation

<div style="text-align: center;">
    <img src="assets/emscribe_logo_small.jpg" alt="EMScribe Logo" width="300"/>
</div>

Welcome to the EMScribe 2.0 documentation. This documentation covers everything you need to know about installing, using, and contributing to EMScribe 2.0.

## Table of Contents

- [Overview](#overview)
- [Installation](installation.md)
- [Usage](usage.md)
- [Development](development.md)
- [API Reference](api_reference.md)
- [Contributing](contributing.md)

## Overview

EMScribe 2.0 is a project designed to create comprehensive EMS narratives in a user-selected format. The application can extract information from text transcripts of patient interactions, providing detailed reports that include patient demographics, medical history, chief complaints, history of present illness, treatments done, objective assessment, treatment plans, transport information, and transfer of care.

### Features

- Extracts detailed patient information from text transcripts.
- Generates comprehensive EMS narratives.
- Reviews narratives for missing information or incongruencies.
- Provides medical-legal review and suggests changes to protect the user.
- Outputs the final narrative in plain text.

### Directory Structure

The project is organized as follows:

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
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_model_loader.py
│   ├── test_transcript_cleaner.py
│   ├── test_transcript_extractor.py
├── README.md
├── requirements.txt
└── venv/
```

### Getting Started

To get started with EMScribe 2.0, follow the [installation instructions](installation.md).

For usage examples and detailed instructions on how to run the scripts, refer to the [usage guide](usage.md).

For developers looking to contribute to EMScribe 2.0, see the [development guide](development.md) and the [contributing guidelines](contributing.md).

For detailed information about the API and how to use each module, see the [API reference](api_reference.md).

## Contact

For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).
