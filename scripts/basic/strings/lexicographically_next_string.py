# ------------------------------------------------------
# File: lexicographically_next_string.py
# Date: 2025-01-17
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find lexicographically next string for a given string

def lexi_next_word(my_string: str):
    # Special case: If the input is an empty string, return 'a'
    if my_string == " ":
        return 'a'

    # Convert the string into a list of characters to handle immutability
    char_list = list(my_string)
    N = len(char_list) - 1  # Start from the last character

    # Traverse the string from the end to find the first character that is not 'z'
    while N >= 0 and char_list[N] == 'z':
        char_list[N] = 'a'  # Reset 'z' to 'a'
        N -= 1  # Move to the previous character

    # If N is -1, it means all characters were 'z'
    if N == -1:
        char_list.insert(0, 'a')  # Prepend 'a' to the string (e.g., 'zzz' -> 'aaaa')
    else:
        # Increment the first non-'z' character
        char_list[N] = chr(ord(char_list[N]) + 1)

    # Convert the list of characters back into a string
    return ''.join(char_list)

if __name__ == "__main__":
    # Test input string
    input_string = "python"
    
    # Print the original string
    print(f"Original string: {input_string}")
    
    # Print the lexicographically next string
    print(f"Lexicographically next string: {lexi_next_word(input_string)}")

