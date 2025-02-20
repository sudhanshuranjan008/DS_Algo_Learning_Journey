# ------------------------------------------------------
# File: array_equality_check.py
# Date: 2025-02-20
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check if two arrays are equal using hashing

class HashTable:
    def __init__(self, size=11):
        # Initialize the hash table with empty slots
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        """Generate an index using a simple modulus-based hash function."""
        return sum(ord(char) for char in str(key)) % self.size
    
    def insert(self, key, value):
        """Insert or update key-value pair using linear probing for collision handling."""
        index = self.hash_function(key)
        original_index = index

        # Find an available slot or update an existing key
        while self.table[index] is not None:
            if self.table[index][0] == key:
                # Update count for existing key
                self.table[index] = (key, self.table[index][1] + value)
                return

            index = (index + 1) % self.size  # Move to next slot
            if index == original_index:
                return False  # Table is full (no resizing in this version)

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
                return self.table[index][1]  # Return stored count
            
            index = (index + 1) % self.size  # Move to next slot
            if index == original_index:
                break  # Stop if we have looped back to the original position

        return None  # Key not found


def is_equal_array(arr1, arr2):
    """Check if two arrays contain the same elements with the same frequencies."""
    if len(arr1) != len(arr2):
        return False  # Different lengths -> Not equal 
    
    ht = HashTable(len(arr1))  # Create hash table
    
    # Store frequency counts from first array
    for item in arr1:        
        ht.insert(item, 1)
    
    # Check and reduce frequency counts using second array
    for item in arr2:
        count = ht.get(item)  # Lookup frequency count
        if count is None or count == 0:
            return False  # Element missing or count mismatch
        
        ht.insert(item, -1)  # Reduce count for the matched item
    
    return True  # Arrays are equal

# Driver function for testing
if __name__ == "__main__":
    list1 = [1, 8, 6, 5, 1, 8, 6]
    list2 = [8, 6, 1, 5, 1, 8, 6]
    
    result = is_equal_array(list1, list2)
    
    if result:
        print("EQUAL :)")
    else:
        print("NOT EQUAL :(")

