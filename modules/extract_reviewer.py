from typing import Optional

from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager


class ExtractReviewer:
    """
    A class to handle the review and final review of extracted data sections using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader for loading the AI model.
        prompt_manager (PromptManager): An instance of PromptManager for managing prompts.

    Methods:
        review_section(section: str, user_input: Optional[str] = None) -> str:
            Reviews a section of extracted data using the AI model.

        final_review(updated_section: str) -> str:
            Performs a final review of a section after changes have been made.

        _get_review_prompt(prompt_key: str, section: str, user_input: Optional[str] = None) -> str:
            Retrieves and formats the review prompt.

        _generate_response(prompt: str) -> str:
            Generates a response from the AI model based on the provided prompt.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def review_section(self, section: str, user_input: Optional[str] = None) -> str:
        """
        Reviews a section of extracted data using the AI model.

        Args:
            section (str): The section of extracted data to review.
            user_input (Optional[str]): The user's input for modifications.

        Returns:
            str: The AI model's response.
        """
        prompt = self._get_review_prompt("review_section", section, user_input)
        return self._generate_response(prompt)

    def final_review(self, updated_section: str) -> str:
        """
        Performs a final review of a section after changes have been made.

        Args:
            updated_section (str): The section of data after user modifications.

        Returns:
            str: The AI model's response after final review.
        """
        prompt = self.prompt_manager.get_prompt(
            "final_review", updated_section=updated_section
        )
        return self._generate_response(prompt)

    def _get_review_prompt(
        self, prompt_key: str, section: str, user_input: Optional[str] = None
    ) -> str:
        """
        Retrieves and formats the review prompt.

        Args:
            prompt_key (str): The key for the review prompt.
            section (str): The section of extracted data.
            user_input (Optional[str]): The user's input for modifications.

        Returns:
            str: The formatted review prompt.
        """
        if user_input:
            return self.prompt_manager.get_prompt(
                prompt_key, section_data=section, user_input=user_input
            )
        return self.prompt_manager.get_prompt(prompt_key, section_data=section)

    def _generate_response(self, prompt: str) -> str:
        """
        Generates a response from the AI model based on the provided prompt.

        Args:
            prompt (str): The input prompt for the model.

        Returns:
            str: The AI model's response.
        """
        context_window_size = (
            self.model_loader.context_window
        )  # Use the dynamic context window size

        if len(prompt) > context_window_size:
            response_parts = [
                self.model_loader.generate(prompt[i : i + context_window_size])
                for i in range(0, len(prompt), context_window_size)
            ]
            return " ".join(response_parts)

        return self.model_loader.generate(prompt)
