import pdfplumber
import re
import io


class PDFExtractor:
    def __init__(self, model_loader, prompt_manager):
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def extract(self, content: bytes) -> dict:
        text = self._extract_text(content)
        data = {
            "Incident Information": {
                "Unit": self._extract_unit(text),
                "Response Mode": self._extract_response_mode(text),
                "Crew Type": self._extract_crew_type(text),
                "Response Delays": self._extract_response_delays(text),
                "Incident Location": self._extract_incident_location(text),
                "Dispatch Complaint": self._extract_dispatch_complaint(text),
            },
            # Add other categories similarly
        }
        return data

    def _extract_text(self, content: bytes) -> str:
        """Extracts and concatenates text from all pages of a PDF."""
        text = ""
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                text += page_text + "\n"
        return text

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
        """Extracts the crew type from the text."""
        match = re.search(r"Crew Type\s+([\w\s]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No crew type found"

    def _extract_response_delays(self, text: str) -> str:
        """Extracts the response delays from the text."""
        match = re.search(r"Response Delays\s+([\w\s]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No response delays found"

    def _extract_incident_location(self, text: str) -> str:
        """Extracts the incident location from the text."""
        match = re.search(r"Incident Location\s+([\w\s,]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No incident location found"

    def _extract_dispatch_complaint(self, text: str) -> str:
        """Extracts the dispatch complaint from the text."""
        match = re.search(r"Dispatch Complaint\s+([\w\s]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "No dispatch complaint found"


# Example usage
if __name__ == "__main__":
    with open("pdf_1.pdf", "rb") as file:
        content = file.read()
    pdf_extractor = PDFExtractor(None, None)
    extracted_data = pdf_extractor.extract(content)
    for category, info in extracted_data.items():
        print(f"{category}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
