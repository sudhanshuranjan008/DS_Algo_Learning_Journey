# File: elements_frequency.py
# Date: 2025-02-18
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the frequency of elements in an array

class HashTable:
    def __init__(self, size=10):
        # Initialize hash table with empty lists (chaining)
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Simple hash function: Sum of ASCII values mod table size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        """Inserts a key into the hash table, updating frequency if it already exists"""
        index = self.hash_function(key)  # Get hash index

        # Check if key already exists, update frequency if found
        for kv in self.table[index]:  
            if kv[0] == key:
                kv[1] += 1  # Increment frequency
                return
        
        # If key is new, append it with frequency 1
        self.table[index].append([key, 1])

    def display(self):
        """Displays the frequency table"""
        print("The frequency table is:")
        for bucket in self.table:  # Iterate through each bucket (list)
            for key_value in bucket:  # Iterate through key-value pairs inside bucket
                print(f"Key: {key_value[0]}, Frequency: {key_value[1]}")

if __name__ == "__main__":
    input_list = ["apple", "banana", "apple", "mango", "apple", "mango"]

    ht = HashTable(len(input_list))  # Create a hash table of appropriate size
    for item in input_list:
        ht.insert(item)  # Insert each element into the hash table

    ht.display()  # Display the frequency table

