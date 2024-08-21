import pdfplumber
import pandas as pd
from dataclasses import dataclass, field
from modules.base_pdf_extractor import BasePDFExtractor


@dataclass
class PatientHistories:
    medical_history: str = field(default="")
    surgical_history: str = field(default="")
    social_history: str = field(default="")
    family_history: str = field(default="")
    sexual_history: str = field(default="")
    medications: str = field(default="")
    allergies: str = field(default="")


class PatientHistoriesExtractor(BasePDFExtractor):
    def __init__(self, pdf_path):
        super().__init__(pdf_path)
        self.histories = PatientHistories()

    def _extract_medical_history(self, df):
        """Extracts Medical History."""
        try:
            self.histories.medical_history = df[df[0] == "History"].iloc[0, 1].strip()
        except IndexError:
            self.histories.medical_history = ""

    def _extract_medications(self, df):
        """Extracts Medications."""
        try:
            self.histories.medications = df[df[0] == "Medications"].iloc[0, 1].strip()
        except IndexError:
            self.histories.medications = ""

    def _extract_allergies(self, df):
        """Extracts Allergies."""
        try:
            self.histories.allergies = df[df[0] == "Allergies"].iloc[0, 1].strip()
        except IndexError:
            self.histories.allergies = ""

    def extract(self):
        """
        Extracts all relevant information from the medications/allergies/history table.
        """
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table)
                    if (
                        "Medications/Allergies/History/Immunizations"
                        in df.iloc[0, :].values
                    ):
                        known_headings = ["Medications/Allergies/History/Immunizations"]
                        split_tables = self.detect_and_split_tables(df, known_headings)

                        history_df = split_tables.get(
                            "Medications/Allergies/History/Immunizations"
                        )
                        if history_df is not None:
                            self._extract_medical_history(history_df)
                            self._extract_medications(history_df)
                            self._extract_allergies(history_df)
                        break

        # Return all fields, even if they are not extracted
        return {
            "Medical History": self.histories.medical_history,
            "Surgical History": self.histories.surgical_history,  # Empty by default
            "Social History": self.histories.social_history,  # Empty by default
            "Family History": self.histories.family_history,  # Empty by default
            "Sexual History": self.histories.sexual_history,  # Empty by default
            "Medications": self.histories.medications,
            "Allergies": self.histories.allergies,
        }


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"  # Path to your PDF file
    extractor = PatientHistoriesExtractor(pdf_path)
    histories_info = extractor.extract()
    print("Patient Histories:")
    print(f"Medical History: {histories_info['Medical History']}")
    print(f"Surgical History: {histories_info['Surgical History']}")
    print(f"Social History: {histories_info['Social History']}")
    print(f"Family History: {histories_info['Family History']}")
    print(f"Sexual History: {histories_info['Sexual History']}")
    print(f"Medications: {histories_info['Medications']}")
    print(f"Allergies: {histories_info['Allergies']}")
