import pdfplumber


class PDFExtractor:
    """
    A class to extract text from a PDF file using pdfplumber.

    Attributes:
        file_path (str): The path to the PDF file from which to extract text.
    """

    def __init__(self, file_path: str):
        """
        Initializes the PDFExtractor with the path to the PDF file.

        Args:
            file_path (str): The path to the PDF file from which to extract text.
        """
        self.file_path = file_path

    def extract_text(self) -> str:
        """
        Extracts all text from the PDF file.

        This method opens the PDF file, iterates over all its pages, and extracts
        the text content from each page. The text from all pages is concatenated
        into a single string.

        Returns:
            str: The extracted text from the entire PDF file, with each page's content
            separated by a newline.
        """
        with pdfplumber.open(self.file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text


if __name__ == "__main__":
    # Example usage
    file_path = "data/pdf_2.pdf"  # Path to your PDF file
    extractor = PDFExtractor(file_path)
    text = extractor.extract_text()
    print(text)
