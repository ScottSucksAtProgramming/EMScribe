import pdfplumber
import pandas as pd
from dataclasses import dataclass, field
from modules.base_pdf_extractor import BasePDFExtractor


@dataclass
class HistoryOfPresentIllness:
    chief_complaint: str = field(default="")
    symptom_onset: str = field(default="")
    last_known_well: str = field(default="")
    associated_signs_and_symptoms: str = field(default="")


class HPIExtractor(BasePDFExtractor):
    def __init__(self, pdf_path):
        super().__init__(pdf_path)
        self.hpi = HistoryOfPresentIllness()

    def extract_chief_complaint(self, df):
        """Extracts Chief Complaint."""
        chief_complaint_row = df[df[4].str.contains("Chief Complaint", na=False)]
        if not chief_complaint_row.empty:
            chief_complaint = chief_complaint_row.iloc[0, 5].replace("\n", " ").strip()
            self.hpi.chief_complaint = chief_complaint

    def extract_symptom_onset(self, df):
        """Extracts Symptom Onset (Onset Time)."""
        onset_row = df[df[4].str.contains("Onset Time", na=False)]
        if not onset_row.empty:
            self.hpi.symptom_onset = onset_row.iloc[0, 5].strip()

    def extract_last_known_well(self, df):
        """Extracts Last Known Well."""
        lkw_row = df[df[4].str.contains("Last Known Well", na=False)]
        if not lkw_row.empty:
            self.hpi.last_known_well = lkw_row.iloc[0, 5].strip()

    def extract_signs_and_symptoms(self, df):
        """Extracts Associated Signs & Symptoms."""
        symptoms_row = df[df[4].str.contains("Signs & Symptoms", na=False)]
        if not symptoms_row.empty:
            self.hpi.associated_signs_and_symptoms = (
                symptoms_row.iloc[0, 5].replace("\n", ", ").strip()
            )

    def extract(self):
        """
        Extracts all relevant information from the clinical impression table.
        """
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table)
                    if "Clinical Impression" in df.values:
                        self.extract_chief_complaint(df)
                        self.extract_symptom_onset(df)
                        self.extract_last_known_well(df)
                        self.extract_signs_and_symptoms(df)
                        break

        # Ensure all fields are printed, even if they are not extracted
        return {
            "Chief Complaint": self.hpi.chief_complaint,
            "Symptom Onset": self.hpi.symptom_onset,
            "Last Known Well": self.hpi.last_known_well,
            "Associated Signs and Symptoms": self.hpi.associated_signs_and_symptoms,  # Fixed the key
            "Onset": "",  # Placeholder for data that isn't extracted
            "Provocation": "",  # Placeholder for data that isn't extracted
            "Palliation": "",  # Placeholder for data that isn't extracted
            "Quality": "",  # Placeholder for data that isn't extracted
            "Radiation": "",  # Placeholder for data that isn't extracted
            "Severity": "",  # Placeholder for data that isn't extracted
            "Time": "",  # Placeholder for data that isn't extracted
            "Interventions": "",  # Placeholder for data that isn't extracted
            "Additional History of Present Illness Information": "",  # Placeholder for data that isn't extracted
        }


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"  # Path to your PDF file
    extractor = HPIExtractor(pdf_path)
    hpi_info = extractor.extract()
    print("History of Present Illness:")
    print(f"Chief Complaint: {hpi_info['Chief Complaint']}")
    print(f"Symptom Onset: {hpi_info['Symptom Onset']}")
    print(f"Last Known Well: {hpi_info['Last Known Well']}")
    print(f"Associated Signs and Symptoms: {hpi_info['Associated Signs and Symptoms']}")
    print(f"Onset: {hpi_info['Onset']}")
    print(f"Provocation: {hpi_info['Provocation']}")
    print(f"Palliation: {hpi_info['Palliation']}")
    print(f"Quality: {hpi_info['Quality']}")
    print(f"Radiation: {hpi_info['Radiation']}")
    print(f"Severity: {hpi_info['Severity']}")
    print(f"Time: {hpi_info['Time']}")
    print(f"Interventions: {hpi_info['Interventions']}")
    print(
        f"Additional History of Present Illness Information: {hpi_info['Additional History of Present Illness Information']}"
    )
