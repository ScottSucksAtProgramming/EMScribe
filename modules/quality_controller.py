# modules/quality_controller.py

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager

class QualityController:
    """
    A class to review and refine EMS narratives for accuracy and completeness.
    
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

    def review_narrative(self, narrative: str, transcript: str) -> str:
        """
        Reviews the narrative against the transcript for accuracy.

        Args:
            narrative (str): The generated narrative.
            transcript (str): The cleaned transcript.

        Returns:
            str: The review results indicating any discrepancies or missing information.
        """
        prompt = self.prompt_manager.get_quality_controller_prompt("review_narrative", narrative=narrative, transcript=transcript)
        response = self.model_loader.generate(prompt)
        return response

    def identify_missing_information(self, narrative: str, transcript: str) -> str:
        """
        Identifies missing information in the narrative.

        Args:
            narrative (str): The generated narrative.
            transcript (str): The cleaned transcript.

        Returns:
            str: The list of missing information or prompts to fill in the gaps.
        """
        prompt = self.prompt_manager.get_quality_controller_prompt("identify_missing_information", narrative=narrative, transcript=transcript)
        response = self.model_loader.generate(prompt)
        return response
