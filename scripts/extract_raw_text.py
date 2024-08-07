import pdfplumber


def extract_raw_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text + "\n"
    return text


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python extract_raw_text.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    raw_text = extract_raw_text_from_pdf(pdf_path)
    print(raw_text)
