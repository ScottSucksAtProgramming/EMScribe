import pytest
from unittest.mock import MagicMock, mock_open, patch

from modules.transcript_extractor import TranscriptExtractor
from modules.pdf_extractor import PDFExtractor
from commands.extract_command import ExtractCommand


@pytest.fixture(name="mock_extractor")
def fixture_mock_extractor():
    return MagicMock(spec=TranscriptExtractor)


@pytest.fixture(name="mock_pdf_extractor")
def fixture_mock_pdf_extractor():
    return MagicMock(spec=PDFExtractor)


@pytest.fixture(name="extract_command")
def fixture_extract_command(mock_extractor, mock_pdf_extractor):
    return ExtractCommand(
        transcript_extractor=mock_extractor, pdf_extractor=mock_pdf_extractor
    )


def test_execute_extract_command_to_file(extract_command, mock_extractor):
    """
    Test executing the extract command with valid input and output paths.
    """
    mock_extractor.extract.return_value = "extracted data"
    mock_open_function = mock_open(read_data=b"This is a test transcript.")

    with patch("builtins.open", mock_open_function):
        with patch("os.makedirs"):
            extract_command.execute("input_path.txt", "output_path.txt")

    mock_open_function.assert_any_call("input_path.txt", "rb")
    mock_open_function.assert_any_call("output_path.txt", "w")
    mock_open_function().write.assert_called_once_with("extracted data")


def test_execute_extract_command_to_stdout(extract_command, mock_extractor):
    """
    Test executing the extract command with valid input path and no output path.
    """
    mock_extractor.extract.return_value = "extracted data"
    mock_open_function = mock_open(read_data=b"This is a test transcript.")

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            extract_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "rb")
    mock_print.assert_any_call("extracted data")


def test_execute_extract_command_clipboard(extract_command, mock_extractor):
    """
    Test executing the extract command with valid input path and no output path, using clipboard.
    """
    mock_extractor.extract.return_value = "extracted data"
    mock_open_function = mock_open(read_data=b"This is a test transcript.")
    mock_pyperclip = MagicMock()

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            with patch.dict("sys.modules", pyperclip=mock_pyperclip):
                extract_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "rb")
    mock_print.assert_any_call("extracted data")
    mock_pyperclip.copy.assert_called_once_with("extracted data")


def test_execute_extract_command_stdin(extract_command, mock_extractor):
    """
    Test executing the extract command reading from stdin.
    """
    mock_extractor.extract.return_value = "extracted data"

    with patch("sys.stdin.read", return_value="This is a test transcript."):
        with patch("builtins.print") as mock_print:
            extract_command.execute("-", None)

    mock_print.assert_any_call("extracted data")


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
    mock_open_function = mock_open(read_data=b"This is a test transcript.")

    with patch("builtins.open", mock_open_function):
        with patch("builtins.print") as mock_print:
            with patch.dict("sys.modules", {"pyperclip": None}):
                with pytest.raises(ImportError, match="pyperclip module not found"):
                    extract_command.execute("input_path.txt", None)

    mock_open_function.assert_called_once_with("input_path.txt", "rb")
    mock_print.assert_any_call("extracted data")


def test_execute_extract_command_with_pdf(extract_command, mock_pdf_extractor):
    """
    Test executing the extract command with a PDF input path.
    """
    mock_pdf_extractor.extract.return_value = {
        "Incident Information": {
            "Unit": "5-41-19",
            "Response Mode": "Non-Emergent",
            "Crew Type": "Full Crew",
            "Response Delays": "None/No Delay",
            "Incident Location": "Hospital in Stony Brook",
            "Dispatch Complaint": "Transfer/Interfacility/Palliative Care",
        },
        "Patient Demographics": {
            "Name": "Richard",
            "Date of Birth": "04/05/1940",
            "Age": "84 Yrs",
            "Gender": "Male",
        },
    }
    mock_open_function = mock_open(read_data=b"This is a test PDF content.")

    with patch("builtins.open", mock_open_function):
        with patch("os.makedirs"):
            extract_command.execute("input_path.pdf", "output_path.txt")

    mock_open_function.assert_any_call("input_path.pdf", "rb")
    mock_open_function.assert_any_call("output_path.txt", "w")
    mock_open_function().write.assert_called_once_with(
        "Incident Information:\n"
        "Unit: 5-41-19\n"
        "Response Mode: Non-Emergent\n"
        "Crew Type: Full Crew\n"
        "Response Delays: None/No Delay\n"
        "Incident Location: Hospital in Stony Brook\n"
        "Dispatch Complaint: Transfer/Interfacility/Palliative Care\n\n"
        "Patient Demographics:\n"
        "Name: Richard\n"
        "Date of Birth: 04/05/1940\n"
        "Age: 84 Yrs\n"
        "Gender: Male\n\n"
    )


def test_format_extracted_data(extract_command):
    """
    Test the _format_extracted_data method.
    """
    data = {
        "Incident Information": {
            "Unit": "5-41-19",
            "Response Mode": "Non-Emergent",
            "Crew Type": "Full Crew",
            "Response Delays": "None/No Delay",
            "Incident Location": "Hospital in Stony Brook",
            "Dispatch Complaint": "Transfer/Interfacility/Palliative Care",
        },
        "Patient Demographics": {
            "Name": "Richard",
            "Date of Birth": "04/05/1940",
            "Age": "84 Yrs",
            "Gender": "Male",
        },
    }
    formatted_data = extract_command._format_extracted_data(data)
    expected_output = (
        "Incident Information:\n"
        "Unit: 5-41-19\n"
        "Response Mode: Non-Emergent\n"
        "Crew Type: Full Crew\n"
        "Response Delays: None/No Delay\n"
        "Incident Location: Hospital in Stony Brook\n"
        "Dispatch Complaint: Transfer/Interfacility/Palliative Care\n\n"
        "Patient Demographics:\n"
        "Name: Richard\n"
        "Date of Birth: 04/05/1940\n"
        "Age: 84 Yrs\n"
        "Gender: Male\n\n"
    )
    assert formatted_data == expected_output


def test_execute_extract_command_unsupported_file_type(extract_command):
    """
    Test executing the extract command with an unsupported file type.
    """
    with patch("builtins.open", mock_open(read_data=b"")):
        with patch("os.path.splitext", return_value=(".unsupported", ".unsupported")):
            with pytest.raises(
                ValueError,
                match="Unsupported file type. Only .txt and .pdf files are supported.",
            ):
                extract_command.execute("input_path.unsupported", None)
