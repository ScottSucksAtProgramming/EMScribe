import re


class HistoryOfPresentIllnessExtractor:
    def extract(self, text: str) -> dict:
        return {
            "Associated Signs and Symptoms": self._extract_associated_signs_and_symptoms(
                text
            ),
            "Onset": self._extract_onset(text),
            "Provocation": self._extract_provocation(text),
            "Palliation": self._extract_palliation(text),
            "Quality": self._extract_quality(text),
            "Radiation": self._extract_radiation(text),
            "Severity": self._extract_severity(text),
            "Time": self._extract_time(text),
            "Interventions": self._extract_interventions(text),
            "Additional History of Present Illness": self._extract_additional_history_of_present_illness(
                text
            ),
        }

    def _extract_field(self, text: str, field: str) -> str:
        pattern = rf"{field}\s*([^\n]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "[No Info]"

    def _extract_associated_signs_and_symptoms(self, text: str) -> str:
        return self._extract_field(text, "Associated Signs and Symptoms")

    def _extract_onset(self, text: str) -> str:
        return self._extract_field(text, "Onset")

    def _extract_provocation(self, text: str) -> str:
        return self._extract_field(text, "Provocation")

    def _extract_palliation(self, text: str) -> str:
        return self._extract_field(text, "Palliation")

    def _extract_quality(self, text: str) -> str:
        return self._extract_field(text, "Quality")

    def _extract_radiation(self, text: str) -> str:
        return self._extract_field(text, "Radiation")

    def _extract_severity(self, text: str) -> str:
        return self._extract_field(text, "Severity")

    def _extract_time(self, text: str) -> str:
        return self._extract_field(text, "Time")

    def _extract_interventions(self, text: str) -> str:
        return self._extract_field(text, "Interventions")

    def _extract_additional_history_of_present_illness(self, text: str) -> str:
        return self._extract_field(text, "Additional History of Present Illness")
