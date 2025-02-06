# ------------------------------------------------------
# File: string_reversal_index_based.py
# Date: 2025-02-06
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Reverse a string using recursion

def reverse_str(text, index=None):
    """Recursive function to reverse a string using index-based approach."""
    
    # Initialize index to last character if not provided
    if index is None:
        index = len(text) - 1  
    
    # Base case: When index goes below 0, stop recursion
    if index < 0:
        return
    
    # Print current character (executed during stack unwinding)
    print(text[index], end="")  
    
    # Recursive call with the previous index
    reverse_str(text, index - 1)

# Call function with input string
reverse_str("python")