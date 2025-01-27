# ------------------------------------------------------
# File: balanced_parentheses_check_hashmap.py
# Date: 2025-01-27
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check for balanced parentheses in an expression(Hash Map Method)

class Stack:
    def __init__(self):
        # Initialize an empty list to act as the stack
        self.this_stack = []

    def is_empty(self):
        # Returns True if the stack is empty, False otherwise
        return len(self.this_stack) == 0
    
    def push(self, item):
        # Adds the item to the top of the stack
        self.this_stack.append(item)

    def peek(self):
        # Returns the item at the top of the stack without removing it
        if self.is_empty():
            return None
        return self.this_stack[-1]
    
    def pop(self):
        # Removes and returns the item from the top of the stack
        if self.is_empty():
            return None
        return self.this_stack.pop()

def check_par_balance(input_string, input_stack):
    # Dictionary to match closing parentheses to opening parentheses
    matching_pairs = {")": "(", "}": "{", "]": "["}

    for par in input_string:
        # If the character is an opening parenthesis, push it to the stack
        if par in matching_pairs.values():
            input_stack.push(par)
        # If it's a closing parenthesis, check if it matches the top of the stack
        elif par in matching_pairs:
            if input_stack.peek() == matching_pairs[par]:
                input_stack.pop()  # Pop if there's a match
            else:
                return False  # Mismatch found, return False
            
    # Return True if the stack is empty (all parentheses matched), else False
    return input_stack.is_empty()


if __name__ == "__main__":
    my_stack = Stack()  # Create an instance of the Stack class
    my_string = "({{[([])]}})"  # Test string with balanced parentheses
    print("Input Parentheses: ", my_string)

    result = check_par_balance(my_string, my_stack)  # Check if the parentheses are balanced
    if result:
        print("Parentheses are balanced.")
    else:
        print("Parentheses are not balanced.")
