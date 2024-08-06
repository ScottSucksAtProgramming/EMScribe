review_prompts = {
    "review_section": {
        "prompt": (
            "Here is a section of data: {section_data}\n"
            "Please make the following changes: {user_input}\n"
            "Do not add any additional details. Use plain text format."
        )
    },
    "final_review": {
        "prompt": (
            "Here is the updated section after making changes: {updated_section}. "
            "If everything is correct, type 'done'. Otherwise, provide further modifications."
        )
    },
}
