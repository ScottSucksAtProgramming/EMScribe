import pandas as pd
import tabula
import re


class PointOfCareTestingExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read all tables from the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Extract information for each Point of Care Testing field
            capillary_blood_glucose = self._extract_capillary_blood_glucose(tables)
            ekg = self._extract_ekg(tables)
            etco2 = self._extract_etco2(tables)
            cincinnati = self._extract_cincinnati(tables)
            la_motor_scale = self._extract_la_motor_scale(tables)
            nihss = self._extract_nihss(tables)
        except Exception as e:
            return {"Error": f"Error extracting point of care testing: {e}"}

        return {
            "Capillary Blood Glucose": capillary_blood_glucose,
            "EKG": ekg,
            "EtCO2": etco2,
            "Cincinnati": cincinnati,
            "LA Motor Scale": la_motor_scale,
            "NIHSS": nihss,
        }

    def _extract_capillary_blood_glucose(self, tables) -> str:
        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(str)

            # Look for the column related to Capillary Blood Glucose
            if any(df.columns.str.contains("BG", case=False)):
                return self._extract_first_value(df, "BG")
        return "[No Info]"

    def _extract_ekg(self, tables) -> str:
        return "[No Info]"

    def _extract_etco2(self, tables) -> str:
        return "[No Info]"

    def _extract_cincinnati(self, tables) -> str:
        return "[No Info]"

    def _extract_la_motor_scale(self, tables) -> str:
        return "[No Info]"

    def _extract_nihss(self, tables) -> str:
        return "[No Info]"

    def _extract_first_value(self, table: pd.DataFrame, label: str) -> str:
        try:
            # Find the best matching column for the given label
            column_candidates = [
                col
                for col in table.columns
                if pd.Series(col).str.contains(label, case=False, na=False).any()
            ]

            if not column_candidates:
                return "[No Info]"

            best_match_column = column_candidates[0]

            for i, row in table.iterrows():
                time_value = row.get("Time", "").strip()
                value = str(row[best_match_column]).strip()

                # Skip rows with 'PTA' in the Time column
                if "PTA" in time_value:
                    continue

                if value:
                    return value

            return "[No Info]"

        except Exception:
            return "[No Info]"


# Example usage
if __name__ == "__main__":
    extractor = PointOfCareTestingExtractor()
    pdf_files = [
        "data/pdf_1.pdf",
        "data/pdf_2.pdf",
        "data/pdf_3.pdf",
    ]  # Add paths to your test PDFs here

    for pdf_file in pdf_files:
        result = extractor.extract(pdf_file)
        for key, value in result.items():
            print(f"{key}: {value}")
