import os
from modules.transcript_extractor import TranscriptExtractor
from modules.utils import sliding_window_transcript

class ExtractCommand:
    def __init__(self, extractor=None):
        if extractor is None:
            extractor = TranscriptExtractor()
        self.extractor = extractor

    def execute(self, input_path="data/cleaned_transcript.txt", output_path="data/extract.txt"):
        with open(input_path, 'r') as file:
            transcript = file.read()

        max_tokens = 4096  # Example token limit for the model
        overlap_tokens = 250  # Example overlap

        chunks = sliding_window_transcript(transcript, max_tokens, overlap_tokens)
        extracted_chunks = [self.extractor.extract(chunk) for chunk in chunks]

        extracted_data = '\n'.join(extracted_chunks)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as file:
            file.write(extracted_data)

        print(f"\n\nExtracted data saved to {output_path}")
