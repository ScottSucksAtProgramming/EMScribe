# CLI

EMScribe also includes a CLI tool to interact with the application.

## Commands:

1. `clean`
   - Cleans the provided transcript.
   - Usage: `emscribe clean <transcript_path> [--output <output_path>]`
   - Default output: `data/cleaned_transcript.txt`

2. `extract`
   - Extracts information from the provided transcript.
   - Usage: `emscribe extract <transcript_path> [--output <output_path>]`
   - Default input: `data/cleaned_transcript.txt`
   - Default output: `data/extract.txt`

3. `generate`
   - Generates a narrative from the extracted data.
   - Usage: `emscribe generate <transcript_path> [--output <output_path>]`
   - Default input: `data/reviewed_extract.txt`
   - Default output: `data/narrative.txt`

4. `review`
   - Reviews the extracted information.
   - Usage: `emscribe review <extracted_data_path> [--output <output_path
