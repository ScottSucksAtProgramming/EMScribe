from abc import ABC, abstractmethod


class BasePDFExtractor(ABC):
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    @abstractmethod
    def extract_patient_information(self):
        """Extracts patient information from the PDF."""
        pass

    @abstractmethod
    def extract_medication_info(self):
        """Extracts medication information from the PDF."""
        pass

    @abstractmethod
    def extract_clinical_impression(self):
        """Extracts clinical impression information from the PDF."""
        pass

    @abstractmethod
    def extract_all(self):
        """Extracts all relevant information from the PDF."""
        pass
