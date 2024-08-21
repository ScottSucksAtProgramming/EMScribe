import pdfplumber
import pandas as pd
from modules.base_pdf_extractor import BasePDFExtractor


class ClinicalImpressionExtractor(BasePDFExtractor):
    """
    Extracts clinical impression information from a PDF.

    This class inherits from BasePDFExtractor and is responsible for extracting
    clinical impressions such as primary impression, secondary impression,
    onset time, last known well, and other related data from the 'Clinical Impression' section of the PDF.

    Methods:
        extract(): Extracts clinical impression data from the PDF and returns it as a dictionary.
    """

    def extract(self):
        """
        Extracts clinical impression information from the PDF.

        Returns:
            dict: A dictionary containing the extracted clinical impression information.
        """
        clinical_impression = {}
        with pdfplumber.open(self.pdf_path) as pdf:
            page = pdf.pages[0]
            tables = page.extract_tables()

            if tables:
                df = pd.DataFrame(tables[0])
                known_headings = ["Clinical Impression"]
                split_tables = self.detect_and_split_tables(df, known_headings)

                clinical_impression_df = split_tables.get("Clinical Impression")
                if clinical_impression_df is not None:
                    clinical_impression["Primary Impression"] = (
                        self._extract_primary_impression(clinical_impression_df)
                    )
                    clinical_impression["Secondary Impression"] = (
                        self._extract_secondary_impression(clinical_impression_df)
                    )
                    clinical_impression["Onset Time"] = self._extract_onset_time(
                        clinical_impression_df
                    )
                    clinical_impression["Last Known Well"] = (
                        self._extract_last_known_well(clinical_impression_df)
                    )
                    clinical_impression["Chief Complaint"] = (
                        self._extract_chief_complaint_with_duration(
                            clinical_impression_df
                        )
                    )
                    clinical_impression["Secondary Complaint"] = (
                        self._extract_secondary_complaint_with_duration(
                            clinical_impression_df
                        )
                    )
                    clinical_impression["Signs & Symptoms"] = (
                        self._extract_signs_and_symptoms(clinical_impression_df)
                    )
                    clinical_impression["Injury"] = self._extract_injury_info(
                        clinical_impression_df
                    )

        return clinical_impression

    def _extract_primary_impression(self, df):
        try:
            primary_impression_row = df[
                df.iloc[:, 0].str.contains("Primary Impression", na=False)
            ]
            if not primary_impression_row.empty:
                primary_impression_value = primary_impression_row.iloc[0, 1].strip()
                return primary_impression_value
            else:
                return "Primary Impression not found"
        except Exception as e:
            return "Primary Impression not found"

    def _extract_secondary_impression(self, df):
        try:
            secondary_impression_row = df[
                df.iloc[:, 0].str.contains("Secondary Impression", na=False)
            ]
            if not secondary_impression_row.empty:
                secondary_impression_value = secondary_impression_row.iloc[0, 1].strip()
                return secondary_impression_value
            else:
                return "Secondary Impression not found"
        except Exception as e:
            return "Secondary Impression not found"

    def _extract_onset_time(self, df):
        try:
            onset_time_row = df[df.iloc[:, 0].str.contains("Onset Time", na=False)]
            if not onset_time_row.empty:
                onset_time_value = onset_time_row.iloc[0, 1].strip()
                return onset_time_value
            else:
                return "Onset Time not found"
        except Exception as e:
            return "Onset Time not found"

    def _extract_last_known_well(self, df):
        try:
            last_known_well_row = df[
                df.iloc[:, 0].str.contains("Last Known Well", na=False)
            ]
            if not last_known_well_row.empty:
                last_known_well_value = last_known_well_row.iloc[0, 1].strip()
                return last_known_well_value
            else:
                return "Last Known Well not found"
        except Exception as e:
            return "Last Known Well not found"

    def _extract_chief_complaint_with_duration(self, df):
        try:
            complaint_row = df[df.iloc[:, 0] == "Chief Complaint"]
            duration_row = df[df.iloc[:, 0] == "Duration"]

            if not complaint_row.empty and not duration_row.empty:
                chief_complaint = complaint_row.iloc[0, 1].strip()
                duration = duration_row.iloc[0, 1].strip()
                duration_unit = duration_row.iloc[0, 2].strip()

                return f"{chief_complaint} for {duration} {duration_unit}"
            else:
                return "Chief Complaint with Duration not found"
        except Exception as e:
            return "Chief Complaint with Duration not found"

    def _extract_secondary_complaint_with_duration(self, df):
        try:
            complaint_row = df[df.iloc[:, 0] == "Secondary Complaint"]
            duration_row = df[df.iloc[:, 0] == "Duration"]

            if not complaint_row.empty and len(duration_row) > 1:
                secondary_complaint = complaint_row.iloc[0, 1].strip()
                secondary_duration = duration_row.iloc[1, 1].strip()
                secondary_duration_unit = duration_row.iloc[1, 2].strip()

                return f"{secondary_complaint} for {secondary_duration} {secondary_duration_unit}"
            else:
                return "Secondary Complaint with Duration not found"
        except Exception as e:
            return "Secondary Complaint with Duration not found"

    def _extract_signs_and_symptoms(self, df):
        try:
            signs_symptoms_row = df[
                df.iloc[:, 0].str.contains("Signs & Symptoms", na=False)
            ]
            if not signs_symptoms_row.empty:
                signs_symptoms_value = signs_symptoms_row.iloc[0, 1]
                symptoms_list = [
                    symptom.strip() for symptom in signs_symptoms_value.split("\n")
                ]
                return ", ".join(symptoms_list)
            else:
                return "Signs & Symptoms not found"
        except Exception as e:
            return "Signs & Symptoms not found"

    def _extract_injury_info(self, df):
        """
        Extracts the injury information from the Clinical Impression DataFrame.

        Args:
            df (pd.DataFrame): The Clinical Impression DataFrame.

        Returns:
            str: The injury information on a single line.
        """
        try:
            injury_row = df[df.iloc[:, 0].str.contains("Injury", na=False)]
            if not injury_row.empty:
                injury_value = injury_row.iloc[0, 1].strip()

                # Check if there are multiple lines within the injury cell and join them into one line.
                injury_info = " ".join(
                    injury_value.splitlines()
                )  # Ensures the injury info is all on one line

                return injury_info
            else:
                return "Injury information not found"
        except Exception as e:
            return "Injury information not found"


if __name__ == "__main__":
    # Path to the PDF file for testing
    pdf_path = "data/demo_eso.pdf"

    # Create an instance of the extractor
    extractor = ClinicalImpressionExtractor(pdf_path)

    # Extract the clinical impression information
    clinical_impression = extractor.extract()

    # Print the extracted information for testing
    print("Extracted Clinical Impression Information:")
    for key, value in clinical_impression.items():
        print(f"{key}: {value}")
