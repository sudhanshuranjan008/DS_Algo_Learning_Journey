# File: hash_table_with_linked_list.py
# Date: 2025-02-15
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement hash table with linked list for collision handling

# Node class for linked list
class Node:
    def __init__(self, key, value):
        self.key = key  # Stores key
        self.value = value  # Stores value
        self.next = None  # Pointer to next node in case of collision

# Hash Table class
class HashTable:
    def __init__(self, size=10):
        self.size = size  # Defines size of hash table
        self.table = [None] * self.size  # Initializes the table with None

    # Hash function to compute index from key
    def hash_function(self, key):
        sum_of_chars = sum(ord(char) for char in key)  # Sum ASCII values of key characters
        return sum_of_chars % self.size  # Modulo to fit within table size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self.hash_function(key)  # Compute index using hash function
        new_node = Node(key, value)  # Create a new node

        # If no collision, insert directly
        if not self.table[index]:
            self.table[index] = new_node
        else:
            # Collision detected, insert at the head (chaining via linked list)
            new_node.next = self.table[index]  # Link new node to existing head
            self.table[index] = new_node  # Update head to new node

    # Retrieve the value for a given key
    def get(self, key):
        index = self.hash_function(key)  # Compute index
        current_node = self.table[index]  # Get the linked list at that index

        # Traverse the linked list to find the key
        while current_node:
            if current_node.key == key:
                return current_node.value  # Return the value if found
            current_node = current_node.next  # Move to next node

        return None  # Key not found, return None

    # Remove a key-value pair from the hash table
    def remove(self, key):
        index = self.hash_function(key)  # Compute index
        current_node = self.table[index]
        prev_node = None

        # Traverse the linked list to find the key
        while current_node:
            if current_node.key == key:
                if prev_node:  # If node is not head, update previous node's next pointer
                    prev_node.next = current_node.next
                else:  # If node is head, move the head pointer
                    self.table[index] = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next

        print("Key not found!")  # If key is not found, print message

    # Display the hash table
    def display(self):
        for i, bucket in enumerate(self.table):  # Loop through each index in the hash table
            current_node = bucket  # Get the linked list at index
            chain = []
            while current_node:  # Traverse the linked list
                chain.append((current_node.key, current_node.value))  # Store as tuple
                current_node = current_node.next
            print(f"Index {i}: {chain}")  # Print key-value pairs at each index

# Example Usage
ht = HashTable()

# Insert key-value pairs
ht.insert("apple", 5)
ht.insert("banana", 3)
ht.insert("orange", 8)
ht.insert("papaya", 10)
ht.insert("mango", 19)

# Display the hash table
ht.display()

# Retrieve the value for a key
print(f"mango: {ht.get('mango')}")

# Attempt to remove a non-existent key
ht.remove("kiwi")

# Remove an existing key
ht.remove("apple")

# Display the hash table after removal
ht.display()

