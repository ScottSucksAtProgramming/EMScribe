import os


class FileManager:
    """
    A class to handle file operations including reading, writing, and checking the existence of files.
    """

    @staticmethod
    def read_file(file_path: str) -> str:
        """
        Reads the content of a file and returns it as a string.

        Args:
            file_path (str): The path to the file to read.

        Returns:
            str: The content of the file.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        """
        Writes content to a file.

        Args:
            file_path (str): The path to the file to write.
            content (str): The content to write to the file.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def ensure_file_exists(file_path: str) -> None:
        """
        Ensures that the specified file exists.

        Args:
            file_path (str): The path to the file to check.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
