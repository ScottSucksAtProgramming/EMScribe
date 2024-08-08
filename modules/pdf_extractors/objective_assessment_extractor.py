import pandas as pd
import tabula


class ObjectiveAssessmentExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Find and extract objective assessment information
            objective_assessment = self.extract_assessment(tables)
        except Exception as e:
            objective_assessment = {
                section: f"Error extracting {section.lower()}: {e}"
                for section in self.sections()
            }

        return {
            section: objective_assessment.get(section, "[No Info]")
            for section in self.sections()
        }

    def extract_assessment(self, tables) -> dict:
        assessment = {section: "[No Info]" for section in self.sections()}

        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(str)

            for i, row in df.iterrows():
                for j, cell in row.items():
                    if "Mental Status" in cell:
                        assessment["GENERAL"] = self._extract_information(
                            df, i, df.columns.get_loc(j)
                        )

        return assessment

    def _extract_information(self, df: pd.DataFrame, row: int, col: int) -> str:
        left_col = col - 1
        right_col = col + 1
        above_empty_count = 0
        below_empty_count = 0

        # Check cells above for empty values
        for k in range(row - 1, -1, -1):
            if df.iat[k, col] == "":
                above_empty_count += 1
            else:
                break

        # Check cells below for empty values
        for k in range(row + 1, len(df)):
            if df.iat[k, col] == "":
                below_empty_count += 1
            else:
                break

        start_row = row - above_empty_count
        end_row = row + below_empty_count

        left_info = df.iloc[start_row : end_row + 1, left_col].tolist()
        right_info = df.iloc[start_row : end_row + 1, right_col].tolist()

        combined_info = ", ".join(
            [info.strip() for info in left_info + right_info if info.strip()]
        ).strip()
        return combined_info

    def sections(self):
        return [
            "GENERAL",
            "SKIN",
            "HEENT",
            "NECK",
            "CARDIOVASCULAR",
            "RESPIRATORY",
            "ABDOMEN",
            "GENITOURINARY",
            "GASTROINTESTINAL",
            "SPINE",
            "MUSCULOSKELETAL",
            "NEUROLOGICAL",
            "PSYCHIATRIC",
        ]


# Example usage
if __name__ == "__main__":
    extractor = ObjectiveAssessmentExtractor()
    pdf_files = [
        "pdf_1.pdf",
        "pdf_2.pdf",
        "pdf_3.pdf",
    ]  # Add paths to your test PDFs here

    for pdf_file in pdf_files:
        result = extractor.extract(pdf_file)
        for key, value in result.items():
            print(f"{key}: {value}")
