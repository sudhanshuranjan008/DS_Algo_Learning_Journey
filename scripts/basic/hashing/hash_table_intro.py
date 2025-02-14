# File: hash_table_intro.py
# Date: 2025-02-14
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a basic hash table (with collision handling via chaining)

class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with empty lists (for chaining)
        self.size = size
        self.table = [[] for _ in range(self.size)]  # List of lists to handle collisions via chaining

    # Hash function to compute index from key
    def hash_function(self, key):
        # Sum the ASCII values of the characters in the key
        sum_of_chars = sum(ord(char) for char in key)
        # Use modulo to ensure the index is within the table size
        return sum_of_chars % self.size

    # Insert a key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)  # Find the index using the hash function
        # Check if key already exists at the computed index (to update the value)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                self.table[index][i] = (key, value)  # Update the existing key-value pair
                return
        # If the key doesn't exist, append the new key-value pair
        self.table[index].append((key, value))

    # Retrieve the value for a given key
    def get(self, key):
        index = self.hash_function(key)  # Get the index using the hash function
        # Search the list at the computed index
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]  # Return the value if the key is found
        return None  # If the key is not found, return None

    # Remove a key-value pair from the table
    def remove(self, key):
        index = self.hash_function(key)  # Find the index using the hash function
        # Search the list at the computed index for the key
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]  # Remove the key-value pair
                return
        print("Key not found!")  # Print message if the key is not found

    # Print the hash table (for debugging)
    def display(self):
        # Print the index and its associated key-value pairs
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Example Usage
ht = HashTable()

# Insert some key-value pairs
ht.insert("apple", 5)
ht.insert("banana", 3)
ht.insert("orange", 8)
ht.insert("papaya", 10)
ht.insert("mango", 19)

# Display the hash table
ht.display()

# Retrieve the value for the key 'mango'
print(f"mango: {ht.get('mango')}")

# Remove a non-existent key ('kiwi')
ht.remove("kiwi")

# Remove an existing key ('apple')
ht.remove("apple")

# Display the hash table after removal
ht.display()
