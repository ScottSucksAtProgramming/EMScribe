import pytest
from unittest.mock import MagicMock, mock_open, patch

from modules.narrative_manager import NarrativeManager
from commands.generate_command import GenerateCommand


@pytest.fixture(name="mock_narrative_manager")
def fixture_mock_narrative_manager():
    return MagicMock(spec=NarrativeManager)


@pytest.fixture(name="generate_command")
def fixture_generate_command(mock_narrative_manager):
    return GenerateCommand(narrative_manager=mock_narrative_manager)


def test_execute_generate_command_to_file(generate_command, mock_narrative_manager):
    """
    Test executing the generate command with valid input and output paths.
    """
    mock_narrative_manager.generate_narrative.return_value = "generated narrative"
    mock_open_function = mock_open(read_data="This is extracted data.")

    with patch("builtins.open", mock_open_function):
        with patch("os.makedirs"):
            generate_command.execute("input_path.txt", "output_path.txt")

    mock_open_function.assert_any_call("input_path.txt", "r")
    mock_open_function.assert_any_call("output_path.txt", "w")
    mock_open_function().write.assert_called_once_with("generated narrative")


def test_execute_generate_command_to_stdout(generate_command, mock_narrative_manager):
    """
    Test executing the generate command with valid input path and no output path.
    """
    mock_narrative_manager.generate_narrative.return_value = "generated narrative"
    mock_open_function = mock_open(read_data="This is extracted data.")

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            generate_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "r")
    mock_print.assert_called_once_with("generated narrative")


def test_execute_generate_command_clipboard(generate_command, mock_narrative_manager):
    """
    Test executing the generate command with valid input path and no output path, using clipboard.
    """
    mock_narrative_manager.generate_narrative.return_value = "generated narrative"
    mock_open_function = mock_open(read_data="This is extracted data.")
    mock_pyperclip = MagicMock()

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            with patch.dict("sys.modules", pyperclip=mock_pyperclip):
                generate_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "r")
    mock_print.assert_called_once_with("generated narrative")
    mock_pyperclip.copy.assert_called_once_with("generated narrative")


def test_execute_generate_command_stdin(generate_command, mock_narrative_manager):
    """
    Test executing the generate command reading from stdin.
    """
    mock_narrative_manager.generate_narrative.return_value = "generated narrative"

    with patch("sys.stdin.read", return_value="This is extracted data."):
        with patch("builtins.print") as mock_print:
            generate_command.execute("-", None)

    mock_print.assert_called_once_with("generated narrative")


def test_execute_generate_command_io_error(generate_command, mock_narrative_manager):
    """
    Test executing the generate command with an IOError.
    """
    mock_narrative_manager.generate_narrative.return_value = "generated narrative"
    mock_open_function = mock_open()
    mock_open_function.side_effect = IOError("File not found")

    with patch("builtins.open", mock_open_function):
        with pytest.raises(IOError, match="Error processing files: File not found"):
            generate_command.execute("input_path.txt", "output_path.txt")


def test_execute_generate_command_import_error(
    generate_command, mock_narrative_manager
):
    """
    Test executing the generate command with an ImportError for pyperclip.
    """
    mock_narrative_manager.generate_narrative.return_value = "generated narrative"
    mock_open_function = mock_open(read_data="This is extracted data.")

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            with patch.dict("sys.modules", {"pyperclip": None}):
                with pytest.raises(ImportError, match="pyperclip module not found"):
                    generate_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "r")
    mock_print.assert_called_once_with("generated narrative")
