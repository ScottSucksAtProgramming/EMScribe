import os
import pytest
import logging
from commands.clean_command import CleanCommand
from modules.transcript_cleaner import TranscriptCleaner
from utils.utils import ensure_file_exists

class MockTranscriptCleaner:
    def clean(self, transcript):
        return "cleaned transcript"

def test_clean_command_file_not_found(tmp_path, caplog):
    cleaner = MockTranscriptCleaner()
    command = CleanCommand(cleaner)

    transcript_path = tmp_path / "nonexistent_file.txt"
    output_path = tmp_path / "output.txt"

    with caplog.at_level(logging.ERROR):
        command.execute(transcript_path, output_path)
    
    assert "File not found" in caplog.text

def test_clean_command_success(tmp_path):
    cleaner = MockTranscriptCleaner()
    command = CleanCommand(cleaner)

    transcript_path = tmp_path / "transcript.txt"
    output_path = tmp_path / "output.txt"

    with open(transcript_path, "w") as file:
        file.write("raw transcript")

    command.execute(transcript_path, output_path)

    with open(output_path, "r") as file:
        cleaned_transcript = file.read()
    
    assert cleaned_transcript == "cleaned transcript"
