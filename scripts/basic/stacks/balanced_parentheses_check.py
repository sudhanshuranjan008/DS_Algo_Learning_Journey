# ------------------------------------------------------
# File: balanced_parentheses_check.py
# Date: 2025-01-27
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check for balanced parentheses in an expression

# Stack class definition to implement basic stack operations
class Stack:
    # Initialize the stack as an empty list
    def __init__(self):
        self.this_stack = []

    # Check if the stack is empty (returns True if empty, False otherwise)
    def is_empty(self):
        return len(self.this_stack) == 0

    # Push an item onto the stack (adds an element to the top of the stack)
    def push(self, item):
        self.this_stack.append(item)

    # Peek at the top element of the stack without removing it
    def peek(self):
        if self.is_empty():
            return None  # If stack is empty, return None
        return self.this_stack[-1]  # Return the top item

    # Pop the top element from the stack (removes and returns it)
    def pop(self):
        if self.is_empty():
            return None  # If stack is empty, return None
        return self.this_stack.pop()  # Remove and return the top item
    
# Function to check if the parentheses in the input string are balanced
def check_par_balance(input_string, input_stack):
    # Iterate through each character in the input string
    for par in input_string:
        # If the character is an opening parenthesis, push it onto the stack
        if par in ("(", "{", "["):
            input_stack.push(par)
        
        # If the character is a closing parenthesis, check if it matches the last opened parenthesis
        elif par == ")" and input_stack.peek() == "(":
            input_stack.pop()  # If matches, pop the opening parenthesis from the stack
        elif par == "}" and input_stack.peek() == "{":
            input_stack.pop()  # If matches, pop the opening parenthesis from the stack
        elif par == "]" and input_stack.peek() == "[":
            input_stack.pop()  # If matches, pop the opening parenthesis from the stack
        else:
            return False  # If a mismatch is found, return False (indicating unbalanced)

    # If the stack is empty, all opening parentheses were matched and balanced
    return input_stack.is_empty()

# Main block to test the stack-based parentheses balancing function
if __name__ == "__main__":
    my_stack = Stack()  # Create an instance of the Stack class
    my_string = "(()){}[]"  # Test string with balanced parentheses
    print("Input Parentheses: ", my_string)
    
    # Check if the parentheses in the string are balanced using the check_par_balance function
    result = check_par_balance(my_string, my_stack)

    # Print the result based on whether parentheses are balanced or not
    if result:
        print("Parentheses are balanced.")
    else:
        print("Parentheses are not balanced.")


    

    