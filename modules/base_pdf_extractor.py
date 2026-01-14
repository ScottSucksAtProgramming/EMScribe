from abc import ABC, abstractmethod


class BasePDFExtractor(ABC):
    """
    A base class for PDF extractors, providing common methods and structure for
    all specific extractors.

    Attributes:
        pdf_path (str): The path to the PDF file to be processed.
    """

    def __init__(self, pdf_path):
        """
        Initializes the BasePDFExtractor with the path to the PDF.

        Args:
            pdf_path (str): The path to the PDF file.
        """
        self.pdf_path = pdf_path

    @abstractmethod
    def extract(self):
        """
        Abstract method to be implemented by subclasses to extract data from
        the PDF.

        Returns:
            dict: A dictionary containing the extracted information.
        """
        pass

    def detect_and_split_tables(self, df, known_headings):
        """
        Detects where tables should be split based on known table headings.

        Args:
            df (pd.DataFrame): The original DataFrame with multiple tables.
            known_headings (list): A list of known table headings to look for.

        Returns:
            dict: Keys are table headings; values are DataFrames of split
            tables.
        """
        tables = {}
        current_table_start = 0
        current_heading = None

        for i in range(df.shape[1]):
            if df.iloc[0, i] in known_headings:
                if current_heading is not None:
                    tables[current_heading] = df.iloc[:, current_table_start:i].copy()
                current_heading = df.iloc[0, i]
                current_table_start = i

        if current_heading is not None:
            tables[current_heading] = df.iloc[:, current_table_start:].copy()

        return tables
