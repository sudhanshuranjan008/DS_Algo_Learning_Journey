# ------------------------------------------------------
# File: binary_numbers_generation_using_queue.py
# Date: 2025-01-31
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Generate binary numbers from 1 to N using a queue

from collections import deque

def print_binary_till_n(N: int) -> str:
    """
    Generate binary numbers from 1 to N using a queue.

    Args:
        N (int): The upper limit for the binary sequence.

    Returns:
        str: A space-separated string of binary numbers from 1 to N.
    """
    # Initialize the queue with the first binary number
    queue = deque(["1"])
    result = []  # To store the final binary numbers

    for _ in range(N):
        # Dequeue the current binary number
        current = queue.popleft()
        # Enqueue the current binary number
        result.append(current)

        # Enqueue the next two binary numbers derived from the current number
        queue.append(current + "0")
        queue.append(current + "1")

    # Join and return the list of binary numbers into a single space-separated string
    return " ".join(result)

if __name__ == "__main__":
    try:
        # Input from the user
        input_num = int(input("Please enter the number till which you want to generate binary sequence: "))
        
        # Check if the input is valid
        if input_num <= 0:
            print("Invalid input! Please enter a positive integer.")  # Non-positive numbers are not allowed
        else:
            # Generate and print the binary sequence
            print(f"The binary sequence from '1' to '{input_num}' is:\n{print_binary_till_n(input_num)}")
    except ValueError:
        # Handle invalid input such as strings or special characters
        print("Invalid input! Please enter a positive integer.")

