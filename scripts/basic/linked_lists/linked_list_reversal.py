# ------------------------------------------------------
# File: linked_list_reversal.py
# Date: 2025-01-23
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Program to reverse a linked list

class Node:
    def __init__(self, data):
        self.data = data  # Stores the data for the node.
        self.next = None  # Points to the next node in the linked list.


class LinkedList:
    def __init__(self):
        self.head = None  # Initializes an empty linked list with no head.

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data.

        if not self.head:  # Check if the list is empty.
            self.head = new_node  # Set the new node as the head of the list.

        else:
            current = self.head  # Start traversal from the head.
            while current.next:  # Traverse until the last node.
                current = current.next

            current.next = new_node  # Append the new node at the end.

    def display(self):
        current = self.head  # Start traversal from the head.
        result = []  # List to store node values for display.
        while current:
            result.append(str(current.data))  # Append data of each node to the result list.
            current = current.next

        return " -> ".join(result) + " -> Null"  # Return the linked list as a string.

    def reverse_linked_list(self):
        if not self.head:   # Explicit check for empty list.
            print("The list is empty, nothing to reverse.")
            return

        # Initialize pointers to reverse the list.
        current = self.head  # Pointer to traverse the list.
        previous = None  # Pointer to keep track of the reversed part.

        while current:
            next_node = current.next  # Store the next node.
            current.next = previous  # Reverse the link to point to the previous node.
            previous = current  # Move the `previous` pointer forward.
            current = next_node  # Move the `current` pointer forward.

        self.head = previous  # Update the head to the last node (now the first node in the reversed list).
        print("The linked list has been reversed successfully.")


if __name__ == "__main__":
    ll = LinkedList()

    # Append values to the linked list.
    for i in range(5, 30, 5):
        ll.append(i)

    print(f"The original linked list is:\n{ll.display()}")  # Display the original list.

    ll.reverse_linked_list()  # Reverse the linked list.

    print(f"The reversed linked list is:\n{ll.display()}")  # Display the reversed list.

