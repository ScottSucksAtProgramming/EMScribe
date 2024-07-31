review_prompts = {
    "review_section": (
        "Here is a section of data: {section_data}\n"
        "Please make the following changes: {user_input}"
    ),
    "final_review": (
        "Here is the updated section after making changes: {updated_section}. "
        "If everything is correct, type 'done'. Otherwise, provide further modifications."
    )
}