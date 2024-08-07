import pytest
from modules.pdf_extractors.subjective_information_extractor import (
    SubjectiveInformationExtractor,
)


@pytest.fixture
def subjective_information_extractor():
    return SubjectiveInformationExtractor()


import pytest
from modules.pdf_extractors.subjective_information_extractor import (
    SubjectiveInformationExtractor,
)


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


def test_extract_patient_location_and_position(subjective_information_extractor):
    text = "Subjective Information\nPatient Location and Position: Room 101, Supine"
    result = subjective_information_extractor._extract_patient_location_and_position(
        text
    )
    assert result == "Room 101, Supine"


def test_extract_patient_appearance(subjective_information_extractor):
    text = "Subjective Information\nPatient Appearance: Conscious, alert"
    result = subjective_information_extractor._extract_patient_appearance(text)
    assert result == "Conscious, alert"


def test_extract_medical_equipment(subjective_information_extractor):
    text = "Subjective Information\nMedical Equipment: IV, Oxygen"
    result = subjective_information_extractor._extract_medical_equipment(text)
    assert result == "IV, Oxygen"


def test_extract_patient_chief_complaint(subjective_information_extractor):
    text = "Subjective Information\nPatient Chief Complaint: Chest pain"
    result = subjective_information_extractor._extract_patient_chief_complaint(text)
    assert result == "Chest pain"


# Edge cases
def test_no_address_or_facility_name(subjective_information_extractor):
    text = "Subjective Information\nAddress or Facility Name:"
    result = subjective_information_extractor._extract_address_or_facility_name(text)
    assert result == "No address or facility name found"


def test_no_patient_location_and_position(subjective_information_extractor):
    text = "Subjective Information\nPatient Location and Position:"
    result = subjective_information_extractor._extract_patient_location_and_position(
        text
    )
    assert result == "No patient location and position found"


def test_no_patient_appearance(subjective_information_extractor):
    text = "Subjective Information\nPatient Appearance:"
    result = subjective_information_extractor._extract_patient_appearance(text)
    assert result == "No patient appearance found"


def test_no_medical_equipment(subjective_information_extractor):
    text = "Subjective Information\nMedical Equipment:"
    result = subjective_information_extractor._extract_medical_equipment(text)
    assert result == "No medical equipment found"


def test_no_patient_chief_complaint(subjective_information_extractor):
    text = "Subjective Information\nPatient Chief Complaint:"
    result = subjective_information_extractor._extract_patient_chief_complaint(text)
    assert result == "No patient chief complaint found"
