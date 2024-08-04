# preprocess.py

import re
from modules.transcript_cleaner import TranscriptCleaner
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager


class TranscriptPreprocessor:
    def __init__(self, model_loader: ModelLoader, prompt_manager: PromptManager):
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager
        self.cleaner = TranscriptCleaner(model_loader, prompt_manager)

    def preprocess(self, transcript: str) -> str:
        cleaned_transcript = self.clean_transcript(transcript)
        return self.further_process(cleaned_transcript)

    def clean_transcript(self, transcript: str) -> str:
        return self.cleaner.clean(transcript)

    def further_process(self, cleaned_transcript: str) -> str:
        return re.sub(r"\s+", " ", cleaned_transcript).strip()


def run(model_loader: ModelLoader, prompt_manager: PromptManager):
    example_transcript = "example transcript text"
    preprocessor = TranscriptPreprocessor(model_loader, prompt_manager)
    cleaned_transcript = preprocessor.preprocess(example_transcript)
    print(cleaned_transcript)


if __name__ == "__main__":
    model_loader_instance = ModelLoader(
        base_url="http://localhost:11434", model_name="llama3.1"
    )
    prompt_manager_instance = PromptManager()
    run(model_loader_instance, prompt_manager_instance)
