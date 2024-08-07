# tests/test_patient_demographics_extractor.py

import pytest
from modules.pdf_extractors.patient_demographics_extractor import (
    PatientDemographicsExtractor,
)


@pytest.fixture
def patient_demographics_extractor():
    return PatientDemographicsExtractor()


def test_extract_first_name(patient_demographics_extractor):
    text = "Name: Doe, John"
    first_name = patient_demographics_extractor._extract_first_name(text)
    assert first_name == "John"


def test_extract_first_name_not_found(patient_demographics_extractor):
    text = "Name:"
    first_name = patient_demographics_extractor._extract_first_name(text)
    assert first_name == "No first name found"


def test_extract_date_of_birth(patient_demographics_extractor):
    text = "DOB 01/01/1980"
    dob = patient_demographics_extractor._extract_date_of_birth(text)
    assert dob == "01/01/1980"


def test_extract_date_of_birth_not_found(patient_demographics_extractor):
    text = "Some other text without DOB"
    date_of_birth = patient_demographics_extractor._extract_date_of_birth(text)
    assert date_of_birth == "No date of birth found"


def test_extract_age(patient_demographics_extractor):
    text = "Age 40 Yrs, 11 Month, 1 Days"
    age = patient_demographics_extractor._extract_age(text)
    assert age == "40 Yrs"


def test_extract_age_not_found(patient_demographics_extractor):
    text = "Some other text without Age"
    age = patient_demographics_extractor._extract_age(text)
    assert age == "No age found"


def test_extract_gender(patient_demographics_extractor):
    text = "Gender Male State NY Local Protocol Provided"
    gender = patient_demographics_extractor._extract_gender(text)
    assert gender == "Male"


def test_extract_gender_not_found(patient_demographics_extractor):
    text = "Some other text without Gender"
    gender = patient_demographics_extractor._extract_gender(text)
    assert gender == "No gender found"
