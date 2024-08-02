import os
import pytest
import logging
from commands.generate_command import GenerateCommand

class MockNarrativeManager:
    def generate_narrative(self, data):
        return f"generated {data}"

class MockPromptManager:
    def __init__(self):
        self.prompts = {
            "presoaped_format.prearrival": "Pre-Arrival: {data}",
            "presoaped_format.subjective": "Subjective: {data}",
            "presoaped_format.history_of_present_illness": "History of Present Illness: {data}",
            "presoaped_format.patient_histories": "Patient Histories: {data}",
            "presoaped_format.objective_1": "Objective: {data}",
            "presoaped_format.labs_and_tests": "Labs and Tests: {data}",
            "presoaped_format.assessment": "Assessment: {data}",
            "presoaped_format.plan": "Plan: {data}",
            "presoaped_format.delta": "Delta: {data}",
            "presoaped_format.hand_off": "Hand Off: {data}",
        }

    def get_prompt(self, key, **kwargs):
        if key not in self.prompts:
            raise KeyError(f"Prompt with key '{key}' not found.")
        return self.prompts[key].format(**kwargs)

def test_generate_command_file_not_found(tmp_path, caplog):
    narrative_manager = MockNarrativeManager()
    prompt_manager = MockPromptManager()
    command = GenerateCommand(narrative_manager, prompt_manager)

    reviewed_data_path = tmp_path / "nonexistent_file.txt"
    output_path = tmp_path / "output.txt"

    with caplog.at_level(logging.ERROR):
        command.execute(reviewed_data_path, output_path)

    assert "File not found" in caplog.text

def test_generate_command_success(tmp_path, caplog):
    narrative_manager = MockNarrativeManager()
    prompt_manager = MockPromptManager()
    command = GenerateCommand(narrative_manager, prompt_manager)

    reviewed_data_path = tmp_path / "reviewed_data.txt"
    output_path = tmp_path / "output.txt"

    with open(reviewed_data_path, "w") as file:
        file.write("reviewed data")

    # Log paths for debugging
    logging.debug("Reviewed data path: %s", reviewed_data_path)
    logging.debug("Output path: %s", output_path)

    with caplog.at_level(logging.DEBUG):
        command.execute(reviewed_data_path, output_path)

    # Log for debugging
    logging.debug("Checking if output file exists: %s", output_path.exists())

    assert output_path.exists(), f"Output file does not exist: {output_path}"

    with open(output_path, "r") as file:
        generated_narrative = file.read()

    # Check that each section is generated correctly
    assert "Pre-Arrival: reviewed data" in generated_narrative
    assert "Subjective: reviewed data" in generated_narrative
    assert "History of Present Illness: reviewed data" in generated_narrative
    assert "Patient Histories: reviewed data" in generated_narrative
    assert "Objective: reviewed data" in generated_narrative
    assert "Labs and Tests: reviewed data" in generated_narrative
    assert "Assessment: reviewed data" in generated_narrative
    assert "Plan: reviewed data" in generated_narrative
    assert "Delta: reviewed data" in generated_narrative
    assert "Hand Off: reviewed data" in generated_narrative
