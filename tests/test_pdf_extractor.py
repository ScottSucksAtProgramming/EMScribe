import pytest
from modules.pdf_extractor import PDFExtractor


@pytest.fixture
def pdf_extractor():
    # Initialize PDFExtractor with None for model_loader and prompt_manager since they are not used in the tests
    return PDFExtractor(None, None)


def test_extract_text(pdf_extractor):
    with open("tests/data/sample.pdf", "rb") as file:
        content = file.read()
    text = pdf_extractor._extract_text(content)
    assert isinstance(text, str)
    assert len(text) > 0  # Ensure text is extracted


def test_extract_unit(pdf_extractor):
    text = "Medic Vehicle 5-41-19"
    unit = pdf_extractor._extract_unit(text)
    assert unit == "5-41-19"


def test_extract_response_mode(pdf_extractor):
    text = "Response Mode Non-Emergent"
    response_mode = pdf_extractor._extract_response_mode(text)
    assert response_mode == "Non-Emergent"


def test_extract_crew_type_medic_only(pdf_extractor):
    text = """
    Crew Members
    SMITH, JOHN - Driver - Response, Driver - Transport 2009 Paramedic (New York) - 366399
    """
    crew_type = pdf_extractor._extract_crew_type(text)
    assert crew_type == "Medic Only"


def test_extract_crew_type_full_crew(pdf_extractor):
    text = """
    Crew Members
    SMITH, JOHN - Driver - Response, Driver - Transport 2009 Paramedic (New York) - 366399
    DOE, JANE - Lead - At Scene, Lead - Transport 2009 Paramedic (New York) - 454663
    """
    crew_type = pdf_extractor._extract_crew_type(text)
    assert crew_type == "Full Crew"


def test_extract_crew_members(pdf_extractor):
    text = """
    Crew Members
    Personnel Role Certification Level
    Driver - Response, Driver
    SMITH, JOHN 2009 Paramedic (New York) - 366399
    - Transport
    Lead - At Scene, Lead -
    DOE, JANE 2009 Paramedic (New York) - 454663
    """
    crew_members = pdf_extractor._extract_crew_members(text)
    print(f"Extracted crew members: {crew_members}")
    assert len(crew_members) == 2
    assert crew_members[0] == ("SMITH", "JOHN")
    assert crew_members[1] == ("DOE", "JANE")


def test_extract_crew_members_multiple_lines(pdf_extractor):
    text = """
    Crew Members
    Driver - Response, Driver
    SMITH, JOHN 2009 Paramedic (New York) - 366399
    Lead - At Scene, Lead -
    DOE, JANE 2009 Paramedic (New York) - 454663
    Transport
    """
    crew_members = pdf_extractor._extract_crew_members(text)
    print(f"Extracted crew members: {crew_members}")
    assert len(crew_members) == 2
    assert crew_members[0] == ("SMITH", "JOHN")
    assert crew_members[1] == ("DOE", "JANE")


def test_extract_crew_members_case_insensitive(pdf_extractor):
    text = """
    Crew Members
    Driver - Response, Driver
    smith, john 2009 Paramedic (New York) - 366399
    Lead - At Scene, Lead -
    doe, jane 2009 Paramedic (New York) - 454663
    Transport
    """
    crew_members = pdf_extractor._extract_crew_members(text)
    print(f"Extracted crew members: {crew_members}")
    assert len(crew_members) == 2
    assert crew_members[0] == ("SMITH", "JOHN")
    assert crew_members[1] == ("DOE", "JANE")


def test_extract_crew_members_unexpected_interruption(pdf_extractor):
    text = """
    Crew Members
    Driver - Response, Driver
    SMITH, JOHN 2009 Paramedic (New York) - 366399
    Lead - At Scene, Lead -
    Some unexpected text
    DOE, JANE 2009 Paramedic (New York) - 454663
    Transport
    """
    crew_members = pdf_extractor._extract_crew_members(text)
    print(f"Extracted crew members: {crew_members}")
    assert len(crew_members) == 2
    assert crew_members[0] == ("SMITH", "JOHN")
    assert crew_members[1] == ("DOE", "JANE")


def test_extract_crew_members_no_names(pdf_extractor):
    text = """
    Crew Members
    Personnel Role Certification Level
    Transport
    """
    crew_members = pdf_extractor._extract_crew_members(text)
    print(f"Extracted crew members: {crew_members}")
    assert len(crew_members) == 0


def test_extract_response_delays(pdf_extractor):
    text = "Response Delays None"
    response_delays = pdf_extractor._extract_response_delays(text)
    assert response_delays == "None"


def test_extract_incident_location(pdf_extractor):
    text = "Incident Location Stony Brook University Hospital"
    incident_location = pdf_extractor._extract_incident_location(text)
    assert incident_location == "Stony Brook University Hospital"


def test_extract_dispatch_complaint(pdf_extractor):
    text = "Dispatch Complaint Chest Pain"
    dispatch_complaint = pdf_extractor._extract_dispatch_complaint(text)
    assert dispatch_complaint == "Chest Pain"
