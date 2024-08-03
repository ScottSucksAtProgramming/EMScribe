# -*- coding: utf-8 -*-
import sys
import os
import pyperclip


class GenerateCommand:
    """
    Command to generate a narrative from extracted EMS data.

    This command reads extracted EMS data from a file or standard input, uses the
    narrative manager to generate a narrative in the specified format, and writes
    the generated narrative to a specified output file or copies it to the clipboard.
    """

    def __init__(self, narrative_manager):
        self.narrative_manager = narrative_manager

    def execute(self, extracted_data_path, output_path="data/narrative.txt"):
        if extracted_data_path == "-":
            extracted_data = sys.stdin.read()
        else:
            with open(extracted_data_path, "r", encoding="utf-8") as file:
                extracted_data = file.read()

        narrative = self.narrative_manager.generate_narrative(
            "presoaped_format", data=extracted_data
        )

        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(narrative)
        else:
            print(narrative)

            pyperclip.copy(narrative)
