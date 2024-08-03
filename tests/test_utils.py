import os
import tempfile

import pytest

from utils.utils import FileManager


def test_read_file():
    # Create a temporary file and write some content to it
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b"Test content")
    temp_file.close()

    try:
        # Use the FileManager to read the file
        content = FileManager.read_file(temp_file.name)
        assert content == "Test content"
    finally:
        os.remove(temp_file.name)


def test_write_file():
    # Create a temporary file path
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, "test_write.txt")

    try:
        # Use the FileManager to write to the file
        FileManager.write_file(temp_file_path, "Test content")

        # Read the file to ensure the content was written
        with open(temp_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        assert content == "Test content"
    finally:
        os.remove(temp_file_path)
        os.rmdir(temp_dir)


def test_ensure_file_exists():
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()

    try:
        # Use the FileManager to check if the file exists
        FileManager.ensure_file_exists(temp_file.name)
    finally:
        os.remove(temp_file.name)


def test_ensure_file_exists_raises_error():
    with pytest.raises(FileNotFoundError):
        FileManager.ensure_file_exists("non_existent_file.txt")
