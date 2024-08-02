import os
import pytest
import logging
from commands.review_command import ReviewCommand
from modules.extract_reviewer import ExtractReviewer

class MockExtractReviewer:
    def review_section(self, section, user_input):
        return "reviewed section"

def test_review_command_file_not_found(tmp_path, caplog):
    reviewer = MockExtractReviewer()
    command = ReviewCommand(reviewer)

    extracted_data_path = tmp_path / "nonexistent_file.txt"
    output_path = tmp_path / "output.txt"

    with caplog.at_level(logging.ERROR):
        command.execute(extracted_data_path, output_path)

    assert "Extracted data file not found" in caplog.text

def test_review_command_success(tmp_path, monkeypatch):
    reviewer = MockExtractReviewer()
    command = ReviewCommand(reviewer)

    extracted_data_path = tmp_path / "extracted_data.txt"
    output_path = tmp_path / "output.txt"

    with open(extracted_data_path, "w") as file:
        file.write("extracted section\n\nanother section")

    inputs = iter(["s", "s"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command.execute(extracted_data_path, output_path)

    with open(output_path, "r") as file:
        reviewed_data = file.read()
    
    assert reviewed_data == "extracted section\n\nanother section"
