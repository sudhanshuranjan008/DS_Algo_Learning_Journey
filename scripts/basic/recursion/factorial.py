# ------------------------------------------------------
# File: factorial.py
# Date: 2025-02-04
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the factorial of a number

def factorial(num):
    """Recursive function to calculate factorial of a number."""
    if num in (0, 1):  # Base case: factorial of 0 or 1 is 1
        return 1
        
    return num * factorial(num - 1) # Recursive step
    
if __name__ == "__main__":
    # Keep prompting the user until a valid input is entered
    while True:
        try:
            # Get user input and validate it
            value = int(input("Enter the number to calculate its factorial: "))
            if value < 0:
                raise ValueError("Factorial is not defined for negative numbers.")
            break   # Exit loop if input is valid

        except ValueError as e:
            print(f"Invalid input! {e}")    # Display the error message

    # Compute and display the factorial
    print(f"Factorial of {value} is {factorial(value)}")