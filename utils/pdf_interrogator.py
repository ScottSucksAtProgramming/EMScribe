#!/usr/bin/env python3
import argparse
import pandas as pd
import tabula


def extract_tables_from_pdf(pdf_path):
    """
    Extracts and returns tables from the specified PDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Formatted string of extracted tables.
    """
    df_list = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)
    output = []

    if isinstance(df_list, list) and len(df_list) > 0:
        for i, df in enumerate(df_list):
            df = df.applymap(str)  # Ensure all data is string type
            df.fillna("", inplace=True)
            output.append(f"Table {i + 1}:\n")
            output.append(df.to_string(index=False))
            output.append("\n")
    else:
        output.append("No tables found in the PDF.")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Interrogate PDF files to extract tables."
    )
    parser.add_argument(
        "--tables", type=str, help="Path to the PDF file to extract tables from."
    )
    args = parser.parse_args()

    if args.tables:
        result = extract_tables_from_pdf(args.tables)
        with open("tables.txt", "w") as file:
            file.write(result)
        print(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
