# ------------------------------------------------------
# File: anagrams_check.py
# Date: 2025-01-14
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check if two strings are anagrams

# Function to check if two strings are anagrams
def anagram_check(string1: str, string2: str):
    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Count characters in the first string (string1)
    for char in string1:
        # For each character, increment the count in the dictionary
        # If character doesn't exist, the get() method will return 0 and then add 1
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract character counts based on the second string (string2)
    for char in string2:
        # Decrease the count for each character found in string2
        char_count[char] = char_count.get(char, 0) - 1

    # Check if all character counts are 0, meaning both strings have the same characters in the same frequency
    for value in char_count.values():
        if value != 0:
            # If any character has a non-zero count, return False
            return False
    
    # If all counts are 0, the strings are anagrams
    return True

# Driver code
if __name__ == "__main__":
    s1 = 'listen'  # First string
    s2 = 'silent'  # Second string

    # Check if the strings are anagrams and print the result
    if anagram_check(s1, s2):
        print(f"{s1} and {s2} are anagrams.")
    else:
        print(f"{s1} and {s2} are not anagrams.")
