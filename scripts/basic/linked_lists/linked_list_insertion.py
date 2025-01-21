# ------------------------------------------------------
# File: linked_list_insertion.py
# Date: 2025-01-21
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to do insertion in a linked list

# Class to represent a node in the linked list
class Node:
    def  __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node, initialized as None

# Class to represent the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # The head (starting node) of the linked list, initialized as None

    # Method to append a new node with the given data at the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the provided data

        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node

        else:  # Traverse to the end of the list and append the new node
            current = self.head
            while current.next:  # Continue until the current node's next pointer is None
                current = current.next
            
            current.next = new_node  # Link the last node to the new node

    # Method to display the elements of the linked list
    def display(self):
        current = self.head  # Start from the head of the list
        while current:  # Traverse until the end of the list (current becomes None)
            print(current.data, end=" -> ")  # Print the data of the current node
            current = current.next  # Move to the next node
        
        print("Null")  # Indicate the end of the linked list
    
    # Method to insert a new node at the head (start) of the linked list
    def insert_at_head(self, data):
        new_node = Node(data)  # Create a new node with the provided data
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to be the new node

    # Method to insert a new node at the tail (end) of the linked list
    def insert_at_tail(self, data):
        new_node = Node(data)  # Create a new node with the provided data
        current = self.head  # Start from the head of the list
        while current.next:  # Traverse until the last node
            current = current.next

        current.next = new_node  # Link the last node to the new node

# Main program to test the linked list implementation
if __name__ == "__main__":
    ll = LinkedList()  # Create an instance of the LinkedList class

    # Append squares of numbers from 2 to 5 to the linked list
    for i in range(2, 6):
        ll.append(i * i)
    
    # Display the original linked list
    print("The original linked list is :")
    ll.display()

    # Insert the square of 1 at the start of the list
    ll.insert_at_head(1 * 1)

    # Display the list after inserting at the head
    print("The list after inserting square of 1 at start is :")
    ll.display()

    # Insert the square of 6 at the end of the list
    ll.insert_at_tail(6 * 6)

    # Display the list after inserting at the tail
    print("The list after inserting square of 6 in the end is :")
    ll.display()
