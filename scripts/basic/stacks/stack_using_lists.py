# ------------------------------------------------------
# File: stack_using_lists.py
# Date: 2025-01-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Stack implementation using functions and lists (arrays in Python)

# Function to create a new stack
def create_stack():
    return []  # Initialize and return an empty stack (using a list)

# Function to check if the stack is empty
def is_empty(stack):
    return len(stack) == 0  # Return True if the stack is empty, otherwise False

# Function to push an element onto the stack
def push(stack, item):
    stack.append(item)  # Add the element to the top of the stack
    print(f"{item} pushed to stack.")  # Print confirmation

# Function to pop (remove) the top element from the stack
def pop(stack):
    if is_empty(stack):  # Check if the stack is empty
        return "Stack is empty. Nothing to pop."  # Handle underflow by returning a message
    return stack.pop()  # Remove and return the top element of the stack

# Function to peek (view) the top element of the stack without removing it
def peek(stack):
    if is_empty(stack):  # Check if the stack is empty
        return "Stack is empty."  # Return a message if the stack is empty
    return stack[-1]  # Return the top element of the stack

# Example usage
if __name__ == "__main__":
    stack = create_stack()  # Initialize an empty stack
    push(stack, 2)  # Push the element 2 onto the stack
    push(stack, 3)  # Push the element 4 onto the stack
    push(stack, 5)  # Push the element 6 onto the stack
    print(f"Top element: {peek(stack)}")  # Display the top element using peek
    print(f"Popped element: {pop(stack)}")  # Remove and display the top element using pop
    print(f"Stack after popping: {stack}")  # Display the stack after popping an element


