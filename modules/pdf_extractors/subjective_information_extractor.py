import re


class SubjectiveInformationExtractor:
    def extract(self, text: str) -> dict:
        return {
            "Address or Facility Name": self._extract_address_or_facility_name(text),
            "Patient Location and Position": self._extract_patient_location_and_position(
                text
            ),
            "Patient Appearance": self._extract_patient_appearance(text),
            "Medical Equipment": self._extract_medical_equipment(text),
            "Patient Chief Complaint": self._extract_patient_chief_complaint(text),
        }

    def _extract_address_or_facility_name(self, text: str) -> str:
        match = re.search(r"Address or Facility Name:\s*([^\n]*)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No address or facility name found"

    def _extract_patient_location_and_position(self, text: str) -> str:
        match = re.search(
            r"Patient Location and Position:\s*([^\n]*)", text, re.IGNORECASE
        )
        if match:
            return match.group(1).strip()
        return "No patient location and position found"

    def _extract_patient_appearance(self, text: str) -> str:
        match = re.search(r"Patient Appearance:\s*([^\n]*)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No patient appearance found"

    def _extract_medical_equipment(self, text: str) -> str:
        match = re.search(r"Medical Equipment:\s*([^\n]*)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No medical equipment found"

    def _extract_patient_chief_complaint(self, text: str) -> str:
        match = re.search(r"Patient Chief Complaint:\s*([^\n]*)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No patient chief complaint found"
