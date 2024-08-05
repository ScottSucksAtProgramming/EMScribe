import os
import pytest
from utils.utils import FileManager


@pytest.fixture(name="test_file_path")
def fixture_test_file_path(tmpdir):
    return os.path.join(tmpdir, "test_file.txt")


@pytest.fixture(name="test_content")
def fixture_test_content():
    return "This is a test content."


def test_read_file(test_file_path, test_content):
    # Setup
    FileManager.write_file(test_file_path, test_content)

    # Test read_file
    content = FileManager.read_file(test_file_path)
    assert content == test_content


def test_write_file(test_file_path, test_content):
    # Test write_file
    FileManager.write_file(test_file_path, test_content)

    # Verify
    with open(test_file_path, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == test_content


def test_ensure_file_exists(test_file_path, test_content):
    # Setup
    FileManager.write_file(test_file_path, test_content)

    # Test ensure_file_exists
    try:
        FileManager.ensure_file_exists(test_file_path)
    except FileNotFoundError:
        pytest.fail("FileNotFoundError raised unexpectedly.")


def test_ensure_file_exists_raises_error():
    # Test ensure_file_exists raises error
    with pytest.raises(FileNotFoundError):
        FileManager.ensure_file_exists("non_existent_file.txt")


def test_write_and_read_empty_file(test_file_path):
    # Test writing and reading an empty file
    FileManager.write_file(test_file_path, "")
    content = FileManager.read_file(test_file_path)
    assert content == ""
