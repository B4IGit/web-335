# -*- coding: utf-8 -*-
"""
Author: Devin Ledesma
Date: 06/09/2025
File Name: print_quote.py
Description: This program prints a quote by Oscar Wilde
"""

# Function to print quote
def print_quote():
    # Defines variables for quote and author
    quote = "Experience is the name everyone gives to their mistakes."
    author = "Oscar Wilde"

    # Concatenates quote & author into single sentence
    full_quote = quote + " - " + author

    # Prints the full quote
    print(full_quote)

# Call the function outside of its definition
print_quote()