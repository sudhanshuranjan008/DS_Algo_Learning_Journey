# ------------------------------------------------------
# File: longest_unique_substring.py
# Date: 2025-02-20
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the longest substring without repeating characters using hashing

class HashTable:
    def  __init__(self, size=11):
        # Initialize hash table with empty slots
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        """Generate an index using modulus-based hashing."""
        return ord(key) % self.size
    
    def insert(self, key, value):
        """Insert key-value pair using linear probing for collision handling."""
        index = self.hash_function(key)
        original_index = index

        # Probe until an empty slot is found
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)  # Update existing key's value
                return True
            
            index = (index + 1) % self.size  # Move to the next slot
            if index == original_index:
                return False  # Table is full

        # Insert new key-value pair
        self.table[index] = (key, value)
        return True
    
    def get(self, key):
        """Retrieve value for a given key using linear probing."""
        index = self.hash_function(key)
        original_index = index

        # Search for key using linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Return stored index
            
            index = (index + 1) % self.size  # Move to next slot
            if index == original_index:
                break  # Stop if we have looped back to the original position

        return None  # Key not found


def longest_substring(string):
    """Find the longest substring without repeating characters."""
    ht = HashTable()
    left = 0  # Left boundary of the current valid window
    max_length = 0  # Track the longest valid substring length
    longest_start = 0  # Start index of the longest substring found

    for right in range(len(string)):
        prev_index = ht.get(string[right])  # Get last seen index of current char

        if prev_index is not None and prev_index >= left:
            left = prev_index + 1  # Move left past the previous occurrence

        ht.insert(string[right], right)  # Store the latest index of the character

        # Update longest substring details if current window is larger
        if right - left + 1 > max_length:
            max_length = right - left + 1
            longest_start = left
        
    return string[longest_start: longest_start + max_length]  # Extract substring

# Driver code for testing
if __name__ == "__main__":
    input_string = "success"
    result = longest_substring(input_string)
    print(result)  # Expected Output: "suc"
