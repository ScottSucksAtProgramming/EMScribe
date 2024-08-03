import os
import sys
from unittest.mock import MagicMock, mock_open, patch
import pytest
from commands.extract_command import ExtractCommand


@pytest.fixture
def mock_extractor():
    return MagicMock()


@pytest.fixture
def extract_command(mock_extractor):
    return ExtractCommand(mock_extractor)


def test_execute_with_file_path(extract_command, mock_extractor):
    transcript_path = "path/to/transcript.txt"
    output_path = "path/to/output.txt"
    transcript_content = "This is a test transcript."
    extracted_data = "Extracted data."

    mock_extractor.extract.return_value = extracted_data

    m = mock_open(read_data=transcript_content)
    with patch("builtins.open", m):
        with patch("os.makedirs") as mock_makedirs:
            extract_command.execute(transcript_path, output_path)

            # Check if the file was read correctly
            m.assert_any_call(transcript_path, "r")
            # Check if the directory was created
            mock_makedirs.assert_called_with(
                os.path.dirname(output_path), exist_ok=True
            )
            # Check if the file was written correctly
            m.assert_any_call(output_path, "w")
            handle = m()
            handle.write.assert_called_with(extracted_data)


def test_execute_with_stdin(extract_command, mock_extractor):
    transcript_path = "-"
    output_path = "path/to/output.txt"
    transcript_content = "This is a test transcript."
    extracted_data = "Extracted data."

    mock_extractor.extract.return_value = extracted_data

    with patch("builtins.open", mock_open(read_data=transcript_content)) as mock_file:
        with patch("os.makedirs") as mock_makedirs:
            with patch("sys.stdin.read", return_value=transcript_content):
                extract_command.execute(transcript_path, output_path)

                mock_makedirs.assert_called_with(
                    os.path.dirname(output_path), exist_ok=True
                )
                mock_file().write.assert_called_with(extracted_data)


def test_execute_with_no_output_path(extract_command, mock_extractor, capsys):
    transcript_path = "path/to/transcript.txt"
    transcript_content = "This is a test transcript."
    extracted_data = "Extracted data."

    mock_extractor.extract.return_value = extracted_data

    with patch("builtins.open", mock_open(read_data=transcript_content)) as mock_file:
        with patch("pyperclip.copy") as mock_pyperclip:
            extract_command.execute(transcript_path, None)

            captured = capsys.readouterr()
            assert captured.out == extracted_data + "\n"
            mock_pyperclip.assert_called_with(extracted_data)
