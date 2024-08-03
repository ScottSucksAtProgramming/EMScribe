# -*- coding: utf-8 -*-
# tests/test_cli.py

import sys
import tempfile
from unittest.mock import patch
from scripts.cli import main


def test_clean_command():
    with tempfile.NamedTemporaryFile(delete=False) as temp_transcript:
        temp_transcript.write(b"Sample transcript text")
        temp_transcript.flush()
        transcript_path = temp_transcript.name

    with tempfile.NamedTemporaryFile(delete=False) as temp_cleaned:
        cleaned_path = temp_cleaned.name

    with patch.object(
        sys, "argv", ["cli.py", "clean", transcript_path, "--output", cleaned_path]
    ):
        main()

    with open(cleaned_path, "r", encoding="utf-8") as file:
        cleaned_transcript = file.read()

    assert "Sample transcript text" in cleaned_transcript


def test_extract_command():
    with tempfile.NamedTemporaryFile(delete=False) as temp_transcript:
        temp_transcript.write(b"Sample transcript text")
        temp_transcript.flush()
        transcript_path = temp_transcript.name

    with tempfile.NamedTemporaryFile(delete=False) as temp_extracted:
        extracted_path = temp_extracted.name

    with patch.object(
        sys, "argv", ["cli.py", "extract", transcript_path, "--output", extracted_path]
    ):
        main()

    with open(extracted_path, "r", encoding="utf-8") as file:
        extracted_data = file.read()

    assert (
        "Sample extracted data" in extracted_data
    )  # Adjust this as per the actual extraction logic


def test_generate_command():
    with tempfile.NamedTemporaryFile(delete=False) as temp_transcript:
        temp_transcript.write(b"Sample extracted data")
        temp_transcript.flush()
        transcript_path = temp_transcript.name

    with tempfile.NamedTemporaryFile(delete=False) as temp_narrative:
        narrative_path = temp_narrative.name

    with patch.object(
        sys, "argv", ["cli.py", "generate", transcript_path, "--output", narrative_path]
    ):
        main()

    with open(narrative_path, "r", encoding="utf-8") as file:
        narrative = file.read()

    assert (
        "Sample narrative text" in narrative
    )  # Adjust this as per the actual narrative generation logic


def test_review_command():
    with tempfile.NamedTemporaryFile(delete=False) as temp_transcript:
        temp_transcript.write(b"Sample extracted data")
        temp_transcript.flush()
        transcript_path = temp_transcript.name

    with tempfile.NamedTemporaryFile(delete=False) as temp_reviewed:
        reviewed_path = temp_reviewed.name

    with patch.object(
        sys, "argv", ["cli.py", "review", transcript_path, "--output", reviewed_path]
    ):
        main()

    with open(reviewed_path, "r", encoding="utf-8") as file:
        reviewed_data = file.read()

    assert (
        "Sample reviewed data" in reviewed_data
    )  # Adjust this as per the actual review logic
