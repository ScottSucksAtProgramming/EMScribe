class Refiner:
    """
    A class to refine the extracted information before generating a narrative.
    
    Attributes:
        extracted_data (dict): The extracted data to be refined.
    """

    def __init__(self, extracted_data: dict):
        """
        Initializes the Refiner with the extracted data.

        Args:
            extracted_data (dict): The extracted data to be refined.
        """
        self.extracted_data = extracted_data

    def review_data(self):
        """
        Reviews the extracted data and allows the user to make modifications.

        Returns:
            dict: The refined data.
        """
        # Display the extracted data to the user
        print("Extracted Information:")
        for key, value in self.extracted_data.items():
            print(f"{key}: {value}")
        
        # Allow the user to make modifications
        refined_data = self.extracted_data.copy()
        for key in self.extracted_data.keys():
            new_value = input(f"Enter updated value for {key} (leave blank to keep current value): ")
            if new_value:
                refined_data[key] = new_value
        
        return refined_data
