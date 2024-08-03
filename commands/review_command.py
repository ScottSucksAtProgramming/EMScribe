# -*- coding: utf-8 -*-
import os


class ReviewCommand:
    """
    Command to review and edit extracted EMS data sections interactively.

    This command reads extracted EMS data from a file, presents each section to the user
    for review, allows the user to make changes, and uses the reviewer to validate these
    changes. The validated sections are then saved to a specified output file.

    Attributes:
        reviewer: An object with a `review_section` method that processes and validates
                  user changes to each section of the extracted data.
    """

    def __init__(self, reviewer):
        """
        Initialize the ReviewCommand with a reviewer.

        Args:
            reviewer: An object with a `review_section` method for validating changes.
        """
        self.reviewer = reviewer

    def execute(self, extracted_data_path, output_path="data/reviewed_extract.txt"):
        """
        Execute the review command.

        Reads the extracted EMS data from the given path, allows the user to review and edit
        each section, validates the changes using the reviewer, and saves the validated sections
        to the output path.

        Args:
            extracted_data_path (str): Path to the file containing extracted EMS data.
            output_path (str): Path to save the reviewed and validated data. Default is
            "data/reviewed_extract.txt".
        """
        with open(extracted_data_path, "r", encoding="utf-8") as file:
            extracted_data = file.read()

        sections = extracted_data.split("\n\n")
        reviewed_sections = []

        for section in sections:
            while True:
                os.system("clear")  # Clears the screen for a clean prompt
                print("=" * 50)
                print(f"Current Section:\n{section}\n\n")
                print("=" * 50)
                user_input = input(
                    "Enter changes or type 'skip' or 's' to move to the next section: "
                ).strip()
                if user_input.lower() in ["skip", "s"]:
                    reviewed_sections.append(section)
                    break
                response = self.reviewer.review_section(section, user_input)
                os.system("clear")
                print("=" * 50)
                print(f"AI Response:\n{response}\n\n")
                print("=" * 50)
                user_input_confirm = (
                    input("Is this correct? (yes/no): ").strip().lower()
                )
                if user_input_confirm in ["yes", "y"]:
                    reviewed_sections.append(response)
                    break

        reviewed_data = "\n\n".join(reviewed_sections)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(reviewed_data)
        print(f"\n\nReviewed data saved to {output_path}")
