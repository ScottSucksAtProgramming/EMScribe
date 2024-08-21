from modules.pdf_extractor_factory import PDFExtractorFactory


def test_pdf_extraction(pdf_path):
    try:
        extractor = PDFExtractorFactory.get_extractor(pdf_path)
        extracted_information = extractor.extract()

        # Print the extracted information for verification
        for heading, info in extracted_information.items():
            print(f"{heading}:")
            for key, value in info.items():
                print(f"  {key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Path to the PDF you want to test
    pdf_path = "data/demo_imagetrend.pdf"
    test_pdf_extraction(pdf_path)
