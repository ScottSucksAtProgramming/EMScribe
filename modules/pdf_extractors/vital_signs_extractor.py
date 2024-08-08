import pandas as pd
import tabula


class VitalSignsExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read all tables from the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Find the vital signs table
            vital_signs_table = self._find_vital_signs_table(tables)
            if vital_signs_table is None:
                raise ValueError("No vital signs table found in the PDF.")

            # Extract information for the vital signs
            blood_pressure = self._extract_first_vital(vital_signs_table, "BP")
            heart_rate = self._extract_first_vital(vital_signs_table, "Pulse")
            respiratory_rate = self._extract_first_vital(vital_signs_table, "RR")
            spo2 = self._extract_first_vital(vital_signs_table, "SPO2")
            pain = self._extract_first_vital(vital_signs_table, "Pain")
            temperature = self._extract_first_vital(vital_signs_table, "Temp")
        except Exception as e:
            return {"Error": f"Error extracting vital signs: {e}"}

        return {
            "Blood Pressure": blood_pressure,
            "Heart Rate": heart_rate,
            "Respiratory Rate": respiratory_rate,
            "SpO2": spo2,
            "Pain": pain,
            "Temperature": temperature,
        }

    def _find_vital_signs_table(self, tables):
        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(str)
            if "Vital Signs" in df.columns:
                return df
        return None

    def _extract_first_vital(self, table, label) -> str:
        # Find the row where the "Vital Signs" start and extract the corresponding column
        try:
            label_row_index = table.columns.get_loc("Vital Signs")
            for i, row in table.iterrows():
                if row[label_row_index].strip() != "":
                    value = row[table.columns.get_loc(label)].strip()
                    return value if value else "[No Info]"
        except Exception:
            return "[No Info]"

        return "[No Info]"


# Example usage
if __name__ == "__main__":
    extractor = VitalSignsExtractor()
    pdf_files = [
        "pdf_1.pdf",
        "pdf_2.pdf",
        "pdf_3.pdf",
    ]  # Add paths to your test PDFs here

    for pdf_file in pdf_files:
        result = extractor.extract(pdf_file)
        for sign, value in result.items():
            print(f"{sign}: {value}")
