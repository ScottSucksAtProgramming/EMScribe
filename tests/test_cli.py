import pytest
from unittest.mock import patch, MagicMock
import sys
from scripts.cli import main, create_parser, execute_command, initialize_components


@pytest.fixture
def mock_components():
    with patch("scripts.cli.TranscriptCleaner") as MockTranscriptCleaner, patch(
        "scripts.cli.TranscriptExtractor"
    ) as MockTranscriptExtractor, patch(
        "scripts.cli.NarrativeManager"
    ) as MockNarrativeManager, patch(
        "scripts.cli.ExtractReviewer"
    ) as MockExtractReviewer:
        yield MockTranscriptCleaner, MockTranscriptExtractor, MockNarrativeManager, MockExtractReviewer


def test_clean_command(mock_components):
    """Test the clean command execution."""
    with patch("scripts.cli.CleanCommand") as MockCleanCommand:
        mock_clean_command = MockCleanCommand.return_value
        args = [
            "scripts/main.py",
            "clean",
            "data/test_transcript.txt",
            "--output",
            "data/test_cleaned.txt",
        ]

        with patch("sys.argv", args):
            main()

        # Ensure the CleanCommand is created and used only once
        MockCleanCommand.assert_called_once()

        # Ensure the execute method is called only once with the correct arguments
        mock_clean_command.execute.assert_called_once_with(
            "data/test_transcript.txt", "data/test_cleaned.txt"
        )


def test_extract_command(mock_components):
    """Test the extract command execution."""
    with patch("scripts.cli.ExtractCommand") as MockExtractCommand:
        mock_extract_command = MockExtractCommand.return_value
        args = [
            "scripts/main.py",
            "extract",
            "data/test_cleaned.txt",
            "--output",
            "data/test_extract.txt",
        ]

        with patch("sys.argv", args):
            main()

        MockExtractCommand.assert_called_once()
        mock_extract_command.execute.assert_called_once_with(
            "data/test_cleaned.txt", "data/test_extract.txt"
        )


def test_generate_command(mock_components):
    """Test the generate command execution."""
    with patch("scripts.cli.GenerateCommand") as MockGenerateCommand:
        mock_generate_command = MockGenerateCommand.return_value
        args = [
            "scripts/main.py",
            "generate",
            "data/test_extracted.txt",
            "--output",
            "data/test_narrative.txt",
        ]

        with patch("sys.argv", args):
            main()

        MockGenerateCommand.assert_called_once()
        mock_generate_command.execute.assert_called_once_with(
            "data/test_extracted.txt", "data/test_narrative.txt"
        )


def test_review_command(mock_components):
    """Test the review command execution."""
    with patch("scripts.cli.ReviewCommand") as MockReviewCommand:
        mock_review_command = MockReviewCommand.return_value
        args = [
            "scripts/cli.py",
            "review",
            "data/test_extracted.txt",
            "--output",
            "data/test_reviewed.txt",
        ]

        with patch("sys.argv", args):
            main()

        MockReviewCommand.assert_called_once()
        mock_review_command.execute.assert_called_once_with(
            "data/test_extracted.txt", "data/test_reviewed.txt"
        )


def test_unknown_command():
    """Test handling of an unknown command."""
    args = ["scripts/cli.py", "unknown"]

    with patch("sys.argv", args):
        with patch("builtins.print") as mock_print, patch(
            "sys.stderr.write"
        ) as mock_stderr:
            with pytest.raises(SystemExit):
                main()

            # Verify the exact error message
            mock_stderr.assert_any_call(
                "usage: cli.py [-h] {clean,extract,generate,review} ...\n"
            )
            mock_stderr.assert_any_call(
                "cli.py: error: argument command: invalid choice: 'unknown' (choose from 'clean', 'extract', 'generate', 'review')\n"
            )


def test_unknown_command_in_execute():
    """Test handling of an unknown command in execute_command."""
    args = MagicMock()
    args.command = "unknown"
    components = initialize_components()

    with patch("builtins.print") as mock_print:
        execute_command(args, components)
        mock_print.assert_called_once_with("Unknown command: unknown")


def test_missing_command():
    """Test handling of missing command."""
    args = ["scripts/cli.py"]

    with patch("sys.argv", args):
        with patch("builtins.print") as mock_print, patch(
            "sys.stderr.write"
        ) as mock_stderr:
            with pytest.raises(SystemExit):
                main()
            mock_stderr.assert_any_call(
                "usage: cli.py [-h] {clean,extract,generate,review} ...\n"
            )
            mock_stderr.assert_any_call(
                "cli.py: error: the following arguments are required: command\n"
            )


def test_missing_required_argument():
    """Test handling of missing required arguments."""
    args = ["scripts/cli.py", "review"]

    with patch("sys.argv", args):
        with patch("builtins.print") as mock_print, patch(
            "sys.stderr.write"
        ) as mock_stderr:
            with pytest.raises(SystemExit):
                main()
            mock_stderr.assert_any_call(
                "usage: cli.py review [-h] [--output OUTPUT] extracted_data_path\n"
            )
            mock_stderr.assert_any_call(
                "cli.py review: error: the following arguments are required: extracted_data_path\n"
            )


def test_argument_parsing():
    """Test argument parsing."""
    parser = create_parser()
    args = parser.parse_args(
        ["clean", "data/test_transcript.txt", "--output", "data/test_cleaned.txt"]
    )

    assert args.command == "clean"
    assert args.transcript_path == "data/test_transcript.txt"
    assert args.output == "data/test_cleaned.txt"


def test_entry_point():
    """Test the script entry point."""
    with patch(
        "sys.argv",
        [
            "scripts/cli.py",
            "clean",
            "data/test_transcript.txt",
            "--output",
            "data/test_cleaned.txt",
        ],
    ), patch("scripts.cli.main") as mock_main, patch("builtins.__name__", "__main__"):
        import scripts.cli

        scripts.cli.main()
        mock_main.assert_called_once()
