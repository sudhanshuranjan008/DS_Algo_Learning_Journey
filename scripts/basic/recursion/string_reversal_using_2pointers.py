# ------------------------------------------------------
# File: string_reversal_using_2pointers.py
# Date: 2025-02-06
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Reverse a string using recursion

def reverse_str(text, left=0, right=None):
    """Recursive function to reverse a string using two-pointer swapping."""
    
    # Initialize right pointer to last character if not provided
    if right is None:
        right = len(text) - 1  
    
    # Base case: when pointers meet or cross, return the reversed string
    if left >= right:
        return "".join(text)  
    
    # Swap characters at left and right pointers
    text[left], text[right] = text[right], text[left]  
    
    # Recursive call, moving pointers inward
    return reverse_str(text, left + 1, right - 1)

# Convert string to list (since strings are immutable)
text = list("python")  

# Call function and print reversed string
print("".join(reverse_str(text)))