import os
from typing import Optional
from modules.extract_reviewer import ExtractReviewer


class ReviewCommand:
    """
    Command class to handle the review of extracted data.

    Attributes:
        ExtractReviewer (ExtractReviewer): An instance of ExtractReviewer to review the extracted data.
    """

    def __init__(self, ExtractReviewer: ExtractReviewer):
        """
        Initializes the ReviewCommand with a ExtractReviewer instance.

        Args:
            ExtractReviewer (ExtractReviewer): An instance of ExtractReviewer to review the extracted data.
        """
        self.ExtractReviewer = ExtractReviewer

    def execute(
        self,
        extracted_data_path: str,
        output_path: Optional[str] = "data/reviewed_extract.txt",
    ) -> None:
        """
        Executes the review process on the given extracted data file and saves the output.

        Args:
            extracted_data_path (str): The path to the extracted data file.
            output_path (Optional[str]): The path to save the reviewed data.

        Raises:
            IOError: If there is an error reading or writing the files.
        """
        try:
            with open(extracted_data_path, "r") as file:
                extracted_data = file.read()

            sections = extracted_data.split("\n\n")
            reviewed_sections = []

            for section in sections:
                while True:
                    user_input = self.get_user_input(section)
                    if user_input.lower() in ["skip", "s"]:
                        reviewed_sections.append(section)
                        break
                    else:
                        response = self.ExtractReviewer.review_section(
                            section, user_input
                        )
                        user_input_confirm = self.confirm_response(response)
                        if user_input_confirm in ["yes", "y"]:
                            reviewed_sections.append(response)
                            break

            reviewed_data = "\n\n".join(reviewed_sections)

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as file:
                file.write(reviewed_data)
            print(f"\n\nReviewed data saved to {output_path}")

        except IOError as e:
            raise IOError(f"Error processing files: {e}")

    def get_user_input(self, section: str) -> str:
        """
        Prompts the user for input on the current section.

        Args:
            section (str): The current section of extracted data.

        Returns:
            str: The user's input.
        """
        os.system("clear")
        print("=" * 50)
        print(f"Current Section:\n{section}\n\n")
        print("=" * 50)
        return input(
            "Enter changes or type 'skip' or 's' to move to the next section: "
        ).strip()

    def confirm_response(self, response: str) -> str:
        """
        Prompts the user to confirm the AI response.

        Args:
            response (str): The AI-generated response.

        Returns:
            str: The user's confirmation ('yes' or 'no').
        """
        os.system("clear")
        print("=" * 50)
        print(f"AI Response:\n{response}\n\n")
        print("=" * 50)
        return input("Is this correct? (yes/no): ").strip().lower()
