import pdfplumber
import matplotlib.pyplot as plt
import pandas as pd


def visualize_table_boundaries(pdf_path, page_number):
    """
    Visualizes table boundaries on a given page of the PDF.

    Args:
        pdf_path (str): Path to the PDF file.
        page_number (int): Page number to visualize (0-indexed).

    Returns:
        None
    """
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        im = page.to_image()
        im.debug_tablefinder()  # Highlight detected table boundaries
        im.show()  # Display the image with table boundaries


def extract_tables(pdf_path, page_number):
    """
    Extracts tables from a given page of the PDF and prints them as DataFrames.

    Args:
        pdf_path (str): Path to the PDF file.
        page_number (int): Page number to extract tables from (0-indexed).

    Returns:
        List[pd.DataFrame]: List of DataFrames, each representing a table.
    """
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        tables = page.extract_tables()
        dataframes = [pd.DataFrame(table[1:], columns=table[0]) for table in tables]
        for i, df in enumerate(dataframes):
            print(f"--- Table {i + 1} ---")
            print(df)
        return dataframes


def clean_extracted_table(df):
    """
    Cleans up the extracted table by removing rows with mostly None values and handling specific columns.

    Args:
        df (pd.DataFrame): The extracted table as a DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Drop rows where all values are None
    df_cleaned = df.dropna(how="all")

    # Fill forward or backward for merged cells, if applicable
    df_cleaned = df_cleaned.fillna(method="ffill").fillna(method="bfill")

    # Additional custom cleaning logic here, if needed

    return df_cleaned


def extract_and_clean_tables(pdf_path, page_number):
    """
    Extracts and cleans tables from a given page of the PDF.

    Args:
        pdf_path (str): Path to the PDF file.
        page_number (int): Page number to extract tables from (0-indexed).

    Returns:
        List[pd.DataFrame]: List of cleaned DataFrames, each representing a table.
    """
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        tables = page.extract_tables()
        cleaned_tables = []

        for i, table in enumerate(tables):
            df = pd.DataFrame(table[1:], columns=table[0])
            df_cleaned = clean_extracted_table(df)
            cleaned_tables.append(df_cleaned)
            print(f"--- Cleaned Table {i + 1} ---")
            print(df_cleaned)

        return cleaned_tables


if __name__ == "__main__":
    pdf_path = "data/pdf_2.pdf"  # Update with your actual PDF path
    page_number = 0  # Update with the specific page you want to analyze
    extract_and_clean_tables(pdf_path, page_number)
