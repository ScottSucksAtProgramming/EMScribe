from base_pdf_extractor import BasePDFExtractor
from patient_demographics_extractor import PatientDemographicsExtractor
from medication_information_extractor import MedicationInformationExtractor


class ESOExtractor(BasePDFExtractor):
    """
    Extractor for ESO PDFs, designed to extract various sections of EMS data.

    This class utilizes specific extractors for different data sections.
    """

    def __init__(self, pdf_path):
        super().__init__(pdf_path)
        self.demographics_extractor = PatientDemographicsExtractor(pdf_path)
        self.medication_extractor = MedicationInformationExtractor(pdf_path)

    def extract_patient_information(self):
        """
        Extracts patient demographic information using the PatientDemographicsExtractor.

        Returns:
            dict: Extracted patient demographic information.
        """
        return self.demographics_extractor.extract()

    def extract_medication_information(self):
        """
        Extracts medication information using the MedicationInformationExtractor.

        Returns:
            dict: Extracted medication information.
        """
        return self.medication_extractor.extract()

    def extract(self):
        """
        Extracts all relevant information from the PDF.

        Returns:
            dict: A dictionary containing all the extracted information.
        """
        return {
            "Patient Information": self.extract_patient_information(),
            "Medication Information": self.extract_medication_information(),
            # Placeholder for future extractions:
            # "Clinical Impression": self.extract_clinical_impression(),
        }


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"  # Path to your PDF file
    extractor = ESOExtractor(pdf_path)
    extracted_information = extractor.extract()

    for section, info in extracted_information.items():
        print(f"{section}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
        print()  # Adds an empty line after each section
