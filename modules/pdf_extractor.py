import io
import os
import pdfplumber

from modules.pdf_extractors.history_of_present_illness_extractor import (
    HistoryOfPresentIllnessExtractor,
)
from modules.pdf_extractors.incident_information_extractor import (
    IncidentInformationExtractor,
)
from modules.pdf_extractors.patient_demographics_extractor import (
    PatientDemographicsExtractor,
)
from modules.pdf_extractors.subjective_information_extractor import (
    SubjectiveInformationExtractor,
)
from modules.pdf_extractors.patient_histories_extractor import (
    PatientHistoriesExtractor,
)


class PDFExtractor:
    def __init__(self, model_loader, prompt_manager):
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager
        self.incident_information_extractor = IncidentInformationExtractor()
        self.patient_demographics_extractor = PatientDemographicsExtractor()
        self.subjective_information_extractor = SubjectiveInformationExtractor()
        self.history_of_present_illness_extractor = HistoryOfPresentIllnessExtractor()
        self.patient_histories_extractor = PatientHistoriesExtractor()

    def extract(self, content: bytes) -> dict:
        temp_pdf_path = "temp_pdf.pdf"
        with open(temp_pdf_path, "wb") as f:
            f.write(content)

        text = self._extract_text(temp_pdf_path)
        data = {
            "Incident Information": self.incident_information_extractor.extract(text),
            "Patient Demographics": self.patient_demographics_extractor.extract(text),
            "Subjective Information": self.subjective_information_extractor.extract(
                text
            ),
            "History of Present Illness": self.history_of_present_illness_extractor.extract(
                temp_pdf_path
            ),
            "Patient Histories": self.patient_histories_extractor.extract(
                temp_pdf_path
            ),
        }

        os.remove(temp_pdf_path)
        return data

    def _extract_text(self, pdf_path: str) -> str:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                text += page_text + "\n"
        return text

    def format_extracted_data(self, data: dict) -> str:
        formatted_data = []
        for section, content in data.items():
            formatted_data.append(f"{section}:")
            for key, value in content.items():
                formatted_data.append(f"{key}: {value}")
            formatted_data.append("")  # Add a newline between sections
        return "\n".join(formatted_data).replace("\n\n", "\n")  # Remove extra newlines


# Example usage
if __name__ == "__main__":
    with open("pdf_1.pdf", "rb") as file:
        content = file.read()
    pdf_extractor = PDFExtractor(None, None)
    extracted_data = pdf_extractor.extract(content)
    formatted_data = pdf_extractor.format_extracted_data(extracted_data)
    print(formatted_data)
