# ------------------------------------------------------
# File: stack_minimum_element.py
# Date: 2025-01-27
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Design a stack that supports get_min() in O(1) for finding item with minimum value

class Stack:
    def __init__(self):
        # Initialize two stacks: one for main data and one for minimum tracking
        self.main_stack = []
        self.min_stack = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.main_stack) == 0
    
    def push(self, item):
        # Push item onto the main stack
        self.main_stack.append(item)

        # If the min_stack is empty or the new item is smaller than the current minimum
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
        else:
            # Otherwise, duplicate the current minimum value in min_stack
            self.min_stack.append(self.min_stack[-1])


    def peek(self):
        # Peek at the top of the main stack
        if self.is_empty():
            return None
        return self.main_stack[-1]
    
    def pop(self):
        # Remove the top item from both stacks if not empty
        if self.is_empty():
            return None
        self.min_stack.pop()  # Update the min_stack
        return self.main_stack.pop()  # Return the popped item
    
    def get_min(self):
        # Retrieve the current minimum value in O(1) time
        if self.is_empty():
            return None
        return self.min_stack[-1]
        

if __name__ == "__main__":
    # Create a stack instance
    my_stack = Stack()

    # Push items onto the stack
    my_stack.push(10)
    my_stack.push(5)
    my_stack.push(5)
    my_stack.push(7)
    my_stack.push(19)
    my_stack.push(2)

    # Display the top and minimum values at each step
    print(f"The top item in stack is: {my_stack.peek()}")
    print(f"The item with minimum value in stack is: {my_stack.get_min()}")
    print()

    # Pop items and display the updated top and minimum values
    print(f"Popped item: {my_stack.pop()}")
    print(f"The top item in stack is: {my_stack.peek()}")
    print(f"The item with minimum value in stack is: {my_stack.get_min()}")
    print()

    print(f"Popped item: {my_stack.pop()}")
    print(f"The top item in stack is: {my_stack.peek()}")
    print(f"The item with minimum value in stack is: {my_stack.get_min()}")
    print()

    print(f"Popped item: {my_stack.pop()}")
    print(f"The top item in stack is: {my_stack.peek()}")
    print(f"The item with minimum value in stack is: {my_stack.get_min()}")
    print()

    print(f"Popped item: {my_stack.pop()}")
    print(f"The top item in stack is: {my_stack.peek()}")
    print(f"The item with minimum value in stack is: {my_stack.get_min()}")
