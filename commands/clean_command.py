import os
from modules.transcript_cleaner import TranscriptCleaner
from modules.utils import sliding_window_transcript

class CleanCommand:
    def __init__(self, cleaner=None):
        if cleaner is None:
            cleaner = TranscriptCleaner()
        self.cleaner = cleaner

    def execute(self, input_path, output_path="data/cleaned_transcript.txt"):
        with open(input_path, 'r') as file:
            transcript = file.read()

        max_tokens = 1024  # Example token limit for the model
        overlap_tokens = 100  # Example overlap

        chunks = sliding_window_transcript(transcript, max_tokens, overlap_tokens)
        cleaned_chunks = [self.cleaner.clean(chunk) for chunk in chunks]

        cleaned_transcript = ' '.join(cleaned_chunks)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as file:
            file.write(cleaned_transcript)

        print(f"\n\nCleaned transcript saved to {output_path}")
