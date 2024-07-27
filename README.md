
# EMScribe 2.0

<p align="center">
  <img src="images/emscribe_logo.png" alt="EMScribe Logo" />
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

## Directory Structure

```plaintext
emscribe/
├── modules/
│   ├── __init__.py
│   ├── model_loader.py
│   ├── prompt_manager.py
│   ├── transcript_cleaner.py
│   ├── transcript_extractor.py
│   ├── prompts/
│       ├── __init__.py
│       ├── extraction_prompts.py
│       ├── cleaning_prompts.py
├── scripts/
│   ├── __init__.py
│   ├── extraction.py
│   ├── preprocess.py
│   ├── main.py
├── README.md
├── requirements.txt
├── venv/
```

## Running the Scripts

### Extraction Script

To run the extraction script, use the following command:

```bash
python -m scripts.extraction
```

### Preprocess Script

To run the preprocess script, use the following command:

```bash
python -m scripts.preprocess
```

### Example Transcript Input

```plaintext
Patient name is John Doe. Age: 45. Gender: Male. 
Past medical history includes hypertension and diabetes. 
The chief complaint is chest pain that started two hours ago...
```

### Expected Output

The script will output detailed information extracted from the transcript, formatted into comprehensive EMS narratives.

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
   git commit -m "Adds new feature"
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