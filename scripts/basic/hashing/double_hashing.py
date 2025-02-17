# File: double_hashing.py
# Date: 2025-02-17
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement open addressing with double hashing in a hash table

class HashTable:
    def __init__(self, size=11):
        # Initialize hash table with a prime size (default 11)
        # `self.size` stores the size of the hash table, and `self.table` holds the actual data
        self.size = size
        self.table = [None] * self.size  # Create a table with `None` indicating empty slots

    def hash1(self, key):
        # Hash function 1: Converts key to ASCII values and takes modulus with table size
        # Ensures the hash index fits within the table size range
        return sum(ord(char) for char in key) % self.size
    
    def hash2(self, key):
        # Hash function 2: Used for calculating step size in double hashing
        # Takes the sum of ASCII values of the key and ensures the step size is within the table size range
        # The value is subtracted from 7 to generate step size to avoid 0 step
        return 7 - (sum(ord(char) for char in key) % 7)
    
    def insert(self, key, value):
        # Insert a key-value pair into the table
        # `index` is calculated using the first hash function
        # `step` is the probe step size calculated by the second hash function (hash2)
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0  # Initialize the probing step counter

        # While loop for probing: Keep checking the slots based on double hashing with custom step size
        while self.table[(index + i * step) % self.size] is not None:
            new_index = (index + i * step) % self.size  # Calculate the new probe index

            # If key already exists, update the value at the found index
            if self.table[new_index][0] == key:
                self.table[new_index] = (key, value)
                print(f"Updated item: {key}")
                return
            
            # If the slot is marked as deleted (-1, None), insert the new key-value pair here
            if self.table[new_index] == (-1, None):
                self.table[new_index] = (key, value)
                print(f"Inserted into deleted slot: {key}")
                return
            
            i += 1  # Increment the step counter for the next probe
            if i == self.size:  # If we've probed all slots and still haven't inserted, table is full
                print("Hash Table is full!")
                return
            
        # If an empty slot is found after probing, insert the key-value pair
        new_index = (index + i * step) % self.size
        self.table[new_index] = (key, value)

    def get(self, key):
        # Retrieve the value associated with a key
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0  # Initialize the probing step counter

        # While loop for probing: Keep checking the slots until the key is found or table is exhausted
        while self.table[(index + i * step) % self.size] is not None:
            new_index = (index + i * step) % self.size  # Calculate the probe index
            if self.table[new_index][0] == key:  # If the key matches, return the associated value
                return self.table[new_index][1]
            
            i += 1  # Increment the step counter for the next probe
            if i == self.size:  # If we've probed all slots and the key is still not found, stop
                break

        print(f"Key '{key}' not found!")  # If the key isn't found, return None
        return None
    
    def remove(self, key):
        # Remove a key-value pair from the table
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0  # Initialize the probing step counter

        # While loop for probing: Keep checking the slots until the key is found or table is exhausted
        while self.table[(index + i * step) % self.size] is not None:
            new_index = (index + i * step) % self.size  # Calculate the probe index
            if self.table[new_index][0] == key:  # If the key matches, mark it as deleted
                self.table[new_index] = (-1, None)  # Mark as deleted with (-1, None) placeholder
                print(f"Removed item: {key}")
                return
            
            i += 1  # Increment the step counter for the next probe
            if i == self.size:  # If we've probed all slots and didn't find the key, stop
                break

        print("Key not found")  # If the key isn't found, print the message

    def display(self):
        # Display the entire hash table with the current contents of each slot
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Main block to test the hash table
if __name__ == "__main__":
    ht = HashTable()

    fruits = ["apple", "banana", "kiwi", "papaya", "berry", "mango", "grapes", "orange", "pear", "coconut", "pineapple"]
    for i in range(len(fruits)):
        ht.insert(fruits[i], i**2)  # Insert fruits and square of their index as value

    ht.display()  # Display the hash table after all insertions

    # Insert some additional items
    ht.insert("watermelon", 100)
    ht.insert("apple", 121)  # Update existing "apple" with new value
    ht.display()

    # Remove an item ("grapes")
    ht.remove("grapes")
    ht.display()

    # Insert watermelon again, which should go into the available slot after "grapes" is removed
    ht.insert("watermelon", 67)
    ht.display()

    # Retrieve the value of a non-existent key ("muskmelon")
    ht.get("muskmelon")

