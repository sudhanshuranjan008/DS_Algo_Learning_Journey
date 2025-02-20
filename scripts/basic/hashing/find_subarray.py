# File: find_subarray.py
# Date: 2025-02-20
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the subarray with the given sum using hashing

class HashTable:
    def __init__(self, size=11):
        # Initialize the hash table with empty slots (None)
        self.size = size
        self.table = [None] * self.size  

    def hash_function(self, key):
        """Generate an index using a simple modulus-based hash function."""
        return key % self.size  

    def insert(self, key, value):
        """Insert key-value pair (prefix_sum → index) using linear probing."""
        index = self.hash_function(key)  # Compute initial index
        original_index = index  # Store original index to detect full loop

        # Find an empty slot using linear probing
        while self.table[index] is not None:
            index = (index + 1) % self.size  # Move to next slot
            
            # If we loop back to the starting index, table is full
            if index == original_index:
                return False  # Resizing should be handled if needed

        # Insert the key-value pair
        self.table[index] = (key, value)
        return True
        

    def get(self, key):
        """Retrieve the index for a given prefix_sum using linear probing."""
        index = self.hash_function(key)  # Compute hash index
        original_index = index  # Store original index to detect full loop

        # Search using linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Return stored index
            
            index = (index + 1) % self.size  # Move to next slot  

            # Stop if we loop back to the start
            if index == original_index:
                break

        return None  # Key not found


def subarray_with_sum(arr, target_sum):
    """Find the first subarray with the given sum using hashing."""
    ht = HashTable()  # Create hash table
    prefix_sum = 0  # Initialize prefix sum

    for i, num in enumerate(arr):
        prefix_sum += num  # Compute prefix sum

        # If prefix_sum itself matches target_sum, subarray starts from index 0
        if prefix_sum == target_sum:
            return (0, i)

        # Check if (prefix_sum - target_sum) exists in hash table
        start_index = ht.get(prefix_sum - target_sum)
        if start_index is not None:
            return (start_index + 1, i)  # Extract subarray indices

        # Store prefix_sum and its index in hash table
        ht.insert(prefix_sum, i)

    return None  # No subarray found

# Test the code
if __name__ == "__main__":
    arr = [1, 21, 4, 7, 5, 5, 6, 2]
    target_sum = 16

    result = subarray_with_sum(arr, target_sum)

    if result:
        print(f"Subarray with sum {target_sum} found at index {result[0]} to {result[1]}")
    else:
        print("No subarray with the given sum found.")


