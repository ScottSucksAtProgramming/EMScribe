# modules/pdf_extractors/patient_demographics_extractor.py

import re


class PatientDemographicsExtractor:
    def extract(self, text: str) -> dict:
        return {
            "Name": self._extract_first_name(text),
            "Date of Birth": self._extract_date_of_birth(text),
            "Age": self._extract_age(text),
            "Gender": self._extract_gender(text),
        }

    def _extract_first_name(self, text: str) -> str:
        match = re.search(r"Name:\s*([A-Z]+),\s*([A-Z]+)", text, re.IGNORECASE)
        if match:
            return match.group(2).capitalize()  # Return the first name part
        return "No first name found"

    def _extract_date_of_birth(self, text: str) -> str:
        match = re.search(r"DOB\s*([\d/]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No date of birth found"

    def _extract_age(self, text: str) -> str:
        match = re.search(r"Age\s*([^,]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No age found"

    def _extract_gender(self, text: str) -> str:
        match = re.search(r"Gender\s*([^\s]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No gender found"
