# ------------------------------------------------------
# File: fibonacci.py
# Date: 2025-02-04
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Print the Fibonacci sequence up to N terms

def fib(N):
    """Recursive function to return the Nth Fibonacci number."""
    # Define base cases
    if N == 0:
        return 0
    if N == 1:
        return 1
    # Recursive step to compute Fibonacci number
    return fib(N - 1) + fib(N - 2)

if __name__ == "__main__":
    # Take user input for the number of terms in the sequence
    num = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
    
    # Print Fibonacci sequence
    print("The Fibonacci sequence is:")
    for i in range(num):
        print(fib(i), end=" ")  # Call the Fibonacci function and print result




