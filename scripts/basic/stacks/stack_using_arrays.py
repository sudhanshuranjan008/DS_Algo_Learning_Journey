# ------------------------------------------------------
# File: stack_using_arrays.py
# Date: 2025-01-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a stack using arrays

from array import array  # Importing the array module for efficient, typed array operations

# Class to represent a stack using a fixed-size array
class Stack:
    def __init__(self, size):
        # Constructor to initialize stack attributes
        self.stack = array('i', [0] * size)  # Initialize an integer array of given size
        self.top = -1  # Index of the top element (-1 indicates an empty stack)
        self.size = size  # Maximum size of the stack

    # Method to check if the stack is empty
    def is_empty(self):
        return self.top == -1  # Returns True if top is -1, meaning no elements in the stack

    # Method to check if the stack is full
    def is_full(self):
        return self.top == self.size - 1  # Returns True if the top index is at the maximum capacity

    # Method to push an element onto the stack
    def push(self, item):
        if self.is_full():  # Check for stack overflow
            print("Stack is full. Cannot push.")  # Print error message if stack is full
        else:
            self.top += 1  # Increment the top pointer
            self.stack[self.top] = item  # Add the new element to the top of the stack
            print(f"{item} pushed to stack.")  # Print confirmation message

    # Method to pop (remove) the top element from the stack
    def pop(self):
        if self.is_empty():  # Check for stack underflow
            return "Stack is empty. Nothing to pop."  # Return error message if stack is empty
        else:
            item = self.stack[self.top]  # Get the top element
            self.top -= 1  # Decrement the top pointer
            return item  # Return the popped element

    # Method to peek (view) the top element without removing it
    def peek(self):
        if self.is_empty():  # Check if the stack is empty
            return "Stack is empty."  # Return error message
        else:
            return self.stack[self.top]  # Return the top element

# Main block to test the stack implementation
if __name__ == "__main__":
    stack = Stack(5)  # Create a stack with a maximum size of 5
    stack.push(2)  # Push element 2 onto the stack
    stack.push(3)  # Push element 3 onto the stack
    stack.push(5)  # Push element 5 onto the stack
    stack.push(7)  # Push element 7 onto the stack
    stack.push(11)  # Push element 11 onto the stack
    stack.push(13)  # Attempt to push element 13 (will fail since the stack is full)
    print(f"Top element in the stack is {stack.peek()}")  # Display the top element
    print(f"Popped element {stack.pop()} from the stack.")  # Pop and display the top element

