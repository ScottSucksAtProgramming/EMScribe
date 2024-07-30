# modules/quality_controller.py

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager

class QualityController:
    """
    A class to review and refine the generated EMS narratives.
    
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
        Reviews the generated narrative for accuracy and completeness.

        Args:
            transcript (str): The cleaned transcript.
            narrative (str): The generated narrative.

        Returns:
            str: The improved narrative.
        """
        # Step 1: Compare the narrative to the transcript
        prompt = self.prompt_manager.get_prompt("compare_narrative_to_transcript", transcript=transcript, narrative=narrative)
        response = self.model_loader.generate(prompt)
        
        # Step 2: Check for missing required information
        prompt = self.prompt_manager.get_prompt("check_missing_information", narrative=narrative)
        response += "\n\n" + self.model_loader.generate(prompt)
        
        return response.strip()
