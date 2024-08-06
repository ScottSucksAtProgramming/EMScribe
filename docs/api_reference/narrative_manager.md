# 🚀 Narrative Manager

Welcome to the Narrative Manager module documentation! The `NarrativeManager` class is crucial for generating comprehensive EMS narratives from extracted data. This guide provides detailed information about its attributes, methods, and usage examples.

## 📚 Class: `NarrativeManager`

### **Description:**
The `NarrativeManager` class is designed to generate EMS narratives using extracted data and an AI model. It leverages the `ModelLoader` and `PromptManager` classes to interact with the AI model and manage prompts efficiently.

### 🏗️ Attributes:

- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

### 🚀 Methods:

#### `__init__(self, model_loader: ModelLoader, prompt_manager: PromptManager)`

**Description:**
Initializes the `NarrativeManager` with a `ModelLoader` and `PromptManager` instance.

**Parameters:**
- `model_loader (ModelLoader)`: An instance of `ModelLoader` to interact with the AI model.
- `prompt_manager (PromptManager)`: An instance of `PromptManager` to manage prompts.

**Example:**

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.narrative_manager import NarrativeManager

# Initialize ModelLoader and PromptManager
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"generate_narrative": "Generate a narrative from the following information: {info}"})

# Initialize NarrativeManager
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)
```

#### `generate_narrative(self, narrative_format: str, data: Dict) -> str`

**Description:**
Generates a narrative based on the specified format and data.

**Parameters:**
- `narrative_format (str)`: The key for the desired narrative format.
- `data (Dict)`: The extracted information in a dictionary.

**Returns:**
- `str`: The generated narrative.

**Example:**

```python
data = {
    "incident_info": "Incident at 123 Main St.",
    "patient_demographics": "John Doe, 45, Male",
    "chief_complaints": "Chest pain, shortness of breath",
    "history_of_present_illness": "Chest pain started 2 hours ago. No relief with rest.",
    "past_medical_history": "Hypertension, diabetes",
    "medications": "Lisinopril, Metformin",
    "allergies": "None",
    "vital_signs": "BP 140/90, HR 88, RR 20, SpO2 98%",
    "physical_exam": "Normal S1S2, no murmurs. Clear lungs bilaterally.",
    "treatment_plan": "Aspirin 325 mg PO, Nitro 0.4 mg SL, IV access, transport to ED.",
    "transport_info": "Transported to General Hospital, code 2.",
    "transfer_of_care": "Patient care transferred to ED staff."
}

narrative = narrative_manager.generate_narrative("presoaped_format", data)
print("Generated Narrative:")
print(narrative)
```

#### `_generate_response(self, prompt: str) -> str`

**Description:**
Generates a response from the AI model based on the provided prompt.

**Parameters:**
- `prompt (str)`: The input prompt for the model.

**Returns:**
- `str`: The AI model's response.

**Example:**

```python
prompt = "Generate a narrative from the following information: Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
response = narrative_manager._generate_response(prompt)
print("Generated Response:")
print(response)
```

## 🌟 Usage Examples

### Example 1: Initializing the NarrativeManager

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.narrative_manager import NarrativeManager

# Initialize ModelLoader with a specific model name
model_loader = ModelLoader(model_name="llama3.1")

# Initialize PromptManager with predefined prompts
prompts = {
    "generate_narrative": "Generate a narrative from the following information: {info}"
}
prompt_manager = PromptManager(prompts=prompts, context_window_size=32000)

# Initialize NarrativeManager
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)
```

### Example 2: Generating a Narrative from Extracted Data

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.narrative_manager import NarrativeManager

# Initialize components
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"generate_narrative": "Generate a narrative from the following information: {info}"})
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

# Example data extracted from a transcript
data = {
    "incident_info": "Incident at 123 Main St.",
    "patient_demographics": "John Doe, 45, Male",
    "chief_complaints": "Chest pain, shortness of breath",
    "history_of_present_illness": "Chest pain started 2 hours ago. No relief with rest.",
    "past_medical_history": "Hypertension, diabetes",
    "medications": "Lisinopril, Metformin",
    "allergies": "None",
    "vital_signs": "BP 140/90, HR 88, RR 20, SpO2 98%",
    "physical_exam": "Normal S1S2, no murmurs. Clear lungs bilaterally.",
    "treatment_plan": "Aspirin 325 mg PO, Nitro 0.4 mg SL, IV access, transport to ED.",
    "transport_info": "Transported to General Hospital, code 2.",
    "transfer_of_care": "Patient care transferred to ED staff."
}

# Generate a narrative
narrative = narrative_manager.generate_narrative("presoaped_format", data)
print("Generated Narrative:")
print(narrative)
```

### Example 3: Generating a Response from a Prompt

```python
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager
from modules.narrative_manager import NarrativeManager

# Initialize components
model_loader = ModelLoader(model_name="llama3.1")
prompt_manager = PromptManager(prompts={"generate_narrative": "Generate a narrative from the following information: {info}"})
narrative_manager = NarrativeManager(model_loader=model_loader, prompt_manager=prompt_manager)

# Generate a response from a prompt
prompt = "Generate a narrative from the following information: Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
response = narrative_manager._generate_response(prompt)
print("Generated Response:")
print(response)
```

## 🎉 Conclusion

The `NarrativeManager` class is an essential tool for generating comprehensive EMS narratives from extracted data. By understanding its attributes and methods, you can effectively create detailed and accurate EMS reports. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).