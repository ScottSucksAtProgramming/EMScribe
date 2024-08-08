import pandas as pd
import tabula


class ObjectiveAssessmentExtractor:
    def extract(self, pdf_path: str) -> dict:
        try:
            # Read all tables from the PDF file
            tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

            # Find all tables containing the 'Assessments' column
            assessment_tables = self._find_assessment_tables(tables)
            if not assessment_tables:
                raise ValueError("No assessment tables found in the PDF.")

            # Extract information for the objective assessment sections
            general_info = self._extract_general(assessment_tables)
            skin_info = self._extract_skin(assessment_tables)
            heent_info = self._extract_heent(assessment_tables)
            neck_info = self._extract_neck(assessment_tables)
            cardiovascular_info = self._extract_cardiovascular(assessment_tables)
            respiratory_info = self._extract_respiratory(assessment_tables)
            abdomen_info = self._extract_abdomen(assessment_tables)
            gu_gi_info = self._extract_gu_gi(assessment_tables)
            spine_info = self._extract_spine(assessment_tables)
            musculoskeletal_info = self._extract_musculoskeletal(assessment_tables)
            neurological_info = self._extract_neurological(assessment_tables)
            psychiatric_info = "[No Info]"
        except Exception as e:
            return {"Error": f"Error extracting objective assessment: {e}"}

        return {
            "GENERAL": general_info,
            "SKIN": skin_info,
            "HEENT": heent_info,
            "NECK": neck_info,
            "CARDIOVASCULAR": cardiovascular_info,
            "RESPIRATORY": respiratory_info,
            "ABDOMEN": abdomen_info,
            "GU/GI": gu_gi_info,
            "SPINE": spine_info,
            "MUSCULOSKELETAL": musculoskeletal_info,
            "NEUROLOGICAL": neurological_info,
            "PSYCHIATRIC": psychiatric_info,
        }

    def _find_assessment_tables(self, tables):
        assessment_tables = []
        for table in tables:
            df = pd.DataFrame(table)
            df = df.fillna("").astype(str)
            if (
                "Assessments" in df.columns
                or df.apply(lambda row: row.str.contains("Assessments")).any().any()
            ):
                assessment_tables.append(df)
        return assessment_tables

    def _extract_general(self, tables) -> str:
        return self._extract_section_info(tables, "Mental Status")

    def _extract_skin(self, tables) -> str:
        return self._extract_section_info(tables, "Skin")

    def _extract_heent(self, tables) -> str:
        return self._extract_section_info(tables, ["Head", "Face", "Eyes"])

    def _extract_neck(self, tables) -> str:
        return self._extract_section_info(tables, "Neck")

    def _extract_cardiovascular(self, tables) -> str:
        labels = [
            "Chest",
            "Heart Sounds",
            "Anterior - General",
            "Posterior - General",
            "Anterior - Left",
            "Posterior - Left",
            "Left - Side",
            "Anterior - Right",
            "Posterior - Right",
            "Right - Side",
        ]
        return self._extract_section_info(tables, labels)

    def _extract_respiratory(self, tables) -> str:
        labels = ["Lung Sounds", "Bilateral"]
        return self._extract_section_info(tables, labels)

    def _extract_abdomen(self, tables) -> str:
        labels = [
            "General",
            "Left Upper",
            "Right Upper",
            "Left Lower",
            "Right Lower",
            "Periumbilical",
        ]
        return self._extract_section_info(tables, labels)

    def _extract_gu_gi(self, tables) -> str:
        return self._extract_section_info(tables, "Pelvis/GU/GI")

    def _extract_spine(self, tables) -> str:
        labels = [
            "Back",
            "Cervical",
            "Midline",
            "Right",
            "Left",
            "Thoracic",
            "Lumbar",
            "Sacral",
        ]
        return self._extract_section_info(tables, labels)

    def _extract_musculoskeletal(self, tables) -> str:
        labels = [
            "Extremities",
            "Arm",
            "Elbow",
            "Thumb",
            "Finger",
            "Hand",
            "Shoulder",
            "Wrist",
            "Leg",
            "Foot",
            "Hip",
            "Knee",
            "Toe",
            "Pulse",
            "Capillary Refill",
        ]
        return self._extract_section_info(tables, labels)

    def _extract_neurological(self, tables) -> str:
        return self._extract_section_info(tables, "Neurological")

    def _extract_section_info(self, tables, labels) -> str:
        if isinstance(labels, str):
            labels = [labels]

        info_left = []
        info_right = []
        for table in tables:
            for label in labels:
                for i, row in table.iterrows():
                    for j, cell in row.items():
                        if label in cell:
                            # Label found, now count empty cells below it
                            below_empty_count = 0
                            for k in range(i + 1, len(table)):
                                if table.iat[k, table.columns.get_loc(j)] == "":
                                    below_empty_count += 1
                                else:
                                    break

                            # Extract information from the range starting from the row of the label
                            start_row = i
                            end_row = i + 1 + below_empty_count

                            for k in range(start_row, end_row):
                                if table.columns.get_loc(j) - 1 >= 0:
                                    left_cell = table.iat[
                                        k, table.columns.get_loc(j) - 1
                                    ]
                                    if (
                                        left_cell and left_cell not in labels
                                    ):  # Skip the label itself and empty cells
                                        info_left.append(
                                            left_cell
                                        )  # Column to the left
                                if table.columns.get_loc(j) + 1 < table.shape[1]:
                                    right_cell = table.iat[
                                        k, table.columns.get_loc(j) + 1
                                    ]
                                    if (
                                        right_cell and right_cell not in labels
                                    ):  # Skip the label itself and empty cells
                                        info_right.append(
                                            right_cell
                                        )  # Column to the right

        # Format the output: no commas for left, commas for right
        left_info = " ".join(filter(None, info_left)).strip()
        right_info = ", ".join(filter(None, info_right)).strip()

        combined_info = f"{left_info} {right_info}".strip()
        return combined_info if combined_info else "[No Info]"


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
