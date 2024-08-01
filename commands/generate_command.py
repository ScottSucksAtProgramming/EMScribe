import os
from modules.narrative_manager import NarrativeManager
from modules.utils import sliding_window_transcript
from modules.model_loader import ModelLoader
from modules.prompt_manager import PromptManager

class GenerateCommand:
    def __init__(self, manager=None):
        if manager is None:
            manager = NarrativeManager()
        self.manager = manager

    def execute(self, input_path="data/reviewed_extract.txt", output_path="data/narrative.txt"):
        with open(input_path, 'r') as file:
            extracted_data = file.read()

        max_tokens = 1024  # Example token limit for the model
        overlap_tokens = 100  # Example overlap

        chunks = sliding_window_transcript(extracted_data, max_tokens, overlap_tokens)
        generated_chunks = [self.manager.generate(chunk) for chunk in chunks]

        narrative = ' '.join(generated_chunks)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as file:
            file.write(narrative)

        print(f"\n\nNarrative saved to {output_path}")
