import pdfplumber
import re


def extract_category(text, start_keyword, stop_keywords):
    # Regex pattern to match from the start_keyword to any of the stop_keywords
    stop_pattern = "|".join(re.escape(kw) for kw in stop_keywords)
    pattern = re.compile(
        rf"{re.escape(start_keyword)}.*?(?={stop_pattern}|$)", re.DOTALL
    )

    match = pattern.search(text)
    if match:
        return match.group(0).strip()
    return ""


def extract_all_assessments(text):
    categories = [
        "Mental Status",
        "Skin",
        "HEENT",
        "Face",
        "Eyes",
        "Neck",
        "Chest",
        "Abdomen",
        "Back",
        "Pelvis/GU/GI",
        "Extremities",
        "Neurological",
        "Neonatal",
    ]
    stop_keywords = categories + [
        "Hospital Chart Number",
        "Page",
        "Template Version",
        "Data Version",
    ]

    assessments_data = []

    for i, category in enumerate(categories):
        subtext = extract_category(text, category, stop_keywords[i + 1 :])
        if subtext:
            assessments_data.append(subtext)

    return assessments_data


def extract_and_combine_assessments_text_based(pdf_path):
    combined_assessments_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number in range(len(pdf.pages)):
            page = pdf.pages[page_number]
            text = page.extract_text()

            assessments_data = extract_all_assessments(text)
            combined_assessments_data.extend(assessments_data)

    return combined_assessments_data


# Example usage
pdf_path = "data/pdf_2.pdf"
assessments_text = extract_and_combine_assessments_text_based(pdf_path)

# Print each captured line
print("Extracted Assessment Data by Category:")
for line in assessments_text:
    print(line)
