import sys
from unittest.mock import MagicMock, patch

import pytest

from scripts.cli import initialize_components, main, parse_args


def test_initialize_components():
    cleaner, extractor, narrative_manager, extract_reviewer = initialize_components()
    assert cleaner is not None
    assert extractor is not None
    assert narrative_manager is not None
    assert extract_reviewer is not None


def test_parse_args_clean():
    test_args = ["clean", "path/to/transcript"]
    with patch.object(sys, "argv", ["emscribe"] + test_args):
        args = parse_args()
        assert args.command == "clean"
        assert args.transcript_path == "path/to/transcript"
        assert args.output == "data/cleaned_transcript.txt"


def test_parse_args_extract():
    test_args = ["extract", "path/to/transcript"]
    with patch.object(sys, "argv", ["emscribe"] + test_args):
        args = parse_args()
        assert args.command == "extract"
        assert args.transcript_path == "path/to/transcript"
        assert args.output == "data/extract.txt"


def test_parse_args_generate():
    test_args = ["generate", "path/to/extracted"]
    with patch.object(sys, "argv", ["emscribe"] + test_args):
        args = parse_args()
        assert args.command == "generate"
        assert args.transcript_path == "path/to/extracted"
        assert args.output == "data/narrative.txt"


def test_parse_args_review():
    test_args = ["review", "path/to/extracted"]
    with patch.object(sys, "argv", ["emscribe"] + test_args):
        args = parse_args()
        assert args.command == "review"
        assert args.extracted_data_path == "path/to/extracted"
        assert args.output == "data/reviewed_extract.txt"


@patch("scripts.cli.CleanCommand")
@patch("scripts.cli.ExtractCommand")
@patch("scripts.cli.GenerateCommand")
@patch("scripts.cli.ReviewCommand")
@patch("scripts.cli.initialize_components")
def test_main(mock_initialize, mock_review, mock_generate, mock_extract, mock_clean):
    mock_initialize.return_value = (MagicMock(), MagicMock(), MagicMock(), MagicMock())

    test_args = ["clean", "path/to/transcript"]
    with patch.object(sys, "argv", ["emscribe"] + test_args):
        main()
        mock_clean.assert_called_once()

    test_args = ["extract", "path/to/transcript"]
    with patch.object(sys, "argv", ["emscribe"] + test_args):
        main()
        mock_extract.assert_called_once()

    test_args = ["generate", "path/to/extracted"]
    with patch.object(sys, "argv", ["emscribe"] + test_args):
        main()
        mock_generate.assert_called_once()

    test_args = ["review", "path/to/extracted"]
    with patch.object(sys, "argv", ["emscribe"] + test_args):
        main()
        mock_review.assert_called_once()


if __name__ == "__main__":
    pytest.main()
