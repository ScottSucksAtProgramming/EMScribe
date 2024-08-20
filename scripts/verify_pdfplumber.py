import pdfplumber


def verify_pdfplumber_installation(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            num_pages = len(pdf.pages)
            print(f"PDF loaded successfully! Number of pages: {num_pages}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'your_pdf_file.pdf' with the path to an actual PDF file for testing.
verify_pdfplumber_installation("data/pdf_2.pdf")
