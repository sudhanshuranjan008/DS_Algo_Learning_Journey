# File: quadratic_probing.py
# Date: 2025-02-17
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement open addressing with quadratic probing in a hash table

class HashTable:
    def __init__(self, size=11):
        # Initialize hash table with the specified size, default is 11 (prime number for better distribution)
        self.size = size
        self.table = [None] * self.size  # Create a list of None, representing empty slots

    def hash_function(self, key):
        # Simple hash function: sum of ASCII values of the characters in the key, modded by table size
        return sum(ord(char) for char in key) % self.size
    
    def insert(self, key, value):
        # Insert the key-value pair into the hash table
        index = self.hash_function(key)  # Compute hash index using hash function
        i = 0  # Probing step counter (for quadratic probing)
        attempts = 0  # Count of probing attempts

        # While loop for probing: Keep checking the slots until we find an empty one or the key exists
        while self.table[(index + i**2) % self.size] is not None:
            new_index = (index + i**2) % self.size  # Quadratic probing calculation

            # If the key already exists, update the value
            if self.table[new_index][0] == key:
                self.table[new_index] = (key, value)  # Update the value for the existing key
                print(f"Updated item: {key}")
                return

            # If we find a deleted slot (-1, None), insert the new key-value pair there
            if self.table[new_index] == (-1, None):
                self.table[new_index] = (key, value)  # Insert in the deleted slot
                print(f"Inserted into deleted slot: {key}")
                return

            i += 1  # Increment probing step for the next iteration
            attempts += 1  # Track how many attempts were made
            if attempts == self.size:  # If we've checked all slots and couldn't find an empty one, the table is full
                print("Hash Table is Full!")
                return

        # If an empty slot is found, insert the key-value pair
        new_index = (index + i**2) % self.size  # Recalculate the new index to insert at
        self.table[new_index] = (key, value)

    def remove(self, key):
        # Remove the key-value pair from the hash table
        index = self.hash_function(key)  # Compute hash index using hash function
        i = 0  # Probing step counter

        # While loop for probing: Keep checking the slots until we find the key or an empty slot
        while self.table[(index + i**2) % self.size] is not None:
            new_index = (index + i**2) % self.size  # Quadratic probing calculation
            if self.table[new_index][0] == key:  # If the key is found, remove it
                self.table[new_index] = (-1, None)  # Mark slot as deleted with a placeholder (-1, None)
                print(f"Removed item: {key}")
                return
            
            i += 1  # Increment probing step for the next iteration
            if i == self.size:  # If we've checked all slots and didn't find the key
                break

        print("Key not found!")  # If key wasn't found after probing all slots

    def display(self):
        # Display the entire hash table with index and values
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Main block to test the hash table
if __name__ == "__main__":
    ht = HashTable()

    fruits = ["apple", "banana", "kiwi", "papaya", "berry", "mango", "grapes", "orange", "pear", "coconut"]
    for i in range(len(fruits)):
        ht.insert(fruits[i], i**2)  # Insert fruit names with their square index value

    ht.display()  # Display the hash table after all insertions

    # Insert some additional items
    ht.insert("watermelon", 100)
    ht.insert("apple", 121)  # Update existing "apple" with new value
    ht.display()

    # Remove an item ("grapes")
    ht.remove("grapes")
    ht.display()

    # Insert watermelon again, it will update the value
    ht.insert("watermelon", 67)
    ht.display()



