from modules.base_pdf_extractor import BasePDFExtractor
from modules.patient_demographics_extractor import PatientDemographicsExtractor
from modules.incident_information_extractor import IncidentInformationExtractor
from modules.subjective_information_extractor import SubjectiveInformationExtractor
from modules.hpi_extractor import HPIExtractor
from modules.patient_history_extractor import PatientHistoriesExtractor


class ESOExtractor(BasePDFExtractor):
    """
    Extractor for ESO PDFs, designed to extract various sections of EMS data.

    This class utilizes specific extractors for different data sections.
    """

    def __init__(self, pdf_path):
        super().__init__(pdf_path)
        self.incident_information_extractor = IncidentInformationExtractor(pdf_path)
        self.demographics_extractor = PatientDemographicsExtractor(pdf_path)
        self.subjective_information_extractor = SubjectiveInformationExtractor(pdf_path)
        self.hpi_extractor = HPIExtractor(pdf_path)
        self.patient_histories_extractor = PatientHistoriesExtractor(pdf_path)

    def extract_incident_information(self):
        """
        Extracts incident information using the IncidentInformationExtractor.

        Returns:
            dict: Extracted incident information.
        """
        return self.incident_information_extractor.extract()

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

    def extract_subjective_information(self):
        """
        Extracts subjective information using the SubjectiveInformationExtractor.

        Returns:
            dict: Extracted subjective information.
        """
        return self.subjective_information_extractor.extract()

    def extract(self):
        """
        Extracts all relevant information from the PDF.

        Returns:
            dict: A dictionary containing all the extracted information.
        """
        return {
            "Incident Information": self.extract_incident_information(),
            "Patient Information": self.extract_patient_information(),
            "Subjective Information": self.extract_subjective_information(),
            "History of Present Illness Information": self.hpi_extractor.extract(),
            "Patient Histories": self.patient_histories_extractor.extract(),
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
