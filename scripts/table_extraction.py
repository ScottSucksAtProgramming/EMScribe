import pdfplumber
import pandas as pd


def extract_raw_tables_from_all_pages(pdf_path):
    """
    Extracts tables from all pages of the PDF without any modifications.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        dict: A dictionary where the keys are page numbers and the values are lists of DataFrames, each representing a table.
    """
    # Set pandas display options to avoid truncation
    pd.set_option("display.max_columns", None)
    pd.set_option("display.expand_frame_repr", False)

    all_tables = {}

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            dataframes = [pd.DataFrame(table) for table in tables]
            all_tables[page_number] = dataframes
            for i, df in enumerate(dataframes):
                print(f"--- Page {page_number + 1} - Raw Table {i + 1} ---")
                print(df)

    return all_tables


def extract_advance_directives(pdf_path):
    """
    Extracts the 'Advance Directives' information from the first table of each page of the PDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        dict: A dictionary with page numbers as keys and the 'Advance Directives' information as values.
    """
    advance_directives_info = {}

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            tables = page.extract_tables()

            # Assuming you want to extract from the first table (index 0)
            if tables:
                df = pd.DataFrame(tables[0])

                # Find the row where "Advance Directives" is mentioned
                advance_directives_row = df[df[0] == "Advance Directives"]

                # Extract the relevant information from that row
                if not advance_directives_row.empty:
                    info = advance_directives_row.iloc[
                        0, 2
                    ]  # Assuming the info is in the third column
                    # Replace newline characters with a space
                    advance_directives_info[page_number] = info.replace("\n", " ")
                else:
                    advance_directives_info[page_number] = (
                        "Advance Directives not found."
                    )

    return advance_directives_info


def display_full_table_from_all_pages(pdf_path):
    """
    Extracts and displays all tables from all pages of the PDF without any truncation.

    Args:
        pdf_path (str): Path to the PDF file.
    """
    # Set pandas display options to ensure all data is shown
    pd.set_option("display.max_columns", None)  # Show all columns
    pd.set_option("display.max_rows", None)  # Show all rows
    pd.set_option("display.max_colwidth", None)  # Show full content in each cell
    pd.set_option(
        "display.expand_frame_repr", False
    )  # Prevent DataFrame from being split across multiple lines

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            tables = page.extract_tables()

            for i, table in enumerate(tables):
                df = pd.DataFrame(table)
                print(f"--- Page {page_number + 1} - Table {i + 1} ---")
                print(df)


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"  # Path to your PDF file

    # Example: Extract and display all tables from all pages
    display_full_table_from_all_pages(pdf_path)

    # Example: Extract raw tables from all pages
    all_tables = extract_raw_tables_from_all_pages(pdf_path)

    # Example: Extract 'Advance Directives' from all pages
    advance_directives_info = extract_advance_directives(pdf_path)
    print("\nAdvance Directives Information:")
    for page, info in advance_directives_info.items():
        print(f"Page {page + 1}: {info}")
