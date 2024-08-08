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
            blood_pressure = self.extract_first_bp(vital_signs_table)
            heart_rate = self.extract_first_vital(vital_signs_table, "Pulse")
            respiratory_rate = self.extract_first_vital(vital_signs_table, "RR")
            spo2 = self.extract_first_vital(vital_signs_table, "SPO2")
            pain = self.extract_first_vital(vital_signs_table, "Pain")
            temperature = self.extract_first_vital(vital_signs_table, "Temp")

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

    def _find_vital_signs_table(self, tables) -> pd.DataFrame:
        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(str)
            if "Vital Signs" in df.columns or "Vital Signs" in df.values:
                return df
        return None

    def extract_first_bp(self, table: pd.DataFrame) -> str:
        try:
            bp_column = self._find_bp_column(table)
            if bp_column is not None:
                # Find the first non-empty value below the 'BP' label
                for i in range(1, len(table)):
                    value = table.iloc[i, bp_column].strip()
                    if value:  # If the value is not empty
                        return value
            return "[No Info]"
        except Exception as e:
            print(f"Error extracting BP: {e}")
            return "[No Info]"

    def extract_first_vital(self, table: pd.DataFrame, label: str) -> str:
        try:
            label_column = self._find_column(table, label)
            if label_column is not None:
                # Find the first non-empty value below the label
                for i in range(1, len(table)):
                    value = table.iloc[i, label_column].strip()
                    if value:  # If the value is not empty
                        return value
            return "[No Info]"
        except Exception as e:
            print(f"Error extracting {label}: {e}")
            return "[No Info]"

    def _find_bp_column(self, table: pd.DataFrame) -> int:
        for idx, column in enumerate(table.columns):
            if table[column].str.contains("BP").any():
                return idx
        return None

    def _find_column(self, table: pd.DataFrame, label: str) -> int:
        for idx, column in enumerate(table.columns):
            if table[column].str.contains(label).any():
                return idx
        return None


# Example usage
if __name__ == "__main__":
    extractor = VitalSignsExtractor()
    pdf_files = [
        "pdf_1.pdf",
        "pdf_2.pdf",
        "pdf_3.pdf",
    ]  # Add paths to your test PDFs here

    for pdf_file in pdf_files:
        print(f"Extracting from {pdf_file}...")
        result = extractor.extract(pdf_file)
        print("Vital Signs:")
        for sign, value in result.items():
            print(f"{sign}: {value}")
