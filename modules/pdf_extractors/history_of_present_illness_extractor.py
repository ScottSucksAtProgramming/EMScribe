import pandas as pd
import tabula


class HistoryOfPresentIllnessExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Find and extract signs and symptoms information
            signs_symptoms_info = self._extract_signs_symptoms(tables)
        except Exception as e:
            signs_symptoms_info = f"Error extracting signs and symptoms: {e}"

        return {
            "Associated Signs and Symptoms": signs_symptoms_info,
            "Onset": self._extract_onset(),  # Placeholder method
            "Provocation": self._extract_provocation(),  # Placeholder method
            "Palliation": self._extract_palliation(),  # Placeholder method
            "Quality": self._extract_quality(),  # Placeholder method
            "Radiation": self._extract_radiation(),  # Placeholder method
            "Severity": self._extract_severity(),  # Placeholder method
            "Time": self._extract_time(),  # Placeholder method
            "Interventions": self._extract_interventions(),  # Placeholder method
            "Additional History of Present Illness": self._extract_additional_history_of_present_illness(),  # Placeholder method
        }

    def _extract_signs_symptoms(self, tables) -> str:
        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(
                str
            )  # Fill NaN with empty string and cast to string type

            signs_symptoms_coords = None
            above_empty_count = 0
            below_empty_count = 0

            # Iterate through the DataFrame to find "Signs & Symptoms"
            for i, row in df.iterrows():
                for j, cell in row.items():
                    if "Signs & Symptoms" in cell:
                        signs_symptoms_coords = (i, j)

                        # Check cells above for empty values
                        for k in range(i - 1, -1, -1):
                            if df.iloc[k, df.columns.get_loc(j)] == "":
                                above_empty_count += 1
                            else:
                                break

                        # Check cells below for empty values
                        for k in range(i + 1, len(df)):
                            if df.iloc[k, df.columns.get_loc(j)] == "":
                                below_empty_count += 1
                            else:
                                break

                        break
                if signs_symptoms_coords:
                    break

            if signs_symptoms_coords:
                row, col = signs_symptoms_coords
                info_col = df.columns[df.columns.get_loc(col) + 1]

                # Extract information from the identified range in the column to the right
                start_row = row - above_empty_count
                end_row = row + below_empty_count
                signs_symptoms_info = df.iloc[
                    start_row : end_row + 1, df.columns.get_loc(info_col)
                ].tolist()

                # Combine the extracted information into a single string
                signs_symptoms_text = ", ".join(
                    [info.strip() for info in signs_symptoms_info if info.strip()]
                ).strip()

                return signs_symptoms_text

        return "[No Info]"

    def _extract_onset(self) -> str:
        return "[No Info]"

    def _extract_provocation(self) -> str:
        return "[No Info]"

    def _extract_palliation(self) -> str:
        return "[No Info]"

    def _extract_quality(self) -> str:
        return "[No Info]"

    def _extract_radiation(self) -> str:
        return "[No Info]"

    def _extract_severity(self) -> str:
        return "[No Info]"

    def _extract_time(self) -> str:
        return "[No Info]"

    def _extract_interventions(self) -> str:
        return "[No Info]"

    def _extract_additional_history_of_present_illness(self) -> str:
        return "[No Info]"


# Example usage
if __name__ == "__main__":
    extractor = HistoryOfPresentIllnessExtractor()
    pdf_files = [
        "pdf_1.pdf",
        "pdf_2.pdf",
        "pdf_3.pdf",
    ]  # Add paths to your test PDFs here

    for pdf_file in pdf_files:
        result = extractor.extract(pdf_file)
        associated_signs_symptoms = result.get(
            "Associated Signs and Symptoms", "[No Info]"
        )
        print(f"{pdf_file}: {associated_signs_symptoms}")
