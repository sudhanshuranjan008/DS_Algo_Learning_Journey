# ------------------------------------------------------
# File: reverse_string_using_stack.py
# Date: 2025-01-27
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Reverse a string using stack

# Function to create an empty stack
def create_stack():
    return []

# Function to check if the stack is empty
def is_empty(stack):
    return len(stack) == 0

# Function to add an item to the stack
def push(stack, item):
    stack.append(item)  # Append item to the end of the list (stack)

# Function to remove and return the top item from the stack
def pop(stack):
    if is_empty(stack):  # Check if the stack is empty before popping
        print("Stack underflow. Cannot pop.")  # Inform the user about the stack underflow
        return
    return stack.pop()  # Remove and return the last item in the stack

# Function to reverse a string using a stack
def reverse_string(input_string):
    # Ensure the input is a string
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")  # Raise an error for invalid input types

    # Create an empty stack
    my_stack = create_stack()

    # Push all characters of the string onto the stack
    for char in input_string:
        push(my_stack, char)

    # Initialize an empty list to store the reversed characters
    reversed_chars = []

    # Pop characters from the stack and append them to the reversed_chars list
    while not is_empty(my_stack):
        reversed_chars.append(pop(my_stack))

    # Join the reversed characters into a single string and return it
    return ''.join(reversed_chars)

# Main block to test the reverse_string function
if __name__ == "__main__":
    my_string = "learn_stack"  # Input string
    print(f"The input string is: {my_string}")  # Print the original string
    rev_string = reverse_string(my_string)  # Reverse the string
    print(f"The reversed string is: {rev_string}")  # Print the reversed string


