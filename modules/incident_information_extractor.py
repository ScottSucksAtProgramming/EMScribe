import pandas as pd
from dataclasses import asdict, dataclass, field
from modules.base_pdf_extractor import BasePDFExtractor


@dataclass
class IncidentInformation:
    unit: str = field(default="")
    response_mode: str = field(default="")
    crew_type: str = field(default="")
    response_delays: str = field(default="")
    incident_location: str = field(default="")
    dispatch_complaint: str = field(default="")


class IncidentInformationExtractor(BasePDFExtractor):
    def __init__(self, pdf_path):
        super().__init__(pdf_path)
        self.incident_info = IncidentInformation()

    def extract_crew_type(self):
        crew_members_table = None

        import pdfplumber  # type: ignore

        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table)
                    if "Personnel" in df.values and "Certification Level" in df.values:
                        crew_members_table = df
                        break
                if crew_members_table is not None:
                    break

        if crew_members_table is None:
            self.incident_info.crew_type = "Not found"
            return

        # Remove any empty rows
        crew_members_table.dropna(how="all", inplace=True)

        # Filter relevant columns
        personnel_col = crew_members_table.iloc[:, 0]
        certification_col = crew_members_table.iloc[:, 2]

        # Determine crew type
        paramedic_or_emt_count = 0
        driver_count = 0

        for cert in certification_col:
            if cert is not None:
                if "Paramedic" in cert or "Emergency Medical Technician" in cert:
                    paramedic_or_emt_count += 1
                else:
                    driver_count += 1

        if paramedic_or_emt_count == 1 and driver_count == 0:
            self.incident_info.crew_type = "Medic Only"
        elif driver_count == 1 and paramedic_or_emt_count == 0:
            self.incident_info.crew_type = "Driver Only"
        elif paramedic_or_emt_count + driver_count >= 2:
            self.incident_info.crew_type = "Full Crew"
        else:
            self.incident_info.crew_type = "Unable to determine"

    def extract_unit_and_response_mode(self):
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
            return  # Handle case where table is not found

        # Remove any empty rows
        incident_details_table.dropna(how="all", inplace=True)

        # Extract Unit from "Medic Vehicle"
        medic_vehicle_row = incident_details_table[
            incident_details_table.iloc[:, 0] == "Medic Vehicle"
        ]
        if not medic_vehicle_row.empty:
            self.incident_info.unit = medic_vehicle_row.iloc[0, 1]

        # Extract Response Mode
        response_mode_row = incident_details_table[
            incident_details_table.iloc[:, 0] == "Response Mode"
        ]
        if not response_mode_row.empty:
            self.incident_info.response_mode = response_mode_row.iloc[0, 1]

    def extract_incident_location_and_dispatch_complaint(self):
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
            return  # Handle case where table is not found

        # Remove any empty rows
        incident_details_table.dropna(how="all", inplace=True)

        # Extract Incident Location (assuming it's in the "Address" or "Location" row)
        location_row = incident_details_table[
            incident_details_table.iloc[:, 0].str.contains("Location", na=False)
        ]
        if not location_row.empty:
            self.incident_info.incident_location = location_row.iloc[0, 1]

        # Extract Dispatch Complaint
        dispatch_complaint_row = incident_details_table[
            incident_details_table.iloc[:, 0] == "EMD Complaint"
        ]
        if not dispatch_complaint_row.empty:
            self.incident_info.dispatch_complaint = dispatch_complaint_row.iloc[0, 1]

    def extract_response_delays(self):
        response_delays_table = None

        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table)
                    if "Response Delays" in df.values:
                        response_delays_table = df
                        break
                if response_delays_table is not None:
                    break

        if response_delays_table is None:
            self.incident_info.response_delays = "Not found"
            return

        # Extract the "Response Delays" information
        response_delays_row = response_delays_table[
            response_delays_table.iloc[:, 3] == "Response Delays"
        ]
        if not response_delays_row.empty:
            self.incident_info.response_delays = response_delays_row.iloc[0, 4].strip()
        else:
            self.incident_info.response_delays = "Not available"

    def extract(self):
        self.extract_crew_type()
        self.extract_unit_and_response_mode()
        self.extract_incident_location_and_dispatch_complaint()
        self.extract_response_delays()
        # Add methods to extract other fields and populate self.incident_info

        return asdict(
            self.incident_info
        )  # Convert dataclass to dictionary before returning


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"  # Update with your actual PDF path
    extractor = IncidentInformationExtractor(pdf_path)
    incident_info = extractor.extract()
    print("Incident Information:", incident_info)
