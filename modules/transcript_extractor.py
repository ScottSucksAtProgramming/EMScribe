from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager

class TranscriptExtractor:
    """
    A class to extract information from EMS transcripts using an AI model.

    Attributes:
        model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
        prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
    """

    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        """
        Initializes the TranscriptExtractor with a ModelLoader instance and a PromptManager instance.

        Args:
            model_loader (ModelLoader): An instance of ModelLoader to interact with the AI model.
            prompt_manager (PromptManager): An instance of PromptManager to manage prompts.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def extract(self, transcript: str) -> dict:
        """
        Extracts information from the transcript using the specified prompts.

        Args:
            transcript (str): The transcript to extract information from.

        Returns:
            dict: A dictionary containing the extracted information.
        """
        extracted_data = {}
        prompts = self.prompt_manager.get_prompts()
        
        for key, prompt in prompts.items():
            full_prompt = prompt.format(transcript=transcript)
            response = self.model_loader.generate(full_prompt)
            extracted_text = response.generations[0][0].text.strip()
            extracted_data[key] = extracted_text
        
        return extracted_data