# ------------------------------------------------------
# File: first_non_repeating_char.py
# Date: 2025-01-14
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the first non-repeating character in a string

def first_non_repeating_char(my_string: str):
    # Create a dictionary to store the frequency of each character
    char_count = {}
    for char in my_string:
        # Update the frequency of the current character
        # If the character is not in the dictionary, initialize its count to 0, then increment it
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through the string again to find the first non-repeating character
    for char in my_string:
        # Check if the current character has a frequency of 1
        if char_count[char] == 1:
            return char  # Return the first non-repeating character

    # If no non-repeating character is found, return a default message
    return "No non-repeating character found"


if __name__ == "__main__":
    # Input string to find the first non-repeating character
    input_string = 'studystring'
    # Print the result
    print(first_non_repeating_char(input_string))
