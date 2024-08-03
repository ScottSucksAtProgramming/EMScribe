
# Testing Guide for EMScribe Project

This document provides an overview of the test suite for the EMScribe project, including the structure of the tests, the purpose of each test, and instructions on how to run the tests.

## Table of Contents

1. [Introduction](#introduction)
2. [Test Structure](#test-structure)
3. [Test Descriptions](#test-descriptions)
4. [Running the Tests](#running-the-tests)

## Introduction

The EMScribe project uses unit tests to ensure the correctness of its functionality. The tests are written using the `pytest` framework and are designed to be easy to run and understand.

## Test Structure

The test suite is organized into the following files:

- `conftest.py`: Configuration file for pytest fixtures.
- `test_cleaning_prompts.py`: Tests for cleaning prompts.
- `test_cli.py`: Tests for the command-line interface (CLI) functionality.
- `test_extract_reviewer.py`: Tests for the extract reviewer functionality.
- `test_extraction.py`: Tests for the transcript extraction and cleaning functionality.
- `test_extraction_prompts.py`: Tests for extraction prompts.
- `test_model_loader.py`: Tests for the model loader.
- `test_narrative_manager.py`: Tests for the narrative manager.
- `test_narrative_prompts.py`: Tests for narrative prompts.
- `test_preprocess.py`: Tests for the transcript preprocessing functionality.
- `test_prompt_manager.py`: Tests for managing prompts.
- `test_review_prompts.py`: Tests for review prompts.
- `test_transcript_cleaner.py`: Tests for the transcript cleaner.
- `test_transcript_extractor.py`: Tests for the transcript extractor.
- `test_utils.py`: Tests for utility functions.
- `transcript.txt`: Example transcript file for testing.

## Test Descriptions

### `conftest.py`

- **Purpose:** Provides common pytest fixtures used across multiple test files.

### `test_cleaning_prompts.py`

- **Purpose:** Tests the cleaning prompts.
- **Main Tests:**
  - Ensures that cleaning prompts are correctly processed and formatted.

### `test_cli.py`

- **Purpose:** Tests the CLI commands for cleaning, extracting, generating, and reviewing transcripts.
- **Main Tests:**
  - `test_initialize_components`: Ensures components are initialized correctly.
  - `test_parse_args_*`: Verifies argument parsing for different CLI commands.
  - `test_main`: Tests the main entry point for the CLI commands.

### `test_extract_reviewer.py`

- **Purpose:** Tests the extract reviewer functionality.
- **Main Tests:**
  - Various tests to ensure correct review and extraction of transcript data.

### `test_extraction.py`

- **Purpose:** Tests the transcript extraction and cleaning process.
- **Main Tests:**
  - `test_extract_information`: Verifies the extraction of information from transcripts.
  - Additional tests for various edge cases and scenarios.

### `test_extraction_prompts.py`

- **Purpose:** Tests the extraction prompts.
- **Main Tests:**
  - Ensures that extraction prompts are correctly processed and formatted.

### `test_model_loader.py`

- **Purpose:** Tests the model loader functionality.
- **Main Tests:**
  - `test_initialization_with_client`: Ensures correct initialization with a client.
  - `test_generate`: Verifies the generation of responses.

### `test_narrative_manager.py`

- **Purpose:** Tests the narrative manager.
- **Main Tests:**
  - Various tests to ensure correct narrative generation from extracted data.

### `test_narrative_prompts.py`

- **Purpose:** Tests the narrative prompts.
- **Main Tests:**
  - Ensures that narrative prompts are correctly processed and formatted.

### `test_preprocess.py`

- **Purpose:** Tests the preprocessing steps for transcripts.
- **Main Tests:**
  - `test_preprocess_cleaning`: Ensures transcripts are cleaned correctly.
  - `test_preprocess_with_whitespace`: Verifies that extra whitespace is removed.
  - `test_preprocess_with_special_characters`: Checks handling of special characters.
  - `test_preprocess_empty_string`: Ensures handling of empty input.

### `test_prompt_manager.py`

- **Purpose:** Tests the management of prompts.
- **Main Tests:**
  - `test_get_prompt_existing_key`: Verifies retrieval of existing prompts.
  - `test_get_prompt_nonexistent_key`: Ensures handling of non-existent prompts.
  - Additional tests for various prompt scenarios.

### `test_review_prompts.py`

- **Purpose:** Tests the review prompts.
- **Main Tests:**
  - Ensures that review prompts are correctly processed and formatted.

### `test_transcript_cleaner.py`

- **Purpose:** Tests the transcript cleaner.
- **Main Tests:**
  - Various tests to ensure correct cleaning of transcripts.

### `test_transcript_extractor.py`

- **Purpose:** Tests the transcript extractor.
- **Main Tests:**
  - Various tests to ensure correct extraction of information from transcripts.

### `test_utils.py`

- **Purpose:** Tests for utility functions.
- **Main Tests:**
  - `test_read_file`: Verifies that file content is read correctly.
  - `test_write_file`: Ensures content is written to a file properly.
  - `test_ensure_file_exists`: Checks that the existence of a file is correctly verified.
  - `test_ensure_file_exists_raises_error`: Ensures an error is raised for non-existent files.

## Running the Tests

To run the tests, you need to have `pytest` installed. You can install it using pip:

```bash
pip install pytest
```

Run the tests using the following command:

```bash
pytest -vv
```

The `-vv` option increases the verbosity of the test output, providing more detailed information about the tests being run.

## Conclusion

This document provides an overview of the test suite for the EMScribe project. Following this guide will help you understand the structure and purpose of each test, and how to run them effectively. If you encounter any issues or have questions about the tests, feel free to reach out to the project maintainers.
