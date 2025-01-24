# ------------------------------------------------------
# File: floyds_cycle_detection_algorithm.py
# Date: 2025-01-24
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Detect and remove a cycle in a linked list using Floyd’s Cycle Detection Algorithm
# aka Floyd's Tortoise and Hare

class Node:
    # Initialize a new node with data and a pointer to the next node (None by default)
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Initialize an empty linked list with the head set to None
    def __init__(self):
        self.head = None

    # Append a new node with data to the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            # Traverse the list to find the last node
            while current.next:
                current = current.next

            # Set the next of the last node to the new node
            current.next = new_node

    # Display the linked list, with a limit on how many elements to show
    def display(self, limit=20):
        current = self.head
        result = []
        count = 0

        # Traverse the list and collect node data up to the limit
        while current and count < limit:
            result.append(str(current.data))
            current = current.next
            count += 1
        
        # Return the list as a string, showing " -> ..." if the limit is reached
        return " -> ".join(result) + (" -> ..." if count == limit else " -> Null")

    # Create a cycle in the linked list by connecting the last node to the node at position `pos`
    def create_cycle(self, pos):
        if pos < 1:
            print("Invalid position to create a cycle.")
            return

        cycle_start = None
        current = self.head
        count = 1

        # Traverse the list and locate the position to start the cycle
        while current.next:
            if count == pos:
                cycle_start = current  # Mark the node where the cycle will start
            current = current.next
            count += 1

        # If the cycle start node is found, link the last node to it
        if cycle_start:
            current.next = cycle_start
            print(f"Cycle created at position {pos}.")
        else:
            print("Invalid position. No cycle created.")

    # Detect a cycle in the linked list using the slow and fast pointer method
    def detect_cycle(self):
        slow, fast = self.head, self.head  # Initialize two pointers (slow and fast)

        # Traverse the list with slow moving one step at a time and fast moving two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # If slow and fast meet, a cycle is detected
            if slow == fast:
                return slow  # Return the node where the cycle starts

        return None  # No cycle detected

    # Remove the detected cycle in the linked list by adjusting the next pointers
    def remove_cycle(self, cycle_node):
        slow = self.head

        # Move slow and cycle_node forward until they meet at the start of the cycle
        while slow != cycle_node:
            slow = slow.next
            cycle_node = cycle_node.next

        # Traverse the cycle and remove the cycle by setting the last node's next to None
        while cycle_node.next != slow:
            cycle_node = cycle_node.next
        cycle_node.next = None

    # Detect and remove the cycle in the list if it exists
    def detect_remove_cycle(self):
        cycle_node = self.detect_cycle()

        # If a cycle is detected, remove it and return True
        if cycle_node:
            self.remove_cycle(cycle_node)
            print("Cycle detected and removed.")
            return True

        print("No cycle detected.")
        return False

# Test code
if __name__ == "__main__":
    ll = LinkedList()

    # Append even numbers to the linked list
    for i in range(2, 11, 2):
        ll.append(i)

    # Display the original linked list
    print(f"The original linked list is:\n{ll.display()}")

    # Create a cycle starting at position 3
    ll.create_cycle(3)
    print(f"The linked list with a cycle is:\n{ll.display()}")

    # Detect and remove the cycle
    if ll.detect_remove_cycle():
        print(f"The linked list after cycle removal is:\n{ll.display()}")
