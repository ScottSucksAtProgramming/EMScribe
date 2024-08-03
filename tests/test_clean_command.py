import pytest
from unittest.mock import MagicMock, patch
from commands.clean_command import CleanCommand
from modules.transcript_cleaner import TranscriptCleaner


@pytest.fixture
def mock_cleaner():
    return MagicMock(spec=TranscriptCleaner)


def test_clean_command_init(mock_cleaner):
    command = CleanCommand(mock_cleaner)
    assert command.cleaner is mock_cleaner


@patch("builtins.open", new_callable=MagicMock)
def test_clean_command_execute(mock_open, mock_cleaner):
    command = CleanCommand(mock_cleaner)
    mock_open.return_value.__enter__.return_value.read.return_value = "Transcript"
    mock_cleaner.clean.return_value = "Cleaned Transcript"

    command.execute("input_path.txt", "output_path.txt")

    mock_open.assert_any_call("input_path.txt", "r")
    mock_cleaner.clean.assert_called_once_with("Transcript")
    mock_open.assert_any_call("output_path.txt", "w")
    mock_open.return_value.__enter__.return_value.write.assert_called_once_with(
        "Cleaned Transcript"
    )
