class Reviewer:
    def __init__(self, model_loader, prompt_manager):
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def review_section(self, section, user_input=None):
        """
        Reviews a section of extracted data using the AI model.
        
        Args:
            section (str): The section of extracted data to review.
            user_input (str): The user's input for modifications.
        
        Returns:
            str: The AI model's response.
        """
        if user_input:
            prompt = self.prompt_manager.get_prompt("review_section", section_data=section, user_input=user_input)
        else:
            prompt = self.prompt_manager.get_prompt("review_section", section_data=section)
        response = self.model_loader.generate(prompt)
        return response

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