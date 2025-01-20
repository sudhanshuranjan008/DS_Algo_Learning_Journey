# ------------------------------------------------------
# File: linked_list_intro.py
# Date: 2025-01-20
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to create and print a linked list

# Define the Node class to represent each element (node) in the linked list.
class Node:
    def __init__(self, data):
        self.data = data  # Store the data in the node.
        self.next = None  # Pointer to the next node in the list, initialized to None.

# Define the LinkedList class to represent the linked list structure.
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with an empty head (start of the list).

    # Method to add a new node to the end of the linked list.
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data.
        if not self.head:  # If the list is empty (head is None):
            self.head = new_node  # Set the new node as the head of the list.
        else:
            # Traverse the list to find the last node.
            current = self.head
            while current.next:  # Continue until the current node's next pointer is None.
                current = current.next
            # Link the last node to the new node.
            current.next = new_node

    # Method to display all the nodes in the linked list.
    def display(self):
        current = self.head  # Start from the head of the list.
        while current:  # Traverse the list until current is None (end of the list).
            print(current.data, end=" -> ")  # Print the data of the current node.
            current = current.next  # Move to the next node in the list.
        print("null")  # Print "null" to indicate the end of the list.

# The following block ensures that the code runs only when the file is executed directly.
if __name__ == "__main__":
    ll = LinkedList()  # Create an instance of the LinkedList class.
    
    # Append nodes to the linked list with the given data.
    ll.append(3)   # Add a node with the value 3.
    ll.append(5)   # Add a node with the value 5.
    ll.append(13)  # Add a node with the value 13.
    ll.append(2)   # Add a node with the value 2.

    # Display the linked list.
    ll.display()  # Expected output: 3 -> 5 -> 13 -> 2 -> null
