import pandas as pd
import tabula


class ObjectiveAssessmentExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read all tables from the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Extract information for the "GENERAL" section
            general_info = self._extract_general(tables)
        except Exception as e:
            return {"Error": f"Error extracting objective assessment: {e}"}

        return {
            "GENERAL": general_info,
            # Add more sections as needed
        }

    def _extract_general(self, tables) -> str:
        # Ensure we are looking at table 7
        if len(tables) < 7:
            return "[No Info]"

        df = pd.DataFrame(tables[6])
        df = df.fillna("").astype(
            str
        )  # Fill NaN with empty string and cast to string type

        for i, row in df.iterrows():
            for j, cell in row.items():
                if "Mental Status" in cell:
                    # Label found, now count empty cells below it
                    below_empty_count = 0
                    for k in range(i + 1, len(df)):
                        if df.iloc[k, j] == "":
                            below_empty_count += 1
                        else:
                            break

                    # Extract information from the range to the left and right of the label column
                    left_info = []
                    right_info = []
                    start_row = i + 1
                    end_row = i + 1 + below_empty_count
                    for k in range(start_row, end_row):
                        left_info.append(df.iloc[k, df.columns.get_loc("Unnamed: 0")])
                        right_info.append(df.iloc[k, df.columns.get_loc("Unnamed: 1")])

                    combined_info = ", ".join(
                        filter(None, left_info + right_info)
                    ).strip()
                    return combined_info

        return "[No Info]"


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
        for section, info in result.items():
            print(f"{section}: {info}")
