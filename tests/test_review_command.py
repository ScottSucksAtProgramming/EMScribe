import pytest
from unittest.mock import MagicMock, patch, mock_open

from modules.extract_reviewer import ExtractReviewer
from commands.review_command import ReviewCommand


@pytest.fixture(name="mock_ExtractReviewer")
def fixture_mock_ExtractReviewer():
    return MagicMock(spec=ExtractReviewer)


@pytest.fixture(name="review_command")
def fixture_review_command(mock_ExtractReviewer):
    return ReviewCommand(ExtractReviewer=mock_ExtractReviewer)


def test_execute_review_command(review_command, mock_ExtractReviewer):
    """
    Test executing the review command with valid input and output paths.
    """
    mock_ExtractReviewer.review_section.side_effect = (
        lambda section, user_input: f"reviewed {section}"
    )
    mock_open_function = mock_open(read_data="Section 1\n\nSection 2")

    user_inputs = iter(["change for section 1", "yes", "s"])
    with patch("builtins.open", mock_open_function):
        with patch("builtins.input", lambda _: next(user_inputs)):
            with patch("os.makedirs"):
                review_command.execute("input_path.txt", "output_path.txt")

    mock_open_function.assert_any_call("input_path.txt", "r")
    mock_open_function.assert_any_call("output_path.txt", "w")
    mock_open_function().write.assert_called_once_with(
        "reviewed Section 1\n\nSection 2"
    )


def test_execute_review_command_io_error(review_command, mock_ExtractReviewer):
    """
    Test executing the review command with an IOError.
    """
    mock_open_function = mock_open()
    mock_open_function.side_effect = IOError("File not found")

    with patch("builtins.open", mock_open_function):
        with pytest.raises(IOError, match="Error processing files: File not found"):
            review_command.execute("input_path.txt", "output_path.txt")


def test_get_user_input(review_command):
    """
    Test getting user input for a section.
    """
    section = "This is a test section."
    with patch("builtins.input", return_value="user input"):
        user_input = review_command.get_user_input(section)
    assert user_input == "user input"


def test_confirm_response(review_command):
    """
    Test confirming AI response.
    """
    response = "This is an AI response."
    with patch("builtins.input", return_value="yes"):
        user_input = review_command.confirm_response(response)
    assert user_input == "yes"
