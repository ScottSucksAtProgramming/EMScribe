import pandas as pd
import tabula


class PatientHistoriesExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Find and extract patient histories
            patient_histories = self.extract_histories(tables)
        except Exception as e:
            patient_histories = {
                "Medical History": f"Error extracting patient histories: {e}",
                "Medications": f"Error extracting patient histories: {e}",
                "Allergies": f"Error extracting patient histories: {e}",
            }

        return {
            "Medical History": patient_histories.get("Medical History", "[No Info]"),
            "Surgical History": patient_histories.get("Surgical History", "[No Info]"),
            "Social History": patient_histories.get("Social History", "[No Info]"),
            "Family History": patient_histories.get("Family History", "[No Info]"),
            "Sexual History": patient_histories.get("Sexual History", "[No Info]"),
            "Medications": patient_histories.get("Medications", "[No Info]"),
            "Allergies": patient_histories.get("Allergies", "[No Info]"),
        }

    def extract_histories(self, tables) -> dict:
        histories = {
            "Medical History": "[No Info]",
            "Surgical History": "[No Info]",
            "Social History": "[No Info]",
            "Family History": "[No Info]",
            "Sexual History": "[No Info]",
            "Medications": "[No Info]",
            "Allergies": "[No Info]",
        }

        if len(ttables) > 1:
            df = pd.DataFrame(tables[1])
            df = df.fillna("").astype(str)

            for i, row in df.iterrows():
                for j, cell in enumerate(row):
                    if "History" in cell:
                        if j + 1 < len(df.columns):
                            histories["Medical History"] = df.iat[i, j + 1]
                    if "Medications" in cell:
                        if j + 1 < len(df.columns):
                            histories["Medications"] = df.iat[i, j + 1]
                    if "Allergies" in cell:
                        if j + 1 < len(df.columns):
                            histories["Allergies"] = df.iat[i, j + 1]

        return histories


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
        for key, value in result.items():
            print(f"{key}: {value}")
