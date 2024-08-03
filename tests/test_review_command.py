import os
from unittest.mock import MagicMock, patch, mock_open
import pytest
from commands.review_command import ReviewCommand


@pytest.fixture
def mock_reviewer():
    return MagicMock()


@pytest.fixture
def review_command(mock_reviewer):
    return ReviewCommand(reviewer=mock_reviewer)


def test_execute_with_file_path(review_command, mock_reviewer):
    extracted_data = "Section 1\n\nSection 2"
    reviewed_section1 = "Reviewed Section 1"
    reviewed_section2 = "Reviewed Section 2"

    mock_reviewer.review_section.side_effect = [reviewed_section1, reviewed_section2]

    mock_open_file = mock_open(read_data=extracted_data)
    mock_open_write = mock_open()

    with patch("builtins.open", mock_open_file):
        with patch("os.makedirs") as mock_makedirs:
            with patch("builtins.input", side_effect=["edit", "yes", "skip"]):
                with patch("os.system") as mock_system:
                    review_command.execute(
                        "path/to/extracted.txt", "path/to/output.txt"
                    )

    mock_open_file.assert_any_call("path/to/extracted.txt", "r")
    mock_open_file.assert_any_call("path/to/output.txt", "w")
    mock_makedirs.assert_called_once_with("path/to", exist_ok=True)
    mock_reviewer.review_section.assert_any_call("Section 1", "edit")
    handle = mock_open_file()
    handle.write.assert_called_once_with("Reviewed Section 1\n\nSection 2")


def test_get_user_input(review_command):
    section = "Test Section"
    with patch("builtins.input", return_value="user input"):
        with patch("os.system") as mock_system:
            user_input = review_command.get_user_input(section)
            assert user_input == "user input"
            mock_system.assert_called_once_with("clear")


def test_confirm_response(review_command):
    response = "Test Response"
    with patch("builtins.input", return_value="yes"):
        with patch("os.system") as mock_system:
            user_confirmation = review_command.confirm_response(response)
            assert user_confirmation == "yes"
            mock_system.assert_called_once_with("clear")
