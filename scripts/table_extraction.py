import pdfplumber
import pandas as pd


def extract_raw_tables(pdf_path, page_number):
    """
    Extracts tables from a given page of the PDF without any modifications.

    Args:
        pdf_path (str): Path to the PDF file.
        page_number (int): Page number to extract tables from (0-indexed).

    Returns:
        List[pd.DataFrame]: List of DataFrames, each representing a table.
    """
    # Set pandas display options to avoid truncation
    pd.set_option("display.max_columns", None)
    pd.set_option("display.expand_frame_repr", False)

    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        tables = page.extract_tables()
        dataframes = [pd.DataFrame(table) for table in tables]
        for i, df in enumerate(dataframes):
            print(f"--- Raw Table {i + 1} ---")
            print(df)
        return dataframes


def extract_advance_directives(pdf_path, page_number):
    """
    Extracts the 'Advance Directives' information from the first table of the PDF page.

    Args:
        pdf_path (str): Path to the PDF file.
        page_number (int): Page number to extract information from (0-indexed).

    Returns:
        str: The extracted 'Advance Directives' information, with newlines replaced by spaces.
    """
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        tables = page.extract_tables()

        # Assuming you want to extract from the first table (index 0)
        if tables:
            df = pd.DataFrame(tables[0])

            # Find the row where "Advance Directives" is mentioned
            advance_directives_row = df[df[0] == "Advance Directives"]

            # Extract the relevant information from that row
            if not advance_directives_row.empty:
                advance_directives_info = advance_directives_row.iloc[
                    0, 2
                ]  # Assuming the info is in the third column
                # Replace newline characters with a space
                return advance_directives_info.replace("\n", " ")
            else:
                return "Advance Directives not found."


def display_full_table(pdf_path, page_number):
    """
    Extracts and displays the entire table from the specified page of the PDF without any truncation.

    Args:
        pdf_path (str): Path to the PDF file.
        page_number (int): Page number to extract the table from (0-indexed).
    """
    # Set pandas display options to ensure all data is shown
    pd.set_option("display.max_columns", None)  # Show all columns
    pd.set_option("display.max_rows", None)  # Show all rows
    pd.set_option("display.max_colwidth", None)  # Show full content in each cell
    pd.set_option(
        "display.expand_frame_repr", False
    )  # Prevent DataFrame from being split across multiple lines

    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        tables = page.extract_tables()

        for i, table in enumerate(tables):
            df = pd.DataFrame(table)
            print(f"--- Table {i + 1} ---")
            print(df)


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"  # Path to your PDF file
    page_number = 0  # Specific page you want to analyze
    display_full_table(pdf_path, page_number)
