# EMScribe 2.0

<p align="center">
  <img src="images/emscribe_logo.png" alt="EMScribe Logo" width="300" />
</p>

## Overview

EMScribe 2.0 is a project designed to create comprehensive EMS narratives in a user-selected format. The application can extract information from text transcripts of patient interactions, providing detailed reports that include patient demographics, medical history, chief complaints, history of present illness, treatments done, objective assessment, treatment plans, transport information, and transfer of care.

## Features

- Extracts detailed patient information from text transcripts.
- Generates comprehensive EMS narratives.
- Reviews narratives for missing information or incongruencies.
- Provides medical-legal review and suggests changes to protect the user.
- Outputs the final narrative in plain text.

## Setup

### Prerequisites

- Python 3.8 or higher
- Virtual Environment (venv)
- Ollama (running locally)
- VS Code (or any IDE)
- Git

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

4. **Configure Ollama:**

   Ensure Ollama is running locally and accessible at `http://localhost:11434`.

### Verify the Installation

To verify that everything is set up correctly, run the tests:

```bash
pytest
```

If all tests pass, your installation is successful and you are ready to use EMScribe 2.0.

## Directory Structure

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
│   ├── prompt_manager.py
│   ├── transcript_cleaner.py
│   ├── transcript_extractor.py
│   ├── narrative_manager.py
│   ├── prompts/
│       ├── __init__.py
│       ├── extraction_prompts.py
│       ├── cleaning_prompts.py
│       ├── narrative_prompts.py
├── scripts/
│   ├── __init__.py
│   ├── extraction.py
│   ├── preprocess.py
│   ├── main.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_model_loader.py
│   ├── test_transcript_cleaner.py
│   ├── test_transcript_extractor.py
├── README.md
├── requirements.txt
├── venv/
```

## Running the Scripts

### Extraction Script

To run the extraction script and extract detailed patient information from a transcript, use the following command:

```bash
python -m scripts.extraction
```

### Preprocess Script

To clean a transcript by removing repeated words and lines, correcting basic errors, and ensuring meaningful information is preserved, use the following command:

```bash
python -m scripts.preprocess
```

### Main Script

To demonstrate cleaning, extracting, and generating narratives, use the following command:

```bash
python -m scripts.main
```

### Example Transcript Input

```plaintext
Patient name is John Doe. Age: 45. Gender: Male. 
Past medical history includes hypertension and diabetes. 
The chief complaint is chest pain that started two hours ago...
```

### Expected Output

The script will output detailed information extracted from the transcript, formatted into comprehensive EMS narratives.

## Running the Application with Your Own Transcript

To run the application and provide your own transcript, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the main script:

    ```bash
    python -m scripts.main
    ```

4. When prompted, enter your EMS transcript. The application will process the transcript and generate a comprehensive EMS narrative.


## Development

### Adding New Features

To add new features or enhance existing ones, follow these steps:

1. **Create a New Branch:**

   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make Changes and Commit:**

   ```bash
   git add .
   git commit -m "Add new feature"
   ```

3. **Push the Branch and Create a Pull Request:**

   ```bash
   git push origin feature/new-feature
   ```

### Contribution Guidelines

- Ensure your code follows the project’s coding standards.
- Write clear, concise commit messages.
- Test your changes thoroughly before submitting a pull request.
- Provide detailed descriptions of the changes in pull requests.

## License

There is currently no license for this project.

## Contact

For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).

## Documentation

For detailed documentation, refer to the following:

- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage.md)
- [Development Guide](docs/development.md)
- [API Reference](docs/api_reference.md)
- [Contributing Guidelines](docs/contributing.md)