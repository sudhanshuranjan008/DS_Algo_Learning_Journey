# ------------------------------------------------------
# File: linked_list_deletion.py
# Date: 2025-01-21
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to do deletion in a linked list

# Class to define a Node of the linked list
class Node:
    def __init__(self, data):
        # Initialize a node with data and set the next pointer to None
        self.data = data
        self.next = None

# Class to define the LinkedList structure
class LinkedList:
    def __init__(self):
        # Initialize the head of the linked list to None (empty list)
        self.head = None

    # Method to append a new node to the linked list
    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse to the end of the list and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Method to delete the head node of the linked list
    def del_at_head(self):
        if not self.head:
            # If the list is empty, print a message and return
            print("List is empty. Nothing to delete.")
            return
        # Set the head to the next node, effectively removing the current head
        self.head = self.head.next
        print("Deleted the head node.")

    # Method to delete the tail node of the linked list
    def del_at_tail(self):
        if not self.head:
            # If the list is empty, print a message and return
            print("List is empty. Nothing to delete.")
            return
        if not self.head.next:
            # If there's only one node, set the head to None (empty list)
            self.head = None
            print("Deleted the last remaining node.")
            return
        # Traverse to the second-to-last node
        current = self.head
        while current.next.next:
            current = current.next
        # Set the next of the second-to-last node to None, removing the tail
        current.next = None
        print("Deleted the tail node.")

    # Method to display the linked list as a string
    def display(self):
        if not self.head:
            # Return a message if the list is empty
            return "List is empty."
        result = []
        current = self.head
        # Traverse through the list and collect node data
        while current:
            result.append(str(current.data))
            current = current.next
        # Join all the node data with " -> " and append " -> Null" to indicate the end
        return " -> ".join(result) + " -> Null"

# Main driver code
if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()
    # Append values (squares of numbers 1 to 5) to the list
    for i in range(1, 6):
        ll.append(i * 2)

    # Display the original linked list
    print(f"The original linked list is:\n{ll.display()}")

    # Delete the head node and display the list
    ll.del_at_head()
    print(f"The linked list after deletion at head is:\n{ll.display()}")

    # Delete the tail node and display the list
    ll.del_at_tail()
    print(f"The linked list after deletion at tail is:\n{ll.display()}")
