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
                print("="*50)
                print(f"Current Section:\n\n{section}\n\n")
                print("="*50)
                user_input = input("\nEnter changes or type 'skip' or 's' to move to the next section: ").strip()
                if user_input.lower() in ['skip', 's']:
                    reviewed_sections.append(section)
                    break
                else:
                    response = self.reviewer.review_section(section, user_input)
                    os.system('clear')
                    print("="*50)
                    print(f"Current Section:\n{section}\n")
                    print(f"User Input: {user_input}\n")
                    print(f"AI Response:\n{response}\n")
                    print("="*50)
                    final_response = self.reviewer.final_review(response)
                    print(f"Final AI Response:\n{final_response}\n")
                    print("="*50)
                    user_input = input("\nIs this correct? (yes/no): ").strip()
                    if user_input.lower() == 'yes':
                        reviewed_sections.append(final_response)
                        break

        reviewed_data = '\n\n'.join(reviewed_sections)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as file:
            file.write(reviewed_data)
        print(f"\nReviewed data saved to {output_path}")