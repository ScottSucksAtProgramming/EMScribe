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
                for j, cell in enumerate(row):
                    for section in self.sections():
                        if section in cell:
                            if j + 1 < len(df.columns):
                                assessment[section] = df.iat[i, j + 1]

        return assessment

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
