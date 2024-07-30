# modules/reviewer.py
from .model_loader import ModelLoader
from .prompt_manager import PromptManager

class Reviewer:
    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def review_section(self, section_data: str) -> str:
        prompt = self.prompt_manager.get_prompt("review_section", section_data=section_data)
        response = self.model_loader.generate(prompt)
        return response

    def final_review(self, updated_section: str) -> str:
        prompt = self.prompt_manager.get_prompt("final_review", updated_section=updated_section)
        response = self.model_loader.generate(prompt)
        return response