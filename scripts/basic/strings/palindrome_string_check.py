# ------------------------------------------------------
# File: palindrome_string_check.py
# Date: 2025-01-13
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check if a string is a palindrome

def palindrome_check(my_string: str) -> bool:
    """
    Check if the given string is a palindrome.
    Compare characters symmetrically from start and end.
    """
    N = len(my_string)

    # Compare characters from the start and end, moving toward the middle
    for i in range(N // 2):  # Iterate up to the middle of the string
        if my_string[i] != my_string[N - i - 1]:  # Compare start and end characters
            return False  # Return early if a mismatch is found

    return True  # If no mismatches, the string is a palindrome


if __name__ == "__main__":
    # Input string for testing
    input_string = "madam"

    # Output based on the result of the function
    if palindrome_check(input_string):
        print(f"{input_string} is a palindrome.")
    else:
        print(f"{input_string} is not a palindrome.")
