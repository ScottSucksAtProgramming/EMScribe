# patient_histories_extractor.py
import pandas as pd
import tabula


class PatientHistoriesExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Find and extract patient histories information
            medical_history = self._extract_medical_history(tables)
            surgical_history = self._extract_surgical_history(tables)
            social_history = self._extract_social_history(tables)
            family_history = self._extract_family_history(tables)
            sexual_history = self._extract_sexual_history(tables)
            medications = self._extract_medications(tables)
            allergies = self._extract_allergies(tables)
        except Exception as e:
            medical_history = surgical_history = social_history = family_history = (
                sexual_history
            ) = medications = allergies = f"Error extracting patient histories: {e}"

        return {
            "Medical History": medical_history,
            "Surgical History": surgical_history,
            "Social History": social_history,
            "Family History": family_history,
            "Sexual History": sexual_history,
            "Medications": medications,
            "Allergies": allergies,
        }

    def _extract_medical_history(self, tables) -> str:
        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(
                str
            )  # Fill NaN with empty string and cast to string type

            for i, row in df.iterrows():
                for j, cell in row.items():
                    if "Medical History" in cell:
                        info_col = df.columns[df.columns.get_loc(j) + 1]
                        medical_history_info = df[info_col].tolist()
                        medical_history_text = ", ".join(
                            [
                                info.strip()
                                for info in medical_history_info
                                if info.strip()
                            ]
                        ).strip()
                        return medical_history_text

        return "[No Info]"

    def _extract_surgical_history(self, tables) -> str:
        # Placeholder method to be implemented
        return "[No Info]"

    def _extract_social_history(self, tables) -> str:
        # Placeholder method to be implemented
        return "[No Info]"

    def _extract_family_history(self, tables) -> str:
        # Placeholder method to be implemented
        return "[No Info]"

    def _extract_sexual_history(self, tables) -> str:
        # Placeholder method to be implemented
        return "[No Info]"

    def _extract_medications(self, tables) -> str:
        # Placeholder method to be implemented
        return "[No Info]"

    def _extract_allergies(self, tables) -> str:
        # Placeholder method to be implemented
        return "[No Info]"


# Example usage
if __name__ == "__main__":
    extractor = PatientHistoriesExtractor()
    pdf_files = [
        "pdf_1.pdf",
        "pdf_2.pdf",
        "pdf_3.pdf",
    ]  # Add paths to your test PDFs here

    for pdf_file in pdf_files:
        result = extractor.extract(pdf_file)
        print(f"Results for {pdf_file}:")
        for key, value in result.items():
            print(f"{key}: {value}")
        print("\n")
