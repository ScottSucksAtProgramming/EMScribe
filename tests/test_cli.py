import subprocess
import pytest
import os

# Get the absolute path to the cli.py script
script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts/cli.py'))

# Function to run a subprocess with the correct working directory and environment
def run_subprocess_with_env(args, working_dir):
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return subprocess.run(args, capture_output=True, text=True, cwd=working_dir, env=env)

# Test for cleaning a transcript
def test_clean_transcript(tmp_path):
    transcript_text = "The patient is experiencing experiencing shortness of breath. The patient is The patient is also complaining of chest pain."
    transcript_path = tmp_path / "transcript.txt"
    with open(transcript_path, "w") as file:
        file.write(transcript_text)

    result = run_subprocess_with_env(["python3", script_path, "clean", str(transcript_path)], os.path.dirname(script_path))
    assert result.returncode == 0
    assert "Cleaned Transcript:" in result.stdout

# Test for extracting information
def test_extract_information(tmp_path):
    transcript_text = "Patient John Doe, 45 years old, male, experiencing chest pain for the past 2 hours. History of hypertension and diabetes."
    transcript_path = tmp_path / "transcript.txt"
    with open(transcript_path, "w") as file:
        file.write(transcript_text)

    result = run_subprocess_with_env(["python3", script_path, "extract", str(transcript_path)], os.path.dirname(script_path))
    assert result.returncode == 0
    assert "Extracted Information:" in result.stdout

# Test for generating a narrative
def test_generate_narrative(tmp_path):
    transcript_text = """
    This is Ambulance 292 responding emergent with a full crew and no delays from headquarters to the Kevorkian Clinic for a reported chest pain. During transport dispatch informed us that the patient is alert and breathing.

    Unit 292 arriving on scene.

    Our patient is Frederich Neizche he was born February 8th, 1986. He is a 38 year old male. Complaining for severe 10/10 chest pain. He is receiving oxygen via a nasal cannula and is lying on the exam table in room 1.

    Frederich can you tell me what's going on today?

    About two hours ago I was sitting and watching TV in my living room and I began to feel a sudden crushing pressure in my chest.

    Do you have any shortness of breath?

    No, but I do feel nauseous and dizzy. I've also been sweating a lot. I took one of my nitro tabs but it didn't help. Any time I stand up or try to do any activity the pain gets worse. I feel a little better when I'm laying down.

    Does the pain radiate or move?

    I also have pain to my jaw and down my left arm.

    On a scale of 1 to 10, with 10 being the worst pain you've ever felt in your life and 1 being almost no pain what is it right now.

    It's a 10. It's really bad.

    According to the paperwork provided by the doctor here Frederich has a known medical history of coronary artery disease, hypertension, high cholesterol, type 2 diabetes, BPH, GERD and a previous MI in 2018 with two cardiac stents placed.

    The doctor has placed an IV in the patients right arm, and gave them another dose of sublingual nitro. He also did an EKG which show ST Elevations in leads II, III, and aVF with a reciprocal ST Depression in aVL.

    Do you have any allergies?

    Only to cats and kiwi.

    What medications do you take?

    I take metoprolol for my blood pressure, eliquis, and metformin.

    Okay great. I'm going to do a quick exam.

    Sure go ahead.

    patient is alert and oriented to person place time and event. He appears pale and diaphoretic and in obvious pain. He is dressed in normal clothes and appear to be well groomed. Frederich's skin is pale, cool and diaphoretic. skin is intact. There are no rashes or bleeding. Airways a patent with good air movement. he is able to speak in full sentence. Trachea is midline. The chest is atraumatic without bruising, implanted devices or flail segments. heart rate is rapid, regular and weak. Distal pulses are palpable but thready. No edema noted.

    Lung sounds a clear and equal bilaterally. Chest expansion is adequate and even. Respiratory pattern is regular and elevated with increased work of breathing.

    Frederich is calm and his behavior is appropriate to the situation. thought pattern and speech are organized no bizarre behavior noted.

    EKG shows Sinus Rhythm at 100 with PVCs.

    Blood sugar is 84.

    Vitals are 102/54, heart rate 100 weak and regular, 17 breaths per minutes regular and labored, SpO2 is 98%, EtCO2 is 33.
    """
    transcript_path = tmp_path / "transcript.txt"
    output_path = tmp_path / "output.txt"
    with open(transcript_path, "w") as file:
        file.write(transcript_text)

    result = run_subprocess_with_env(["python3", script_path, "generate", str(transcript_path), "--output", str(output_path)], os.path.dirname(script_path))
    assert result.returncode == 0
    assert os.path.exists(output_path)
    with open(output_path, "r") as file:
        output_content = file.read()
    assert "Generated Narrative:" in output_content

# Test for displaying help
def test_display_help():
    result = run_subprocess_with_env(["python3", script_path, "--help"], os.path.dirname(script_path))
    assert result.returncode == 0
    assert "usage:" in result.stdout
    assert "options:" in result.stdout
    assert "positional arguments:" in result.stdout
    assert "{clean,extract,generate}" in result.stdout  # Ensure the commands are listed
