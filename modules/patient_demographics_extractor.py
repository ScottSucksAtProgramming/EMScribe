import pdfplumber
import pandas as pd
from modules.base_pdf_extractor import BasePDFExtractor


class PatientDemographicsExtractor(BasePDFExtractor):
    """
    Extracts patient demographic information from a PDF.

    This class inherits from BasePDFExtractor and is responsible for extracting
    information such as the patient's first name, date of birth, age, and gender
    from the 'Patient Information' section of the PDF.

    Methods:
        extract(): Extracts patient demographics from the PDF and returns it as a dictionary.
    """

    def extract(self):
        """
        Extracts patient demographic information from the PDF.

        Returns:
            dict: A dictionary containing the extracted patient demographics.
        """
        patient_info = {}
        with pdfplumber.open(self.pdf_path) as pdf:
            page = pdf.pages[0]
            tables = page.extract_tables()

            if tables:
                df = pd.DataFrame(tables[0])
                known_headings = ["Patient Information"]
                split_tables = self.detect_and_split_tables(df, known_headings)

                patient_info_df = split_tables.get("Patient Information")
                if patient_info_df is not None:
                    patient_info["First Name"] = self._extract_first_name(
                        patient_info_df
                    )
                    patient_info["Date of Birth"] = self._extract_dob(patient_info_df)
                    patient_info["Age"] = self._extract_age(patient_info_df)
                    patient_info["Gender"] = self._extract_gender(patient_info_df)

        return patient_info

    def _extract_first_name(self, df):
        """
        Extracts the first name of the patient from the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame containing patient information.

        Returns:
            str: The first name of the patient.
        """
        return df[df[0] == "First"].iloc[0, 1].strip()

    def _extract_dob(self, df):
        """
        Extracts the date of birth of the patient from the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame containing patient information.

        Returns:
            str: The date of birth of the patient.
        """
        return df[df[0] == "DOB"].iloc[0, 1].strip()

    def _extract_age(self, df):
        """
        Extracts the age of the patient from the DataFrame, truncated to only include
        the first part (e.g., '38 Yrs').

        Args:
            df (pd.DataFrame): The DataFrame containing patient information.

        Returns:
            str: The truncated age of the patient.
        """
        age_full = df[df[0] == "Age"].iloc[0, 1].strip()
        age_truncated = age_full.split(",")[
            0
        ]  # Take only the first part before the comma
        return age_truncated

    def _extract_gender(self, df):
        """
        Extracts the gender of the patient from the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame containing patient information.

        Returns:
            str: The gender of the patient.
        """
        return df[df[0] == "Gender"].iloc[0, 1].strip()


if __name__ == "__main__":
    # Path to the PDF file for testing
    pdf_path = "data/demo_eso.pdf"

    # Create an instance of the extractor
    extractor = PatientDemographicsExtractor(pdf_path)

    # Extract the patient information
    patient_info = extractor.extract()

    # Print the extracted information for testing
    print("Extracted Patient Information:")
    for key, value in patient_info.items():
        print(f"{key}: {value}")
