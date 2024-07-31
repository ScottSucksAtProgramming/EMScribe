# modules/reviewer.py
from .model_loader import ModelLoader
from .prompt_manager import PromptManager

class Reviewer:
    """
    A class to review sections of extracted data using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the Reviewer with a ModelLoader and PromptManager instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def review_section(self, section: str) -> str:
        """
        Reviews a section of the extracted data.

        Args:
            section (str): The section of extracted data to review.

        Returns:
            str: The AI model's response to the review prompt.
        """
        prompt = self.prompt_manager.get_prompt("review_section", section=section)
        return self.model_loader.generate(prompt)

    def final_review(self, updated_section):
        """
        Performs a final review of a section after changes have been made.
        
        Args:
            updated_section (str): The section of data after user modifications.
        
        Returns:
            str: The AI model's response after final review.
        """
        prompt = self.prompt_manager.get_prompt("final_review", updated_section=updated_section)
        response = self.model_loader.generate(prompt)
        return response