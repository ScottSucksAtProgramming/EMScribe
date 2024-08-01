import sys
import os


class GenerateCommand:
    def __init__(self, narrative_manager):
        self.narrative_manager = narrative_manager

    def execute(self, extracted_data_path, output_path="data/narrative.txt"):
        if extracted_data_path == "-":
            extracted_data = sys.stdin.read()
        else:
            with open(extracted_data_path, "r") as file:
                extracted_data = file.read()

        narrative = self.narrative_manager.generate_narrative(
            "presoaped_format", data=extracted_data
        )

        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as file:
                file.write(narrative)
        else:
            print(narrative)
            import pyperclip

            pyperclip.copy(narrative)
