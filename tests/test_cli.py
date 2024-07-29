# tests/test_cli.py

import subprocess
import os
import pytest

script_path = os.path.abspath("scripts/cli.py")

def run_subprocess_with_env(args, working_dir):
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath(os.path.dirname(__file__))
    return subprocess.run(args, capture_output=True, text=True, cwd=working_dir, env=env)

def test_clean_transcript(tmp_path):
    transcript_text = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    transcript_path = tmp_path / "transcript.txt"
    with open(transcript_path, "w") as file:
        file.write(transcript_text)

    result = run_subprocess_with_env(["python3", script_path, "clean", str(transcript_path)], os.path.dirname(script_path))
    assert result.returncode == 0
    assert "Cleaned Transcript:" in result.stdout

def test_extract_information(tmp_path):
    transcript_text = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
    transcript_path = tmp_path / "transcript.txt"
    with open(transcript_path, "w") as file:
        file.write(transcript_text)

    result = run_subprocess_with_env(["python3", script_path, "extract", str(transcript_path)], os.path.dirname(script_path))
    assert result.returncode == 0
    assert "Extracted Information:" in result.stdout

def test_generate_narrative(tmp_path):
    extracted_data = """
    {
        "incident_info": "Unit 5-41-27, emergent, full crew, no delay, headquarters, Kevorkian Clinic, chest pain, stand by until police arrived",
        "patient_demographics": "Frederich Neizche, 38, male",
        "patient_histories": "coronary artery disease, hypertension, high cholesterol, type 2 diabetes, BPH, GERD, previous MI in 2018, metoprolol, eliquis, metformin, no allergies to medications",
        "history_of_present_illness": "Severe 10/10 chest pain, started 2 hours ago, crushing pressure, radiates to jaw and left arm, relieved by nitroglycerin",
        "objective": "Alert and oriented, pale and diaphoretic, nasal cannula, rapid and weak heart rate, clear lung sounds, normal EKG",
        "labs_and_tests": "ST elevations in leads II, III, aVF, reciprocal changes in aVL, blood sugar 84, vitals 102/54, heart rate 100, SpO2 98%, EtCO2 33"
    }
    """
    extracted_data_path = tmp_path / "extracted_data.txt"
    output_path = tmp_path / "output.txt"
    with open(extracted_data_path, "w") as file:
        file.write(extracted_data)

    result = run_subprocess_with_env(["python3", script_path, "generate", str(extracted_data_path), "--output", str(output_path)], os.path.dirname(script_path))
    assert result.returncode == 0
    assert "Generated Narrative:" in result.stdout

def test_display_help():
    result = run_subprocess_with_env(["python3", script_path, "--help"], os.path.dirname(script_path))
    assert result.returncode == 0
    assert "usage:" in result.stdout  # Change this to match the actual output
    assert "options:" in result.stdout

if __name__ == "__main__":
    pytest.main()
