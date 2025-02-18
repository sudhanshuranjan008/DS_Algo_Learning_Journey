# File: dynamic_hash_table.py
# Date: 2025-02-18
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Hash Table implementation with double hashing and dynamic resizing

class HashTable:
    def __init__(self, size=11):
        # Initialize hash table with given size (default is 11)
        self.size = size
        self.table = [None] * self.size  # Create an empty table
        self.count = 0  # Track number of elements in the table

    def hash1(self, key):
        # Primary hash function: Sum of ASCII values mod table size
        return sum(ord(char) for char in key) % self.size
    
    def hash2(self, key):
        # Secondary hash function for probing: Ensures non-zero step size
        return 7 - (sum(ord(char) for char in key) % 7)
    
    def insert(self, key, value):
        # Resize if load factor exceeds 0.7
        if self.count / self.size >= 0.7:
            self.resize()
        
        index = self.hash1(key)  # Compute initial index
        step = self.hash2(key)   # Compute step size for probing
        k = 0  # Probe counter

        # Search for an empty slot using double hashing
        while self.table[(index + k * step) % self.size] is not None:
            new_index = (index + k * step) % self.size  # Compute new index

            if self.table[new_index][0] == key:
                # Key already exists, update value
                self.table[new_index] = (key, value)
                print(f"Updated item: {key}")
                return
            
            if self.table[new_index] == (-1, None):
                # Insert into previously deleted slot
                self.table[new_index] = (key, value)
                print(f"Inserted into deleted slot: {key}")
                return
            
            k += 1
            if k == self.size:
                # If all slots checked and no empty slot found
                print("Hash table is full!")
                return
            
        # Insert into the first empty slot found
        new_index = (index + k * step) % self.size
        self.table[new_index] = (key, value)
        self.count += 1  # Increment count after successful insertion

    def get(self, key):
        # Retrieve value for a given key
        index = self.hash1(key)  # Compute initial index
        step = self.hash2(key)   # Compute step size
        k = 0  # Probe counter

        # Search for key using double hashing
        while self.table[(index + k * step) % self.size] is not None:
            new_index = (index + k * step) % self.size

            if self.table[new_index][0] == key:
                return self.table[new_index][1]  # Return value if key found
            
            k += 1
            if k == self.size:
                break  # Stop searching if table is fully probed
        
        print(f"Key '{key}' not found!")
        return None  # Return None if key is not found

    def remove(self, key):
        # Remove key-value pair from the table
        index = self.hash1(key)  # Compute initial index
        step = self.hash2(key)   # Compute step size
        k = 0  # Probe counter

        # Search for key using double hashing
        while self.table[(index + k * step) % self.size] is not None:
            new_index = (index + k * step) % self.size

            if self.table[new_index][0] == key:
                # Mark the slot as deleted
                self.table[new_index] = (-1, None)
                self.count -= 1  # Decrement count
                print(f"Removed item: {key}")

                # Resize if load factor drops below 0.2
                if self.count / self.size < 0.2:
                    self.resize(shrink=True)
                return
            
            k += 1
            if k == self.size:
                break  # Stop searching if table is fully probed

        print("Key not found!")

    def resize(self, shrink=False):
        # Resize the hash table dynamically
        old_table = self.table  # Store old table
        
        if shrink:
            new_size = max(11, self.size // 2)  # Ensure table size never goes below 11
        else:
            new_size = self.next_prime(2 * self.size)  # Expand to next prime number

        self.size = new_size
        self.table = [None] * self.size  # Create new empty table
        self.count = 0  # Reset count

        # Reinsert all existing (non-deleted) elements
        for item in old_table:
            if item is not None and item != (-1, None):
                self.insert(item[0], item[1])

        print(f"Hash table {'shrunk' if shrink else 'expanded'} to {self.size}")

    def next_prime(self, n):
        # Find next prime number greater than or equal to n
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        while not is_prime(n):
            n += 1

        return n

    def display(self):
        # Display the current state of the hash table
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Test the hash table implementation
if __name__ == "__main__":
    ht = HashTable()

    # Insert test data
    fruits = ["apple", "banana", "kiwi", "papaya", "berry", "mango", "grapes", "orange"]
    for i in range(len(fruits)):
        ht.insert(fruits[i], i**2)

    ht.display()

    # Insert another item to trigger resizing
    ht.insert("pear", 81)
    ht.display()

    # Remove multiple items and trigger shrinking
    ht.remove("apple")
    ht.remove("banana")
    ht.remove("kiwi")
    ht.remove("papaya")
    ht.remove("berry")

    ht.display()

    # Retrieve a key that has been removed
    ht.get("apple")  # Should print "Key 'apple' not found!" and return None
