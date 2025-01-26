# ------------------------------------------------------
# File: stack_using_2_pointers_linked_list.py
# Date: 2025-01-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a stack using a linked list(2 Pointers)

class Node:
    def __init__(self, data):
        self.data = data  # Store the data of the node
        self.next = None  # Pointer to the next node in the linked list

class Stack:
    def __init__(self):
        self.head = None  # Points to the first node (bottom of the stack)
        self.tail = None  # Points to the last node (top of the stack)

    def is_empty(self):
        # Check if the stack is empty by checking if head is None
        return self.head is None
    
    def push(self, data):
        # Create a new node to hold the data
        new_node = Node(data)

        # If the stack is empty, initialize head and tail with the new node
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            # Otherwise, add the new node to the end of the linked list
            self.tail.next = new_node
            self.tail = new_node  # Update tail to point to the new node
    
    def peek(self):
        # Return the data of the top element (tail) if stack is not empty
        if not self.is_empty():
            return self.tail.data
        else:
            # Handle empty stack for peek operation
            print("Stack is empty.")
            return None
        
    def pop(self):
        # Handle underflow if the stack is empty
        if self.is_empty():
            print("Stack underflow. Cannot pop")
            return None

        # If the stack has only one element, remove it and update head and tail
        if not self.head.next:
            popped_value = self.head.data
            self.head = self.tail = None  # Reset head and tail to None
            return popped_value
        else:
            # Store the data of the top element to return later
            popped_value = self.tail.data

            # Traverse the linked list to find the second-last node
            current = self.head
            while current.next.next:
                current = current.next
            
            # Update tail to the second-last node and remove the last node
            self.tail = current
            current.next = None  # Remove the reference to the last node

            return popped_value  # Return the popped value
    
if __name__ == "__main__":
    # Initialize the stack
    my_stack = Stack()

    # Push elements onto the stack
    my_stack.push(2)
    my_stack.push(4)

    # Peek at the top element of the stack
    print(f"Top element: {my_stack.peek()}")

    # Pop elements from the stack
    print(f"Popped value: {my_stack.pop()}")
    print(f"Top element: {my_stack.peek()}")
    print(f"Popped value: {my_stack.pop()}")

    # Attempt to peek and pop from an empty stack
    print(f"Top element: {my_stack.peek()}")
    print(f"Popped value: {my_stack.pop()}")
