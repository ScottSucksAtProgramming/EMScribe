import pytest
from unittest.mock import MagicMock, mock_open, patch

from modules.transcript_cleaner import TranscriptCleaner
from commands.clean_command import CleanCommand


@pytest.fixture(name="mock_cleaner")
def fixture_mock_cleaner():
    return MagicMock(spec=TranscriptCleaner)


@pytest.fixture(name="clean_command")
def fixture_clean_command(mock_cleaner):
    return CleanCommand(cleaner=mock_cleaner)


def test_execute_clean_command(clean_command, mock_cleaner):
    """
    Test executing the clean command with valid input and output paths.
    """
    mock_cleaner.clean.return_value = "cleaned transcript"
    mock_open_function = mock_open(read_data="This is a test transcript.")

    with patch("builtins.open", mock_open_function):
        clean_command.execute("input_path.txt", "output_path.txt")

    mock_open_function.assert_any_call("input_path.txt", "r")
    mock_open_function.assert_any_call("output_path.txt", "w")
    mock_open_function().write.assert_called_once_with("cleaned transcript")


def test_execute_clean_command_io_error(clean_command, mock_cleaner):
    """
    Test executing the clean command with an IOError.
    """
    mock_cleaner.clean.return_value = "cleaned transcript"
    mock_open_function = mock_open()
    mock_open_function.side_effect = IOError("File not found")

    with patch("builtins.open", mock_open_function):
        with pytest.raises(IOError, match="Error processing files: File not found"):
            clean_command.execute("input_path.txt", "output_path.txt")
