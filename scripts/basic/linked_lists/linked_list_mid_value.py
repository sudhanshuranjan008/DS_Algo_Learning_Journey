# ------------------------------------------------------
# File: linked_list_mid_value.py
# Date: 2025-01-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the middle value in a linked list

# Node class represents an individual element in the linked list
class Node:
    # Constructor to initialize the node with data and next pointer
    def __init__(self, data):
        self.data = data  # Holds the data of the node
        self.next = None  # Pointer to the next node, initially None

# LinkedList class represents the entire linked list
class LinkedList:
    # Constructor to initialize the linked list with an empty head
    def __init__(self):
        self.head = None  # Initially, the linked list is empty (head is None)

    # Method to append a new node with given data to the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # If the list is empty, the new node becomes the head
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            # Traverse the list until we find the last node
            while current.next:
                current = current.next

            # Set the next pointer of the last node to the new node
            current.next = new_node

    # Method to display the linked list as a string representation
    def display(self):
        # If the list is empty, return a message indicating that
        if not self.head:
            return "List is empty."
        
        result = []  # List to store string representations of node data
        current = self.head
        # Traverse through the list and append the data to result
        while current:
            result.append(str(current.data))
            current = current.next
        
        # Join the result with " -> " and append " -> Null" at the end
        return " -> ".join(result) + " -> Null"
    
    def mid_node_value(self):
    # Check if the linked list is empty
        if not self.head:
            return "List is empty."  # Return a message if there are no nodes in the list

    # Initialize two pointers: `slow` and `fast`, both starting at the head of the list
        slow = fast = self.head

    # Traverse the list using the two-pointer technique
    # `fast` moves two steps at a time, and `slow` moves one step at a time
        while fast and fast.next:  # Ensure `fast` and its next node are valid to prevent errors
            fast = fast.next.next  # Move `fast` two steps ahead
            slow = slow.next       # Move `slow` one step ahead

    # At the end of the loop, `slow` will be at the middle node
        return slow.data  # Return the data stored in the middle node

    

# Driver code
if __name__ == "__main__":
    ll = LinkedList()  # Create a new linked list instance

    # Append some initial values to the linked list
    for i in range(3, 19, 3):
        ll.append(i)

    # Print the list for clarity
    print(ll.display())

    # Call the function to find middle value and then print it
    result = ll.mid_node_value()
    print(f"The middle value in the list is: {result}")