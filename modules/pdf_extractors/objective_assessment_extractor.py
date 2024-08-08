import pandas as pd
import tabula


class ObjectiveAssessmentExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read all tables from the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Extract information for each section
            general_info = self._extract_general(tables)
            skin_info = self._extract_skin(tables)
            cardiovascular_info = self._extract_cardiovascular(tables)
        except Exception as e:
            return {"Error": f"Error extracting objective assessment: {e}"}

        return {
            "GENERAL": general_info,
            "SKIN": skin_info,
            "CARDIOVASCULAR": cardiovascular_info,
            # Add more sections as needed
        }

    def _extract_general(self, tables) -> str:
        return self._extract_section(tables, "Mental Status")

    def _extract_skin(self, tables) -> str:
        return self._extract_section(tables, "Skin")

    def _extract_cardiovascular(self, tables) -> str:
        chest_info = self._extract_section(tables, "Chest")
        heart_sounds_info = self._extract_section(tables, "Heart Sounds")
        lung_sounds_info = self._extract_section(tables, "Lung Sounds")
        combined_info = ", ".join(
            filter(None, [chest_info, heart_sounds_info, lung_sounds_info])
        ).strip()
        return combined_info

    def _extract_section(self, tables, label) -> str:
        # Ensure we are looking at table 7
        if len(tables) < 7:
            return "[No Info]"

        df = pd.DataFrame(tables[6])
        df = df.fillna("").astype(
            str
        )  # Fill NaN with empty string and cast to string type

        for i, row in df.iterrows():
            for j, cell in row.items():
                if label in cell:
                    section_info = []
                    # Collect information below the label in the same column
                    for k in range(i + 1, len(df)):
                        if df.iloc[k, df.columns.get_loc("Assessments")] == "":
                            section_info.append(
                                df.iloc[k, df.columns.get_loc("Unnamed: 1")]
                            )
                            section_info.append(
                                df.iloc[k, df.columns.get_loc("Unnamed: 0")]
                            )
                        else:
                            break
                    combined_info = ", ".join(filter(None, section_info)).strip()
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
