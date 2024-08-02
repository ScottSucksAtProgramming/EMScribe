# -*- coding: utf-8 -*-
# tests/test_cli.py

"""
Test suite for the EMScribe CLI tool.

This module contains tests for the EMScribe CLI tool, including tests for
cleaning, extracting, reviewing, and generating narratives from EMS transcripts.
"""

import subprocess


def run_subprocess_with_env(command):
    """
    Run a subprocess with the current environment.

    Args:
        command (list): The command to run as a subprocess.

    Returns:
        CompletedProcess: The result of the subprocess.run call.
    """
    return subprocess.run(command, capture_output=True, text=True, check=True)


def test_clean_transcript():
    command = ["python3", "scripts/cli.py", "clean", "data/example_transcript.txt"]
    result = run_subprocess_with_env(command)

    assert not result.returncode, f"Command failed with error: {result.stderr}"

    with open("data/cleaned_transcript.txt", "r", encoding="utf-8") as file:
        cleaned_transcript = file.read()

    assert "This is Ambulance 292" in cleaned_transcript
    assert "Frederich can you tell me what's going on today?" in cleaned_transcript


def test_extract_information():
    command = ["python3", "scripts/cli.py", "extract", "data/cleaned_transcript.txt"]
    result = run_subprocess_with_env(command)

    assert not result.returncode, f"Command failed with error: {result.stderr}"

    with open("data/extract.txt", "r", encoding="utf-8") as file:
        extracted_data = file.read()

    assert "Unit: 292" in extracted_data
    assert "Patient: Frederich Neizche" in extracted_data


def test_generate_narrative():
    command = ["python3", "scripts/cli.py", "generate", "data/reviewed_extract.txt"]
    result = run_subprocess_with_env(command)

    assert not result.returncode, f"Command failed with error: {result.stderr}"

    with open("data/narrative.txt", "r", encoding="utf-8") as file:
        narrative = file.read()

    assert "PRE-ARRIVAL:" in narrative
    assert "SUBJECTIVE:" in narrative


def test_display_help():
    command = ["python3", "scripts/cli.py", "--help"]
    result = run_subprocess_with_env(command)

    assert not result.returncode, f"Command failed with error: {result.stderr}"
    assert "usage:" in result.stdout
