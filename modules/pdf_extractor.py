import pdfplumber
import io
from modules.pdf_extractors.incident_information_extractor import (
    IncidentInformationExtractor,
)
from modules.pdf_extractors.patient_demographics_extractor import (
    PatientDemographicsExtractor,
)


class PDFExtractor:
    def __init__(self, model_loader, prompt_manager):
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager
        self.incident_information_extractor = IncidentInformationExtractor()
        self.patient_demographics_extractor = PatientDemographicsExtractor()

    def extract(self, content: bytes) -> dict:
        text = self._extract_text(content)
        data = {
            "Incident Information": self.incident_information_extractor.extract(text),
            "Patient Demographics": self.patient_demographics_extractor.extract(text),
            # Add other sections here
        }
        return data

    def _extract_text(self, content: bytes) -> str:
        text = ""
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                text += page_text + "\n"
        return text
