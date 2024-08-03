# EMScribe 🚑

<p align="center">
  <img src="images/emscribe_logo.png" alt="EMScribe Logo" width="500" />
</p>

## Overview

Welcome to **EMScribe**! **EMScribe** extracts vital information from text transcripts of patient interactions and generates high-quality, accurate patient care report narratives. With this software, EMS providers can focus their attention on patient care instead of documenting during transport. Give your patients a world-class experience while generating expert patient care reports in record time. 📋

## Features 🌟

- 🩺 **Extracts detailed patient information from recordings taken during the EMS call.**
- 🧹 **Cleans out background noise, side conversations, and inessential chatter while preserving the details of your medical care.**
- 🖋️ **Generates comprehensive EMS narratives with quality checks ensuring information accuracy and a clear professional tone.**
- 🔍 **Reviews narratives for missing information or incongruencies.**
- 🛡️ **Provides medical-legal review and suggests changes to protect the EMS provider.**
- 📄 **Outputs the final narrative in plain text ready for import directly into your ePCR software.**

## Setup 🛠️

### Prerequisites

- Python 3.8 or higher 🐍
- Virtual Environment (venv) 🌐
- [Ollama](https://github.com/ollama/ollama) (running locally) 💻
- VS Code (or any IDE) 🖥️
- Git 🌲

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ScottSucksAtProgramming/EMScribe.git
   cd emscribe
   ```

2. **Set Up the Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure [Ollama](https://github.com/ollama/ollama):**

   Ensure Ollama is running locally and accessible at `http://localhost:11434`. 🦙

### Verify the Installation

To verify that everything is set up correctly, run the tests:

```bash
pytest
```

If all tests pass, your installation is successful and you are ready to use EMScribe 2.0. 🎉

## Using the `emscribe` Command

### Adding `emscribe` to Your PATH

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

You can now use the `emscribe` command to clean transcripts, extract information, review, and generate narratives.

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

### Example Transcript Input

```plaintext
Patient name is John Doe. Age: 45. Gender: Male.
Past medical history includes hypertension and diabetes.
The chief complaint is chest pain that started two hours ago...
```

### Expected Output

The script will output detailed information extracted from the transcript, formatted into comprehensive EMS narratives.

## Roadmap 🚀

### Current Roadmap

#### Initial Setup and Features

- [x] **Set up project repository and initial code structure** ✔️
- [x] **Implement transcript cleaning functionality** 🧼
- [x] **Implement information extraction functionality** 📝
- [x] **Implement narrative generation functionality** 🖋️
- [x] **Add CLI for user interaction** 💻
- [x] **Perform initial testing and validation** 🧪

#### Enhancements and New Features

- [x] **Implement review functionality for extracted data** 🔍
- [x] **Add medical-legal review for narratives** 🛡️
- [ ] **Implement PDF information extraction** 📄
- [ ] **Integrate additional narrative types** 📑
- [ ] **Generate verbal report for hospital staff** 🗣️
- [ ] **Fine-tune model for narrative generation** 🧠

#### Future Development

- [ ] **Develop a web-based interface** 🌐
- [ ] **Implement as a cloud service** ☁️
- [ ] **Ensure HIPAA compliance for cloud service** 🏥
- [ ] **Develop a mobile application** 📱

### Future Roadmap

- [ ] **Explore integration with EHR systems** 🏥
- [ ] **Expand functionality for additional data sources** 🌐
- [ ] **Continuous improvement and feature updates** 🔄

## License 📜

This project is licensed under the Proprietary Software License. See the [LICENSE](./LICENSE) file for details.

## Contact 📧

For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).

## Documentation 📚

For detailed documentation, refer to the following:

- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage.md)
- [Development Guide](docs/development.md)
- [API Reference](docs/api_reference.md)
- [Contributing Guidelines](docs/contributing.md)
