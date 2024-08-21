import re
import pdfplumber
from modules.eso_extractor import ESOExtractor


class PDFExtractorFactory:
    @staticmethod
    def get_extractor(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            content = pdf.pages[0].extract_text()

        # Updated regex patterns for Template Version and Data Version
        template_version_pattern = r"Template Version:\s*PCR-\w+-\d+\.\d+\.\d+"
        data_version_pattern = r"Data Version:\s*\d{5}-\w{16}"

        if re.search(template_version_pattern, content) and re.search(
            data_version_pattern, content
        ):
            return ESOExtractor(pdf_path)
        else:
            raise ValueError(
                "Unsupported PDF format or unable to determine the format."
            )
