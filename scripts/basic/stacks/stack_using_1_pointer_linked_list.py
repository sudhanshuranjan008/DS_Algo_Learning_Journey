# ------------------------------------------------------
# File: stack_using_1_pointer_linked_list.py
# Date: 2025-01-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a stack using a linked list(1 Pointer)

class Stack:
    class Node:
        """
        A class representing a node in the stack.
        Each node stores data and a reference to the next node.
        """
        def __init__(self, data):
            self.data = data  # Holds the data of the node
            self.next = None  # Points to the next node in the stack

    def __init__(self):
        """
        Initialize an empty stack.
        The top of the stack is set to None initially, and size is set to 0.
        """
        self.top = None  # Top element of the stack, initially None
        self.size = 0  # Size of the stack, initially 0

    def is_empty(self):
        """
        Check if the stack is empty.
        Returns True if the stack is empty, else False.
        """
        return self.top is None  # Stack is empty if top is None
    
    def stack_size(self):
        """
        Returns the size of the stack.
        """
        return self.size  # Return the current size of the stack
    
    def push(self, data):
        """
        Push a new element onto the stack.
        The new node is added to the top of the stack, and the size is incremented.
        Args:
            data: The value to be added to the stack.
        """
        new_node = self.Node(data)  # Create a new node with the given data
        new_node.next = self.top  # The new node's next points to the current top
        self.top = new_node  # The new node becomes the new top of the stack
        print(f"{data} is pushed to stack.")  # Print confirmation of the operation
        self.size += 1  # Increment the size of the stack

    def peek(self):
        """
        View the top element of the stack without removing it.
        Returns:
            The data of the top element if the stack is not empty; otherwise, None.
        """
        if self.is_empty():
            print("Stack is empty.")  # Handle the case where the stack is empty
            return None
        return self.top.data  # Return the data of the top element
        
    def pop(self):
        """
        Remove and return the top element of the stack.
        Returns:
            The data of the popped element if the stack is not empty; otherwise, None.
        """
        if self.is_empty():
            print("Stack underflow. Nothing to delete.")  # Handle stack underflow
            return None
        
        popped_value = self.top.data  # Store the data of the top element
        self.top = self.top.next  # Set the top to the next node in the stack
        self.size -= 1  # Decrement the size of the stack
        print(f"Popped element: {popped_value}")  # Print confirmation of the popped element
        return popped_value  # Return the popped value
        
if __name__ == "__main__":
    # Test cases to verify the stack operations
    my_stack = Stack()  # Create an instance of Stack
    my_stack.push(2)  # Push 2 onto the stack
    my_stack.push(3)  # Push 3 onto the stack
    print(f"The size of stack is: {my_stack.stack_size()}")  # Print the stack size
    print(f"Top element: {my_stack.peek()}")  # Peek the top element
    my_stack.pop()  # Pop the top element
    print(f"The size of stack is: {my_stack.stack_size()}")  # Print the updated stack size
    print(f"Top element: {my_stack.peek()}")  # Peek the new top element
    my_stack.pop()  # Pop the next top element
    print(f"Top element: {my_stack.peek()}")  # Peek the top element again
    my_stack.pop()  # Pop the final element (stack should be empty now)



    