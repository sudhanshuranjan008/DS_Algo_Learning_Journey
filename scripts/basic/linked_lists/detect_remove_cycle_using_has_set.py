# ------------------------------------------------------
# File: detect_remove_cycle_using_hash_set.py
# Date: 2025-01-23
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Detect and remove a cycle in a linked list using hash set

class Node:
    # Node class represents an element in the linked list
    def __init__(self, data):
        self.data = data  # Store the value of the node
        self.next = None  # Initialize next to None (for the last node)

class LinkedList:
    # LinkedList class for managing a singly linked list
    def __init__(self):
        self.head = None  # Initialize the head of the list to None (empty list)

    def append(self, data):
        # Appends a new node with the provided data to the end of the list
        new_node = Node(data)  # Create a new node with the given data

        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse the list to find the last node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Set the new node as the next of the last node

    def display(self, limit=20):
        # Displays the list up to a limit (default is 20)
        current = self.head
        result = []
        count = 0

        # Traverse the list and collect data up to the specified limit
        while current and count < limit:
            result.append(str(current.data))  # Append node data to result list
            current = current.next  # Move to the next node
            count += 1
        
        # Join the result list with ' -> ' and check if it exceeds the limit
        return " -> ".join(result) + (" -> ..." if count == limit else " -> Null")
    
    def create_cycle(self, pos):
        # Creates a cycle in the list by connecting the last node to the node at position 'pos'
        if pos < 1:
            print("Invalid position to create a cycle.")
            return

        cycle_start = None
        current = self.head
        count = 1

        # Traverse the list to find the node at the given position 'pos'
        while current.next:
            if count == pos:
                cycle_start = current  # Store the node where the cycle will start
            current = current.next  # Move to the next node
            count += 1

        # If a valid position is found, create the cycle
        if cycle_start:
            current.next = cycle_start  # Point the last node to the node at 'pos'
            print(f"Cycle created at position {pos}.")
        else:
            print("Invalid position. No cycle created.")  # If position is invalid

    def detect_and_remove_cycle(self):
        # Detects if there is a cycle in the list and removes it
        node_set = set()  # Set to keep track of visited nodes
        current = self.head
        prev = None

        # Traverse the list and check for cycles by looking for repeated nodes
        while current:
            if current in node_set:
                # If a node is repeated, it indicates a cycle
                prev.next = None  # Remove the cycle by setting previous node's next to None
                print("Cycle detected and removed.")
                return True

            node_set.add(current)  # Add current node to the visited set
            prev = current  # Update previous node
            current = current.next  # Move to the next node

        print("No cycle detected.")  # If no cycle is found
        return False  # Return False if no cycle exists

# Main block to test the LinkedList class
if __name__ == "__main__":
    ll = LinkedList()  # Create an empty linked list

    # Append values to the list
    for i in range(2, 11, 2):
        ll.append(i)

    # Display the original list
    print(f"The original linked list is:\n{ll.display()}")

    # Create a cycle at position 3
    ll.create_cycle(3)

    # Display the list with the cycle
    print(f"The linked list with cycle is:\n{ll.display()}")

    # Detect and remove the cycle
    if ll.detect_and_remove_cycle():
        print(f"The linked list after cycle removal is:\n{ll.display()}")
