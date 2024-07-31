import pytest
from unittest.mock import Mock, patch
from commands.review_command import ReviewCommand
from modules.extract_reviewer import ExtractReviewer

@pytest.fixture
def mock_reviewer():
    mock_reviewer = Mock(spec=ExtractReviewer)
    return mock_reviewer

def test_review_command_processes_sections_correctly(mock_reviewer, tmp_path):
    review_command = ReviewCommand(mock_reviewer)
    extracted_data_path = tmp_path / "extracted_data.txt"
    output_path = tmp_path / "output.txt"
    
    extracted_data = (
        "Incident Information\n- Unit:\n- Response Mode: emergent\n\n"
        "Patient Demographics\n- Name: John Doe\n- Age: 45\n"
    )
    with open(extracted_data_path, 'w') as file:
        file.write(extracted_data)
    
    mock_reviewer.review_section.side_effect = [
        "Incident Information\n- Unit: 292\n- Response Mode: emergent",
        "Patient Demographics\n- Name: John Doe\n- Age: 45"
    ]
    
    with patch('builtins.input', side_effect=['skip', 'skip']):
        with patch('os.system') as mock_os_system:
            review_command.execute(extracted_data_path, output_path)
            mock_os_system.assert_called()
    
    with open(output_path, 'r') as file:
        reviewed_data = file.read()
    
    expected_output = (
        "Incident Information\n- Unit: 292\n- Response Mode: emergent\n\n"
        "Patient Demographics\n- Name: John Doe\n- Age: 45\n"
    )
    assert reviewed_data == expected_output

def test_review_command_handles_user_input_correctly(mock_reviewer, tmp_path):
    review_command = ReviewCommand(mock_reviewer)
    extracted_data_path = tmp_path / "extracted_data.txt"
    output_path = tmp_path / "output.txt"
    
    extracted_data = "Incident Information\n- Unit:\n- Response Mode: emergent\n"
    with open(extracted_data_path, 'w') as file:
        file.write(extracted_data)
    
    mock_reviewer.review_section.side_effect = [
        "Incident Information\n- Unit: 292\n- Response Mode: emergent"
    ]
    
    with patch('builtins.input', side_effect=['add unit number of 292', 'yes']):
        with patch('os.system') as mock_os_system:
            review_command.execute(extracted_data_path, output_path)
            mock_os_system.assert_called()
    
    with open(output_path, 'r') as file:
        reviewed_data = file.read()
    
    expected_output = "Incident Information\n- Unit: 292\n- Response Mode: emergent\n"
    assert reviewed_data == expected_output

def test_review_command_saves_reviewed_data_correctly(mock_reviewer, tmp_path):
    review_command = ReviewCommand(mock_reviewer)
    extracted_data_path = tmp_path / "extracted_data.txt"
    output_path = tmp_path / "output.txt"
    
    extracted_data = "Incident Information\n- Unit:\n- Response Mode: emergent\n"
    with open(extracted_data_path, 'w') as file:
        file.write(extracted_data)
    
    mock_reviewer.review_section.side_effect = [
        "Incident Information\n- Unit: 292\n- Response Mode: emergent"
    ]
    
    with patch('builtins.input', side_effect=['skip']):
        with patch('os.system') as mock_os_system:
            review_command.execute(extracted_data_path, output_path)
            mock_os_system.assert_called()
    
    with open(output_path, 'r') as file:
        reviewed_data = file.read()
    
    expected_output = "Incident Information\n- Unit: 292\n- Response Mode: emergent\n"
    assert reviewed_data == expected_output