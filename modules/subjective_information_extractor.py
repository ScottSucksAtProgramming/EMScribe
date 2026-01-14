from dataclasses import asdict, dataclass, field

import pandas as pd

from modules.base_pdf_extractor import BasePDFExtractor


@dataclass
class SubjectiveInformation:
    facility_name: str = field(default="")
    patient_location_and_position: str = field(default="")
    patient_appearance: str = field(default="")
    medical_equipment_in_use: str = field(default="")
    patient_chief_complaint: str = field(default="")


class SubjectiveInformationExtractor(BasePDFExtractor):
    def __init__(self, pdf_path):
        super().__init__(pdf_path)
        self.subjective_info = SubjectiveInformation()

    def extract_facility_name(self):
        incident_details_table = None

        import pdfplumber  # type: ignore

        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table)
                    if "Incident Details" in df.values:
                        incident_details_table = df
                        break
                if incident_details_table is not None:
                    break

        if incident_details_table is None:
            self.subjective_info.facility_name = "Private Residence"
            return

        location_type_row = incident_details_table[
            incident_details_table[0] == "Location Type"
        ]
        location_row = incident_details_table[incident_details_table[0] == "Location"]

        if not location_type_row.empty:
            location_type = location_type_row.iloc[0, 1]
            if "Residence" not in location_type and "Home" not in location_type:
                facility_name = location_row.iloc[0, 1].replace("\n", " ")
                self.subjective_info.facility_name = facility_name
            else:
                self.subjective_info.facility_name = "Private Residence"
        else:
            self.subjective_info.facility_name = "Private Residence"

    def extract_chief_complaint(self):
        import pdfplumber  # type: ignore

        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table)
                    if "Chief Complaint" in df.values:
                        chief_complaint_row = df[df[4] == "Chief Complaint"]
                        if not chief_complaint_row.empty:
                            chief_complaint = chief_complaint_row.iloc[0, 5].replace(
                                "\n", " "
                            )
                            # Now extract the duration and unit from the next row
                            duration_row = df[df[4] == "Duration"]
                            if not duration_row.empty:
                                duration_value = duration_row.iloc[0, 5]
                                unit_label = duration_row.iloc[0, 6]  # This is "Units"
                                # Fetch the value in the column after "Units"
                                unit_value = (
                                    duration_row.iloc[0, 7]
                                    if duration_row.shape[1] > 7
                                    else ""
                                )

                                self.subjective_info.patient_chief_complaint = f"{chief_complaint} for {duration_value} {unit_value}".strip()
                            else:
                                self.subjective_info.patient_chief_complaint = (
                                    chief_complaint
                                )
                            return

    def extract(self):
        self.extract_facility_name()
        self.extract_chief_complaint()
        # Extract other fields as needed

        return asdict(self.subjective_info)


if __name__ == "__main__":
    pdf_path = "data/pdf_5.pdf"  # Path to your PDF file
    extractor = SubjectiveInformationExtractor(pdf_path)
    subjective_info = extractor.extract()
    print("Subjective Information:", subjective_info)
