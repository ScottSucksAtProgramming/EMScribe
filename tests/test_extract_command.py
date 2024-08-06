import pytest
from unittest.mock import MagicMock, mock_open, patch

from modules.transcript_extractor import TranscriptExtractor
from commands.extract_command import ExtractCommand


@pytest.fixture(name="mock_extractor")
def fixture_mock_extractor():
    return MagicMock(spec=TranscriptExtractor)


@pytest.fixture(name="extract_command")
def fixture_extract_command(mock_extractor):
    return ExtractCommand(extractor=mock_extractor)


def test_execute_extract_command_to_file(extract_command, mock_extractor):
    """
    Test executing the extract command with valid input and output paths.
    """
    mock_extractor.extract.return_value = "extracted data"
    mock_open_function = mock_open(read_data="This is a test transcript.")

    with patch("builtins.open", mock_open_function):
        with patch("os.makedirs"):
            extract_command.execute("input_path.txt", "output_path.txt")

    mock_open_function.assert_any_call("input_path.txt", "r")
    mock_open_function.assert_any_call("output_path.txt", "w")
    mock_open_function().write.assert_called_once_with("extracted data")


def test_execute_extract_command_to_stdout(extract_command, mock_extractor):
    """
    Test executing the extract command with valid input path and no output path.
    """
    mock_extractor.extract.return_value = "extracted data"
    mock_open_function = mock_open(read_data="This is a test transcript.")

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            extract_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "r")
    mock_print.assert_called_once_with("extracted data")


def test_execute_extract_command_clipboard(extract_command, mock_extractor):
    """
    Test executing the extract command with valid input path and no output path, using clipboard.
    """
    mock_extractor.extract.return_value = "extracted data"
    mock_open_function = mock_open(read_data="This is a test transcript.")
    mock_pyperclip = MagicMock()

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            with patch.dict("sys.modules", pyperclip=mock_pyperclip):
                extract_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "r")
    mock_print.assert_called_once_with("extracted data")
    mock_pyperclip.copy.assert_called_once_with("extracted data")


def test_execute_extract_command_stdin(extract_command, mock_extractor):
    """
    Test executing the extract command reading from stdin.
    """
    mock_extractor.extract.return_value = "extracted data"

    with patch("sys.stdin.read", return_value="This is a test transcript."):
        with patch("builtins.print") as mock_print:
            extract_command.execute("-", None)

    mock_print.assert_called_once_with("extracted data")


def test_execute_extract_command_io_error(extract_command, mock_extractor):
    """
    Test executing the extract command with an IOError.
    """
    mock_extractor.extract.return_value = "extracted data"
    mock_open_function = mock_open()
    mock_open_function.side_effect = IOError("File not found")

    with patch("builtins.open", mock_open_function):
        with pytest.raises(IOError, match="Error processing files: File not found"):
            extract_command.execute("input_path.txt", "output_path.txt")


def test_execute_extract_command_import_error(extract_command, mock_extractor):
    """
    Test executing the extract command with an ImportError for pyperclip.
    """
    mock_extractor.extract.return_value = "extracted data"
    mock_open_function = mock_open(read_data="This is a test transcript.")

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            with patch.dict("sys.modules", {"pyperclip": None}):
                with pytest.raises(ImportError, match="pyperclip module not found"):
                    extract_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "r")
    mock_print.assert_called_once_with("extracted data")
