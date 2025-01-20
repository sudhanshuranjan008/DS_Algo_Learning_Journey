# ------------------------------------------------------
# File: linked_list_value_search.py
# Date: 2025-01-20
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to search for a value in the linked list

# Class to represent a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node, initialized to None (end of list)

# Class to represent the Linked List
class LinkedList:
    def __init__(self):
        self.head = None  # Head pointer initialized to None (empty list)

    # Method to append a node with given data to the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the provided data

        if not self.head:  # If the list is empty, the new node becomes the head
            self.head = new_node
        else:
            current = self.head  # Start traversing from the head
            while current.next:  # Move to the end of the list
                current = current.next
            
            current.next = new_node  # Link the last node to the new node
    
    # Method to search for a value in the linked list
    def search_linked_list(self, value):
        current = self.head  # Start from the head node
        while current:  # Traverse the list until the end (current is None)
            if current.data == value:  # If the value is found, return True
                return True
            current = current.next  # Move to the next node
        
        return False  # Return False if the value was not found

# Main program execution
if __name__ == "__main__":

    ll = LinkedList()  # Create an empty linked list
    
    # Append numbers 0 to 4 to the linked list
    for i in range(5):
        ll.append(i)

    # Input from user to search in the linked list
    search_value = int(input("Enter the value to be searched: "))
    
    # Search the linked list for the value
    result = ll.search_linked_list(search_value)

    # Output whether the value is present or not in the list
    if result:
        print(f"{search_value} is present in the list.")
    else:
        print(f"{search_value} is not present in the list")

