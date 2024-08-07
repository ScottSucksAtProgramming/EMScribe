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
        match = re.search(r"Location\s+(.+?)\s+Unit", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No address or facility name found"

    def _extract_patient_location_and_position(self, text: str) -> str:
        return "[No Info]"

    def _extract_patient_appearance(self, text: str) -> str:
        return "[No Info]"

    def _extract_medical_equipment(self, text: str) -> str:
        return "[No Info]"

    def _extract_patient_chief_complaint(self, text: str) -> str:
        match = re.search(r"Chief Complaint\s*([^\n]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No chief complaint found"
