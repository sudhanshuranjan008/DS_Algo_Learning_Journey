# File: first_repeating_element.py
# Date: 2025-02-19
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the first repeating element in an array using hashing

class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with None (empty slots)
        self.size = size
        self.table = [None] * self.size  

    def hash_function(self, key):
        """Generate an index using a simple hash function based on ASCII values."""
        return sum(ord(char) for char in str(key)) % self.size  # Handles large numbers & strings

    def insert(self, key):
        """Insert key using linear probing. If key exists, return True (first repeat)."""
        index = self.hash_function(key)  # Compute initial index
        original_index = index  # Store original index to detect full loop

        # Probe until an empty slot is found
        while self.table[index] is not None:
            if self.table[index] == key:
                return True  # Key already exists (first repeat found)
            
            index = (index + 1) % self.size  # Move to next slot (linear probing)

            # Stop if we loop back to the starting position (table is full)
            if index == original_index:
                return False  

        # Insert key in the available slot
        self.table[index] = key
        return False  # Key inserted for the first time


if __name__ == "__main__":
    num = ["apple", "banana", "mango", "apple", "grape", "banana"]

    ht = HashTable(len(num))  # Create hash table of appropriate size
    el = None  # Store the first repeating element

    # Iterate through the list and check for first repeat
    for item in num:
        if ht.insert(item):  # If insert returns True, first repeat found
            el = item
            break  

    # Print the result
    if el is not None:
        print(f"The first repeating element is: {el}")
    else:
        print("No repeating elements found.")


