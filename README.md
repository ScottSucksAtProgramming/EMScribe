# EMScribe

<p align="center">
  <img src="images/emscribe_logo.png" alt="EMScribe Logo" width="500" />
</p>

<p align="center">
  <a href="https://github.com/ScottSucksAtProgramming/EMScribe/actions/workflows/python-app.yml"><img src="https://github.com/ScottSucksAtProgramming/EMScribe/actions/workflows/python-app.yml/badge.svg" alt="Build Status"></a>
  <a href="https://github.com/ScottSucksAtProgramming/EMScribe/issues"><img src="https://img.shields.io/github/issues/ScottSucksAtProgramming/EMScribe" alt="Issues"></a>
  <a href="https://github.com/ScottSucksAtProgramming/EMScribe/pulls"><img src="https://img.shields.io/github/issues-pr/ScottSucksAtProgramming/EMScribe" alt="Pull Requests"></a>
  <a href="https://github.com/ScottSucksAtProgramming/EMScribe/stargazers"><img src="https://img.shields.io/github/stars/ScottSucksAtProgramming/EMScribe" alt="Stars"></a>
  <a href="https://github.com/ScottSucksAtProgramming/EMScribe/blob/main/LICENSE"><img src="https://img.shields.io/github/license/ScottSucksAtProgramming/EMScribe" alt="License"></a>
  <a href="https://pypi.org/project/emscribe/"><img src="https://img.shields.io/pypi/pyversions/emscribe" alt="Python Versions"></a>
</p>

## 📑 Table of Contents

- [EMScribe](#emscribe)
   - [📑 Table of Contents](#-table-of-contents)
   - [🚀 Welcome to EMScribe!](#-welcome-to-emscribe)
   - [🌟 Overview](#-overview)
   - [✨ Key Features](#-key-features)
   - [🛠️ Setup](#️-setup)
      - [Prerequisites](#prerequisites)
      - [Installation](#installation)
      - [Verify the Installation](#verify-the-installation)
   - [🚀 Using EMScribe](#-using-emscribe)
      - [Adding EMScribe to Your PATH](#adding-emscribe-to-your-path)
      - [Running the `emscribe` Command](#running-the-emscribe-command)
      - [📈 Quick Start](#-quick-start)
   - [📁 Directory Structure](#-directory-structure)
   - [📅 Roadmap](#-roadmap)
   - [🤝 Contribution Guidelines](#-contribution-guidelines)
   - [📜 License](#-license)
   - [📧 Contact](#-contact)
   - [📚 Documentation](#-documentation)

## 🚀 Welcome to EMScribe!

Welcome to EMScribe, your ultimate companion for crafting comprehensive EMS narratives for patient care reports. Whether you're an EMT, paramedic, or researcher, EMScribe is designed to simplify your workflow and enhance your documentation process. Spend less time on your paperwork and more time providing exceptional care.

## 🌟 Overview

EMScribe is here to save the day by extracting critical information from text transcripts of patient interactions. It generates detailed reports that include:

- Patient demographics
- Medical history
- Chief complaints
- History of present illness
- Treatments performed
- Objective assessments
- Treatment plans
- Transport information
- Transfer of care details

## ✨ Key Features

- **🔍 Detailed Extraction:** Pulls comprehensive patient information from text transcripts.
- **📋 Narrative Generation:** Creates complete EMS narratives.
- **🧐 Narrative Review:** (Coming Soon) Identifies missing information or inconsistencies.
- **⚖️ Medical-Legal Review:** (Coming Soon) Suggests changes to ensure legal protection.
- **📄 Plain Text Output:** Provides the final narrative in an easily readable format.

## 🛠️ Setup

### Prerequisites

Make sure you have the following before getting started:

- Python 3.8 or higher
- Virtual Environment (venv)
- Ollama (running locally)
- VS Code (or any IDE)
- Git

### Installation

Follow these simple steps to install EMScribe:

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

   Ensure [Ollama](https://github.com/ollama/ollama) is running locally and accessible at `http://localhost:11434`.

### Verify the Installation

Run the tests to make sure everything is set up correctly:

```bash
pytest
```

If all tests pass, congratulations! You're ready to use EMScribe. 🎉

## 🚀 Using EMScribe

### Adding EMScribe to Your PATH

To use the `emscribe` command from any directory, add it to your PATH. Add the following line to your shell configuration file (e.g., `.bashrc`, `.zshrc`, or `.profile`):

```bash
export PATH="$PATH:/path/to/emscribe/bin"
```

Replace `/path/to/emscribe` with the absolute path to the `emscribe` file in your project directory.

After updating your shell configuration file, reload it:

```bash
source ~/.bashrc  # or source ~/.zshrc or source ~/.profile
```

### Running the `emscribe` Command

Now, you can use the `emscribe` command to clean transcripts, extract information, review, and generate narratives. Use the provided `transcript.txt` as a demo transcript when running the commands.

```bash
emscribe clean ./transcript.txt
emscribe extract ./transcript.txt
emscribe review ./extract.txt
emscribe generate ./reviewed_extract.txt --output ./narrative.txt
```

You can also pipe the output from one command to another:

```bash
emscribe clean ./transcript.txt | emscribe extract - | emscribe review - | emscribe generate - --output ./narrative.txt
```

### 📈 Quick Start

Want to dive right in? Here’s a quick way to get started with EMScribe:

1. **Clone the Repository**
2. **Install Dependencies**
3. **Run a Demo Command:**

   ```bash
   emscribe clean ./transcript.txt | emscribe extract - | emscribe review - | emscribe generate - --output ./narrative.txt
   ```

Enjoy the streamlined EMS documentation process! 🚑✨

## 📁 Directory Structure

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
|   `-- cli.py
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

## 📅 Roadmap

Here's a sneak peek at what's coming next:

- [ ] **PDF Extraction:** Add the ability to extract information from PDF files generated by ePCR software.
- [ ] **Additional Narrative Formats:** Include more narrative formats.
- [ ] **Hospital Hand-Off Reports:** Generate reports for hospital hand-offs.
- [ ] **User Interface:** Develop a user-friendly GUI for non-technical users.
- [ ] **Enhanced AI Capabilities:** Improve the accuracy  and speed of information extraction.
- [ ] **Customization:** Allow users to customize the narrative generation process.
- [ ] **Mobile App:** A mobile version of EMScribe for on-the-go usage.
- [ ] **API Access:** Integrate with other AI services like OpenAI, Claude, etc.
- [ ] **Integration:** Seamless integration with other EMS software systems.

Stay tuned for more updates!

## 🤝 Contribution Guidelines

Right now, I'm not looking for contributors, but if you have any requests or suggestions, feel free to contact me.

## 📜 License

This project uses a prohibitive license. You must obtain express written permission to use the software. For more details, please refer to the [LICENSE](LICENSE.md) file.

## 📧 Contact

For any questions or support, please contact [Scott Kostolni](https://github.com/ScottSucksAtProgramming).

## 📚 Documentation

For detailed documentation, check out:

- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage.md)
- [Development Guide](docs/development.md)
- [API Reference](docs/api_reference.md)
- [Contributing Guidelines](docs/contributing.md)
- [Testing](docs/testing.md)