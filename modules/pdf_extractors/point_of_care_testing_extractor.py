import pandas as pd
import tabula


class PointOfCareTestingExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read all tables from the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Extract each Point of Care Testing field
            capillary_blood_glucose = self._extract_capillary_blood_glucose(tables)
            cardiac_rhythm, notes = self._extract_cardiac_rhythm(tables)
            etco2 = self._extract_etco2(tables)
            cincinnati = self._extract_cincinnati(tables)
            la_motor_scale = self._extract_la_motor_scale(tables)
            nihss = self._extract_nihss(tables)
        except Exception as e:
            return {"Error": f"Error extracting point of care testing: {e}"}

        return {
            "Capillary Blood Glucose": capillary_blood_glucose,
            "Cardiac Rhythm": cardiac_rhythm,
            "Notes": notes,
            "EtCO2": etco2,
            "Cincinnati": cincinnati,
            "LA Motor Scale": la_motor_scale,
            "NIHSS": nihss,
        }

    def _extract_capillary_blood_glucose(self, tables) -> str:
        return self._extract_first_vital(tables, "BG")

    def _extract_cardiac_rhythm(self, tables) -> (str, str):
        """Extract the first non-empty 'Rhythm' and 'Notes' value where 'Type' is '4-Lead'."""
        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(str)

            # Normalize column headers by stripping and uppercasing them
            df.columns = df.columns.str.strip().str.upper()

            # Identify the columns for "Type", "Rhythm", and "Notes"
            if "ECG" in df.columns:
                type_column = next(
                    (
                        col
                        for col in df.columns
                        if df[col].str.contains("4-LEAD", case=False, na=False).any()
                    ),
                    None,
                )
                rhythm_column = next(
                    (
                        col
                        for col in df.columns
                        if df[col].str.contains("RHYTHM", case=False, na=False).any()
                    ),
                    None,
                )
                notes_column = next(
                    (
                        col
                        for col in df.columns
                        if df[col].str.contains("NOTES", case=False, na=False).any()
                    ),
                    None,
                )

                if type_column and rhythm_column:
                    # Iterate through rows to find the rhythm and notes for "4-Lead"
                    for _, row in df.iterrows():
                        if "4-LEAD" in row[type_column].upper():
                            rhythm_value = row[rhythm_column].strip()
                            notes_value = (
                                row[notes_column].strip()
                                if notes_column
                                else "[No Info]"
                            )
                            if rhythm_value:
                                return rhythm_value, notes_value

        return "[No Info]", "[No Info]"

    def _extract_etco2(self, tables) -> str:
        return "[No Info]"

    def _extract_cincinnati(self, tables) -> str:
        return "[No Info]"

    def _extract_la_motor_scale(self, tables) -> str:
        return "[No Info]"

    def _extract_nihss(self, tables) -> str:
        return "[No Info]"

    def _extract_first_vital(self, tables, label) -> str:
        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(str)

            # Use a simplified pattern to find the best matching column
            column_candidates = [
                col
                for col in df.columns
                if pd.Series(col).str.contains(label, case=False, na=False).any()
            ]

            if not column_candidates:
                continue

            best_match_column = column_candidates[0]

            for _, row in df.iterrows():
                # Skip rows where 'PTA' is present
                if "PTA" in row.str.upper().tolist():
                    continue

                value = str(row[best_match_column]).strip()

                if value:
                    return value

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
        print(f"Extracting from {pdf_file}...")
        result = extractor.extract(pdf_file)
        for key, value in result.items():
            print(f"{key}: {value}")
