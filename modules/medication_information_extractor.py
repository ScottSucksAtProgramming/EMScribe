import pdfplumber
import pandas as pd
from modules.base_pdf_extractor import BasePDFExtractor


class MedicationInformationExtractor(BasePDFExtractor):
    """
    Extracts medication information from a PDF.

    This class inherits from BasePDFExtractor and is responsible for extracting
    information such as medications, allergies, and history from the
    'Medications/Allergies/History/Immunizations' section of the PDF.

    Methods:
        extract(): Extracts medication information from the PDF and returns it as a dictionary.
    """

    def extract(self):
        """
        Extracts medication information from the PDF.

        Returns:
            dict: A dictionary containing the extracted medication information.
        """
        medication_info = {}
        with pdfplumber.open(self.pdf_path) as pdf:
            page = pdf.pages[0]
            tables = page.extract_tables()

            # Iterate through all extracted tables to find the correct one
            for table in tables:
                df = pd.DataFrame(table)

                # Check if the table contains the heading we're interested in
                if (
                    "Medications/Allergies/History/Immunizations"
                    in df.iloc[0, :].values
                ):
                    known_headings = ["Medications/Allergies/History/Immunizations"]
                    split_tables = self.detect_and_split_tables(df, known_headings)

                    medication_df = split_tables.get(
                        "Medications/Allergies/History/Immunizations"
                    )
                    if medication_df is not None:
                        medication_info["Medications"] = self._extract_medications(
                            medication_df
                        )
                        medication_info["Allergies"] = self._extract_allergies(
                            medication_df
                        )
                        medication_info["History"] = self._extract_history(
                            medication_df
                        )
                    break

        return medication_info

    def _extract_medications(self, df):
        return df[df[0] == "Medications"].iloc[0, 1].strip()

    def _extract_allergies(self, df):
        return df[df[0] == "Allergies"].iloc[0, 1].strip()

    def _extract_history(self, df):
        return df[df[0] == "History"].iloc[0, 1].strip()


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"
    extractor = MedicationInformationExtractor(pdf_path)
    medication_info = extractor.extract()

    print("Extracted Medication Information:")
    for key, value in medication_info.items():
        print(f"{key}: {value}")
