import pytest
from modules.pdf_extractors.subjective_information_extractor import (
    SubjectiveInformationExtractor,
)
from modules.pdf_extractors.subjective_information_extractor import (
    SubjectiveInformationExtractor,
)


@pytest.fixture
def subjective_information_extractor():
    return SubjectiveInformationExtractor()


@pytest.fixture
def subjective_information_extractor():
    return SubjectiveInformationExtractor()


def test_extract_address_or_facility_name(subjective_information_extractor):
    text = """
    Incident Details Destination Details Incident Times
    Location Type Hospital Disposition PSAP Call 17:57:00
    Location Stony Brook University Hospital Unit Disposition Patient Contact Made Dispatch Notified
    Patient Evaluation and/or
    """
    address_or_facility_name = (
        subjective_information_extractor._extract_address_or_facility_name(text)
    )
    assert address_or_facility_name == "Stony Brook University Hospital"


def test_extract_address_or_facility_name_not_found(subjective_information_extractor):
    text = """
    Incident Details Destination Details Incident Times
    Location Type Hospital Disposition PSAP Call 17:57:00
    Location Unit Disposition Patient Contact Made Dispatch Notified
    Patient Evaluation and/or
    """
    address_or_facility_name = (
        subjective_information_extractor._extract_address_or_facility_name(text)
    )
    assert address_or_facility_name == "No address or facility name found"


def test_extract_patient_chief_complaint(subjective_information_extractor):
    text = """
    General/Global
    Weight 176.4 lbs - 80.0 kg Tel Onset Time
    Height 6 ft, 4.0 in - 193.0 cm Physician Last Known Well 17:57:00 07/26/2024
    Pedi Color Phys. Tel Chief Complaint Severe abdominal pain
    SSN Ethnicity Not Hispanic or Latino Duration 5 Units Minutes
    Race White Secondary Complaint
    """
    result = subjective_information_extractor._extract_patient_chief_complaint(text)
    assert result == "Severe abdominal pain"


def test_extract_patient_chief_complaint_not_found(subjective_information_extractor):
    text = """
    General/Global
    Weight 176.4 lbs - 80.0 kg Tel Onset Time
    Height 6 ft, 4.0 in - 193.0 cm Physician Last Known Well 17:57:00 07/26/2024
    Pedi Color Phys. Tel SSN Ethnicity Not Hispanic or Latino Duration 5 Units Minutes
    Race White Secondary Complaint
    """
    result = subjective_information_extractor._extract_patient_chief_complaint(text)
    assert result == "No chief complaint found"
