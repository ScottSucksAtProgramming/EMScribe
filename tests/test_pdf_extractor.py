import pytest
from modules.pdf_extractor import PDFExtractor


@pytest.fixture
def pdf_extractor():
    # Initialize PDFExtractor with None for model_loader and prompt_manager since they are not used in the tests
    return PDFExtractor(None, None)


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
    text = """
    Mileage
    Delays
    Loaded Miles 0.8 geo-verified Response Delays None/No Delay
    Start Scene Delays None/No Delay
    End Transport Delays None/No Delay
    """
    response_delays = pdf_extractor._extract_response_delays(text)
    print(f"Extracted response delays: {response_delays}")
    assert response_delays == "None/No Delay"


def test_extract_response_delays_delay_other(pdf_extractor):
    text = """
    Mileage
    Delays
    Loaded Miles 0.8 geo-verified Response Delays Other (Not Listed)
    Start Scene Delays None/No Delay
    End Transport Delays None/No Delay
    """
    response_delays = pdf_extractor._extract_response_delays(text)
    print(f"Extracted response delays: {response_delays}")
    assert response_delays == "Other (Not Listed)"


def test_extract_response_delays_no_delays_mentioned(pdf_extractor):
    text = """
    Mileage
    Delays
    Loaded Miles 0.8 geo-verified
    Start Scene Delays None/No Delay
    End Transport Delays None/No Delay
    """
    response_delays = pdf_extractor._extract_response_delays(text)
    print(f"Extracted response delays: {response_delays}")
    assert response_delays == "No response delays found"


def test_extract_response_delays_partial_text(pdf_extractor):
    text = """
    Response Delays
    """
    response_delays = pdf_extractor._extract_response_delays(text)
    print(f"Extracted response delays: {response_delays}")
    assert response_delays == "No response delays found"


def test_extract_response_delays_unexpected_interruption(pdf_extractor):
    text = """
    Mileage
    Delays
    Loaded Miles 0.8 geo-verified Response Delays Unexpected text
    Start Scene Delays None/No Delay
    End Transport Delays None/No Delay
    """
    response_delays = pdf_extractor._extract_response_delays(text)
    print(f"Extracted response delays: {response_delays}")
    assert response_delays == "Unexpected text"


def test_extract_incident_location(pdf_extractor):
    text = """
    Incident Details
    Location Type Nursing Home Disposition
    Location Stony Brook University Hospital
    City Stony Brook Staged
    """
    incident_location = pdf_extractor._extract_incident_location(text)
    print(f"Extracted incident location: {incident_location}")
    assert incident_location == "Nursing Home in Stony Brook"


def test_extract_incident_location_partial_text(pdf_extractor):
    text = """
    Incident Details
    Location Type Nursing Home Disposition
    City Stony Brook Staged
    """
    incident_location = pdf_extractor._extract_incident_location(text)
    print(f"Extracted incident location: {incident_location}")
    assert incident_location == "Nursing Home in Stony Brook"


def test_extract_incident_location_no_location_type(pdf_extractor):
    text = """
    Incident Details
    Location Stony Brook University Hospital
    City Stony Brook
    """
    incident_location = pdf_extractor._extract_incident_location(text)
    print(f"Extracted incident location: {incident_location}")
    assert incident_location == "No incident location found"


def test_extract_incident_location_no_city(pdf_extractor):
    text = """
    Incident Details
    Location Type Nursing Home
    Location Stony Brook University Hospital
    """
    incident_location = pdf_extractor._extract_incident_location(text)
    print(f"Extracted incident location: {incident_location}")
    assert incident_location == "No incident location found"


def test_extract_dispatch_complaint(pdf_extractor):
    text = "EMD Complaint Transfer/Interfacility/Palliative Care Country US"
    dispatch_complaint = pdf_extractor._extract_dispatch_complaint(text)
    print(f"Extracted dispatch complaint: {dispatch_complaint}")
    assert dispatch_complaint == "Transfer/Interfacility/Palliative Care"


def test_extract_dispatch_complaint_partial_text(pdf_extractor):
    text = "EMD Complaint Transfer/Interfacility/Palliative Care"
    dispatch_complaint = pdf_extractor._extract_dispatch_complaint(text)
    print(f"Extracted dispatch complaint: {dispatch_complaint}")
    assert dispatch_complaint == "Transfer/Interfacility/Palliative Care"


def test_extract_dispatch_complaint_no_complaint(pdf_extractor):
    text = "EMD Complaint"
    dispatch_complaint = pdf_extractor._extract_dispatch_complaint(text)
    print(f"Extracted dispatch complaint: {dispatch_complaint}")
    assert dispatch_complaint == "No dispatch complaint found"
