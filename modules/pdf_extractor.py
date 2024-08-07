import pdfplumber
import re


class PDFExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_first_name(self) -> str:
        with pdfplumber.open(self.pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

        # Find the first name in the "Patient Information" section
        match = re.search(r"First\s+(\w+)", text, re.IGNORECASE)
        if match:
            return match.group(1)
        return None


# Example usage
if __name__ == "__main__":
    pdf_extractor = PDFExtractor("Patient Care Record.pdf")
    first_name = pdf_extractor.extract_first_name()
    print(f"Patient's First Name: {first_name}")
