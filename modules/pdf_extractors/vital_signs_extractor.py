import pandas as pd
import tabula
import re


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
            blood_pressure = self.extract_first_vital(vital_signs_table, "BP")
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

            # Checking if the DataFrame has relevant columns
            if any(df.columns.str.contains("BP|Pulse|RR|SPO2|Pain|Temp", case=False)):
                return df
        return None

    def extract_first_vital(self, table: pd.DataFrame, label: str) -> str:
        try:
            # Use a simplified pattern to find the best matching column
            column_candidates = [
                col
                for col in table.columns
                if pd.Series(col).str.contains(label, case=False, na=False).any()
            ]

            if not column_candidates:
                return "[No Info]"

            best_match_column = column_candidates[0]

            for i, value in enumerate(table[best_match_column]):
                value = str(value).strip()

                # Specific handling for BP - validate using regex
                if label == "BP":
                    # Regex pattern to match any number/any number format
                    bp_pattern = re.compile(r"\d+/\d+")
                    if not bp_pattern.match(value):
                        continue  # Skip invalid BP values

                if value:
                    return value

            return "[No Info]"

        except Exception as e:
            return "[No Info]"


# Example usage
if __name__ == "__main__":
    extractor = VitalSignsExtractor()
    pdf_files = [
        "pdf_1.pdf",
        "pdf_2.pdf",
        "pdf_3.pdf",
        "demo_eso.pdf",
    ]  # Add paths to your test PDFs here

    for pdf_file in pdf_files:
        result = extractor.extract(pdf_file)
        # The output will no longer print anything to the console
