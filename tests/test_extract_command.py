from unittest.mock import patch, mock_open, MagicMock
import pytest
from commands.extract_command import ExtractCommand
import os


@pytest.fixture
def mock_extractor():
    return MagicMock()


@pytest.fixture
def extract_command(mock_extractor):
    return ExtractCommand(extractor=mock_extractor)


def test_execute_with_clipboard(mock_extractor, extract_command):
    extracted_data = "extracted information"
    mock_extractor.extract.return_value = extracted_data
    mock_open_read = mock_open(read_data="transcript content")

    with patch("builtins.open", mock_open_read):
        with patch("pyperclip.copy") as mock_copy:
            extract_command.execute("path/to/transcript.txt", None)

            # Ensure read operation
            mock_open_read.assert_any_call("path/to/transcript.txt", "r")

            # Ensure the data is copied to clipboard
            mock_copy.assert_called_once_with(extracted_data)


def test_execute_with_file_path(mock_extractor, extract_command):
    extracted_data = "extracted information"
    mock_extractor.extract.return_value = extracted_data
    mock_open_rw = mock_open()

    with patch("builtins.open", mock_open_rw):
        with patch("os.makedirs") as mock_makedirs:
            extract_command.execute("path/to/transcript.txt", "data/extract.txt")

            # Ensure read operation
            mock_open_rw.assert_any_call("path/to/transcript.txt", "r")

            # Ensure write operation
            mock_open_rw.assert_any_call("data/extract.txt", "w")
            mock_open_rw().write.assert_called_once_with(extracted_data)

            # Ensure directories were created
            mock_makedirs.assert_called_once_with(
                os.path.dirname("data/extract.txt"), exist_ok=True
            )
