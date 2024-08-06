# 🧪 EMScribe Testing Guide

Welcome to the EMScribe Testing Guide! This document provides instructions on how to write and run tests for the EMScribe project, ensuring that all features are thoroughly tested and work as expected.

## 📚 Table of Contents

- [🧪 EMScribe Testing Guide](#-emscribe-testing-guide)
  - [📚 Table of Contents](#-table-of-contents)
  - [🚀 Introduction](#-introduction)
  - [🛠️ Setting Up the Testing Environment](#️-setting-up-the-testing-environment)
    - [📋 Dependencies](#-dependencies)
    - [🏗️ Setting Up](#️-setting-up)
  - [✅ Running Tests](#-running-tests)
  - [✍️ Writing Tests](#️-writing-tests)
    - [📄 Test Naming Conventions](#-test-naming-conventions)
    - [🧪 Test Structure](#-test-structure)
    - [📝 Example Test](#-example-test)
  - [🗂️ Test File Overview](#️-test-file-overview)
  - [🎉 Conclusion](#-conclusion)

## 🚀 Introduction

Testing is a crucial part of the development process for EMScribe. It helps ensure that all features are working correctly and that any changes do not introduce new issues. We use `pytest` as our testing framework.

## 🛠️ Setting Up the Testing Environment

### 📋 Dependencies

Ensure you have the following dependencies installed:

- Python 3.8 or higher
- `pytest`

You can install `pytest` using pip:

```bash
pip install pytest
```

### 🏗️ Setting Up

Before running the tests, ensure your development environment is set up correctly. Follow the [Development Guide](development.md) to set up your environment and install the necessary dependencies.

## ✅ Running Tests

To run all tests, simply execute the following command in the root directory of the project:

```bash
pytest
```

This command will discover and run all the test files in the project.

## ✍️ Writing Tests

Tests are located in the `tests` directory. Each test file corresponds to a specific module or feature in the project. Here are some guidelines for writing tests:

### 📄 Test Naming Conventions

- Test files should be named `test_<module_name>.py`.
- Test functions should be named `test_<functionality>`.

### 🧪 Test Structure

- Use `pytest` for writing tests.
- Each test function should have a clear and descriptive name.
- Include setup and teardown code if necessary using fixtures.
- Test various scenarios, including edge cases.

### 📝 Example Test

Here's an example of a simple test for the `ModelLoader` class:

```python
import pytest
from modules.model_loader import ModelLoader

def test_model_loader_initialization():
    model_loader = ModelLoader(model_name="llama3.1")
    assert model_loader.model_name == "llama3.1"
    assert model_loader.base_url == "http://localhost:11434"
```

## 🗂️ Test File Overview

Here's an overview of the test files and what they cover:

- `conftest.py`: Configuration for pytest fixtures.
- `test_clean_command.py`: Tests for the cleaning command.
- `test_cleaning_prompts.py`: Tests for cleaning prompts.
- `test_cli.py`: Tests for the command-line interface.
- `test_extract_command.py`: Tests for the extraction command.
- `test_extract_reviewer.py`: Tests for the extract reviewer module.
- `test_extraction_prompts.py`: Tests for extraction prompts.
- `test_generate_command.py`: Tests for the narrative generation command.
- `test_model_loader.py`: Tests for the model loader module.
- `test_narrative_manager.py`: Tests for the narrative manager module.
- `test_narrative_prompts.py`: Tests for narrative prompts.
- `test_prompt_manager.py`: Tests for the prompt manager module.
- `test_review_command.py`: Tests for the review command.
- `test_review_prompts.py`: Tests for review prompts.
- `test_transcript_cleaner.py`: Tests for the transcript cleaner module.
- `test_transcript_extractor.py`: Tests for the transcript extractor module.
- `test_utils.py`: Utility tests (if applicable).

## 🎉 Conclusion

Following these guidelines will help maintain the quality and consistency of the EMScribe codebase. Ensure all new features are thoroughly tested and that tests cover various scenarios and edge cases. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).