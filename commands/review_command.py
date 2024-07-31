import os

class ReviewCommand:
    def __init__(self, reviewer):
        self.reviewer = reviewer

    def execute(self, extracted_data_path, output_path):
        with open(extracted_data_path, 'r') as file:
            extracted_data = file.read()

        sections = extracted_data.split('\n\n')
        reviewed_sections = []

        for section in sections:
            while True:
                os.system('clear')  # Clears the screen for a clean prompt
                print(f"Current Section:\n{section}")
                user_input = input("Enter changes or type 'skip' or 's' to move to the next section: ").strip()
                if user_input.lower() in ['skip', 's']:
                    reviewed_sections.append(section)
                    break
                else:
                    response = self.reviewer.review_section(section, user_input)
                    os.system('clear')
                    print(f"\nAI Response:\n{response}")
                    final_response = self.reviewer.final_review(response)
                    print(f"\nFinal AI Response:\n{final_response}")
                    user_input = input("Is this correct? (yes/no): ").strip()
                    if user_input.lower() == 'yes':
                        reviewed_sections.append(final_response)
                        break

        reviewed_data = '\n\n'.join(reviewed_sections)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as file:
            file.write(reviewed_data)
        print(f"\nReviewed data saved to {output_path}")