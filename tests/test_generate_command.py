import sys
import os
from unittest.mock import MagicMock, patch, mock_open

import pytest
from commands.generate_command import GenerateCommand


@pytest.fixture
def mock_narrative_manager():
    return MagicMock()


@pytest.fixture
def generate_command(mock_narrative_manager):
    return GenerateCommand(narrative_manager=mock_narrative_manager)


def test_execute_with_file_path(generate_command, mock_narrative_manager):
    mock_open_instance = mock_open(read_data="extracted data content")

    with patch("builtins.open", mock_open_instance):
        with patch("os.makedirs") as mock_makedirs:
            generate_command.execute("path/to/extracted.txt", "path/to/output.txt")

            mock_open_instance.assert_any_call("path/to/extracted.txt", "r")
            mock_open_instance.assert_any_call("path/to/output.txt", "w")
            mock_narrative_manager.generate_narrative.assert_called_once_with(
                "presoaped_format", data="extracted data content"
            )
            mock_makedirs.assert_called_once_with("path/to", exist_ok=True)


def test_execute_with_stdin(generate_command, mock_narrative_manager):
    mock_narrative_manager.generate_narrative.return_value = "generated narrative"

    with patch("sys.stdin.read", return_value="extracted data from stdin"):
        with patch("builtins.open", mock_open()) as mock_file:
            generate_command.execute("-", "path/to/output.txt")

            mock_narrative_manager.generate_narrative.assert_called_once_with(
                "presoaped_format", data="extracted data from stdin"
            )
            mock_file.assert_any_call("path/to/output.txt", "w")
            mock_file().write.assert_called_once_with("generated narrative")


def test_execute_without_output_path(generate_command, mock_narrative_manager):
    import io

    mock_narrative_manager.generate_narrative.return_value = "generated narrative"

    with patch("builtins.open", mock_open(read_data="extracted data content")):
        with patch("sys.stdout", new_callable=lambda: io.StringIO()) as mock_stdout:
            with patch("pyperclip.copy") as mock_pyperclip_copy:
                generate_command.execute("path/to/extracted.txt", None)

                mock_narrative_manager.generate_narrative.assert_called_once_with(
                    "presoaped_format", data="extracted data content"
                )
                assert mock_stdout.getvalue().strip() == "generated narrative"
                mock_pyperclip_copy.assert_called_once_with("generated narrative")
