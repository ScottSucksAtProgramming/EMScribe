# modules/quality_controller.py

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager

class QualityController:
    """
    A class to perform quality control on EMS narratives.
    
    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the QualityController with a ModelLoader and PromptManager instance.
        
        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def review_narrative(self, transcript: str, narrative: str) -> str:
        """
        Reviews the narrative for discrepancies and missing information.
        
        Args:
            transcript (str): The cleaned transcript of the patient interaction.
            narrative (str): The generated narrative to review.

        Returns:
            str: The improved narrative after review.
        """
        # Compare the narrative to the transcript
        prompt = self.prompt_manager.get_prompt("compare_narrative_to_transcript", transcript=transcript, narrative=narrative)
        improved_narrative = self.model_loader.generate(prompt)

        # Check for missing information
        improved_narrative = self.check_required_info(improved_narrative)

        return improved_narrative

    def get_required_info(self) -> str:
        """
        Returns the required information template for the narrative format.
        
        Returns:
            str: The required information template.
        """
        # Define the required information for the narrative format
        required_info = """
        PRE-ARRIVAL:
        - Unit number
        - Response priority
        - Crew details
        - Dispatch information

        SUBJECTIVE:
        - Chief complaint
        - Onset
        - Provocation/Palliation
        - Quality
        - Radiation
        - Severity
        - Time

        OBJECTIVE:
        - General appearance
        - Vital signs
        - Physical exam findings
        - Diagnostics

        ASSESSMENT:
        - Field impression
        - Differential diagnosis

        PLAN:
        - Interventions
        - Medications administered
        - Response to treatment

        TRANSPORT:
        - Mode of transport
        - Destination
        - Changes en route
        - Handover details
        """
        return required_info

    def check_required_info(self, narrative: str, format: str = "presoaped_format") -> str:
        """
        Checks the narrative for required information and integrates missing elements.
        
        Args:
            narrative (str): The narrative to check.
            format (str): The narrative format.

        Returns:
            str: The narrative with missing elements integrated.
        """
        required_info = self.get_required_info()
        prompt = self.prompt_manager.get_prompt("check_missing_information", narrative=narrative, required_info=required_info)
        missing_elements = self.model_loader.generate(prompt)

        # Integrate missing elements into the narrative
        narrative_with_missing_info = self.integrate_missing_information(narrative, missing_elements)

        return narrative_with_missing_info

    def integrate_missing_information(self, narrative: str, missing_elements: str) -> str:
        """
        Integrates missing elements into the narrative.
        
        Args:
            narrative (str): The narrative to improve.
            missing_elements (str): The missing elements to add.

        Returns:
            str: The improved narrative with integrated missing elements.
        """
        return narrative + "\n\n" + missing_elements
