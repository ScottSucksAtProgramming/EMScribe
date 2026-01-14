import pdfplumber
import matplotlib.pyplot as plt


def visualize_table_boundaries(pdf_path, page_number, table_settings=None):
    """
    Visualizes table boundaries on a given page of the PDF with customizable table settings.

    Args:
        pdf_path (str): Path to the PDF file.
        page_number (int): Page number to visualize (0-indexed).
        table_settings (dict): Custom settings for table extraction.

    Returns:
        None
    """
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        im = page.to_image()

        # Extract tables with specified settings
        tables = page.find_tables(table_settings=table_settings)

        for i, table in enumerate(tables):
            table_data = table.extract()  # Extract table as a list of lists
            num_rows = len(table_data)
            num_columns = max(len(row) for row in table_data)
            print(
                f"Table {i + 1} found with {num_rows} rows and {num_columns} columns."
            )
            # Print the table data for better insight
            for row in table_data:
                print(row)

        # Visualize the table boundaries
        im.debug_tablefinder()  # Visualize without passing table_settings
        im.show()


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"  # Path to your PDF file
    page_number = 0  # Change this to the specific page you want to visualize

    # Custom table settings to improve detection
    table_settings = {
        "vertical_strategy": "lines",  # Use vertical lines to define columns
        "horizontal_strategy": "words",  # Use horizontal lines to define rows
        "intersection_tolerance": 0,  # Tolerance for intersections to be considered part of a cell
        "snap_tolerance": 3,  # Snap nearby lines to the same position
        "join_tolerance": 5,  # Join line segments that are close together
        "edge_min_length": 50,  # Minimum length of lines to be considered as borders
        "min_words_vertical": 1,  # Minimum words vertically aligned to define a column
        "min_words_horizontal": 1,  # Minimum words horizontally aligned to define a row
    }

    visualize_table_boundaries(pdf_path, page_number, table_settings)
