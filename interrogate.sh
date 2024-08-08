#!/bin/bash

# Ensure the Python script is executable
chmod +x utils/pdf_interrogator.py

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 --tables <pdf_file>"
    exit 1
fi

# Run the Python script with provided arguments
python utils/pdf_interrogator.py "$1" "$2"