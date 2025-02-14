# File: string_hashing.py
# Date: 2025-02-14
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Hash a simple string and display the resulting index

# The hash function calculates the hash index based on the sum of ASCII values of characters in the string
def hash_function(key):
    hash_value = 0  # Start with 0 as the initial hash value
    for char in key:  # Iterate through each character in the string
        hash_value += ord(char)  # Add the ASCII value of the character to hash_value
    return hash_value % 10  # Return the index by applying modulo to fit within a table of size 10

# Example string to hash
string = "banana"

# Get the hash index for the string
index = hash_function(string)

# Output the result: Displays the index computed by the hash function
print(f"The hash index for '{string}' is {index}")

