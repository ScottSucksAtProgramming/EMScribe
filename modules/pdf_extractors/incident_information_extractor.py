import re


class IncidentInformationExtractor:
    def extract(self, text: str) -> dict:
        return {
            "Unit": self._extract_unit(text),
            "Response Mode": self._extract_response_mode(text),
            "Crew Type": self._extract_crew_type(text),
            "Response Delays": self._extract_response_delays(text),
            "Incident Location": self._extract_incident_location(text),
            "Dispatch Complaint": self._extract_dispatch_complaint(text),
        }

    def _extract_unit(self, text: str) -> str:
        """Extracts the unit number from the text."""
        match = re.search(r"Medic Vehicle\s+([\d\-]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No unit found"

    def _extract_response_mode(self, text: str) -> str:
        """Extracts the response mode from the text."""
        match = re.search(r"Response Mode\s+([^\n]+)", text, re.IGNORECASE)
        if match:
            response_mode = match.group(1).split(" ")[
                0
            ]  # Ensure only the first word is captured
            return response_mode.strip()
        return "No response mode found"

    def _extract_crew_type(self, text: str) -> str:
        """Extracts and infers the crew type from the text."""
        crew_members = self._extract_crew_members(text)
        num_personnel = len(crew_members)
        if num_personnel == 1:
            return "Medic Only"
        elif num_personnel >= 2:
            return "Full Crew"
        return "No crew type found"

    def _extract_crew_members(self, text: str) -> list:
        """Extracts the list of crew members from the text."""
        crew_members = []
        lines = text.split("\n")
        in_crew_section = False

        for line in lines:
            line = line.strip()

            if in_crew_section:
                if line.lower().startswith("transport"):
                    break
                match = re.match(r"([A-Za-z]+),\s*([A-Za-z]+)", line)
                if match:
                    crew_members.append(
                        (match.group(1).upper(), match.group(2).upper())
                    )  # Normalize to uppercase

            if line.lower().startswith("crew members"):
                in_crew_section = True

        return crew_members

    def _extract_response_delays(self, text: str) -> str:
        """Extracts the response delays from the text."""
        match = re.search(r"Response Delays\s*([^\n]*)", text, re.IGNORECASE)
        if match:
            response_delays = match.group(1).strip()
            if response_delays:
                return response_delays
            else:
                return "No response delays found"
        return "No response delays found"

    def _extract_incident_location(self, text: str) -> str:
        """Extracts the incident location details from the text."""
        location_type = self._extract_between(text, "Location Type", "Disposition")
        city = self._extract_between(text, "City", "Staged")

        if location_type and city:
            return f"{location_type} in {city}"
        return "No incident location found"

    def _extract_between(self, text: str, start: str, end: str) -> str:
        """Extracts text between two markers."""
        pattern = rf"{start}\s*([^\n]+?)\s*{end}"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            extracted_text = match.group(1).strip()
            return extracted_text
        return None

    def _extract_dispatch_complaint(self, text: str) -> str:
        """Extracts the dispatch complaint from the text."""
        match = re.search(r"EMD Complaint\s+([^\n]*)", text, re.IGNORECASE)
        if match:
            dispatch_complaint = match.group(1).strip()
            if dispatch_complaint:
                return dispatch_complaint.split("Country")[
                    0
                ].strip()  # Stop before the word "Country"
        return "No dispatch complaint found"
