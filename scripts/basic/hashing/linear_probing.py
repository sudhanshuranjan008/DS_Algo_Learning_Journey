# File: linear_probing.py
# Date: 2025-02-16
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement open addressing with linear probing in a hash table

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size  # Initialize hash table with None (empty slots)

    # Hash function to compute index from key
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size  # Simple hash function

    # Insert a key-value pair into the hash table (with update if key exists)
    def insert(self, key, value):
        index = self.hash_function(key)  # Compute hash index
        original_index = index  # Store original index to detect full table

        # Search for existing key or an empty slot using linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:  # If key already exists, update value
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size  # Move to the next slot
            if index == original_index:  # If table is full, exit
                print("Hash Table is Full!")
                return

        # If key not found, insert it in the first empty slot
        self.table[index] = (key, value)

    # Remove a key-value pair from the hash table (with placeholder for deleted slots)
    def remove(self, key):
        index = self.hash_function(key)  # Compute hash index
        original_index = index  # Store original index to detect loop

        # Search for the key using linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Key found
                self.table[index] = (-1, None)  # Mark slot as deleted (-1 as placeholder)
                return
            index = (index + 1) % self.size  # Move to next slot
            if index == original_index:  # If we loop back, key not found
                break

        print("Key not found!")  # If key is not found, print message

    # Display the hash table
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Example Usage
if __name__ == "__main__":
    ht = HashTable()

    # Insert key-value pairs
    ht.insert("apple", 5)
    ht.insert("banana", 3)
    ht.insert("orange", 8)
    ht.insert("papaya", 10)
    ht.insert("mango", 19)

    # Display the hash table
    ht.display()

    # Update value for an existing key
    ht.insert("apple", 15)

    # Display after updating "apple"
    print("\nAfter updating 'apple':")
    ht.display()

    # Remove a key-value pair
    ht.remove("apple")

    # Display after deletion
    print("\nAfter removing 'apple':")
    ht.display()

