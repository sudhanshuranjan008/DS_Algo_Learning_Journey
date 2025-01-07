# ------------------------------------------------------
# File: array_reversal.py
# Date: 2025-01-07
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to reverse an array

# Function to reverse an array while preserving the original array
def reverse_array_copy(arr: list) -> list:
    # Create a copy of the original array to avoid modifying it
    arr_copy = arr.copy()
    
    # Initialize pointers for the start (left) and end (right) of the array
    left = 0
    right = len(arr_copy) - 1

    # Swap elements until the pointers meet in the middle
    while left < right:
        arr_copy[left], arr_copy[right] = arr_copy[right], arr_copy[left]  # Swap the elements
        left += 1  # Move the left pointer one step to the right
        right -= 1  # Move the right pointer one step to the left

    # Return the reversed copy of the array
    return arr_copy

# Main execution block
if __name__ == "__main__":
    # Define the original array
    my_arr = [1, 2, 3, 4, 5, 6]
    
    # Call the function to reverse the array and store the result
    rev_arr = reverse_array_copy(my_arr)
  
    # Print the original array to show it remains unchanged
    print(f"Original array is: {my_arr}")
    
    # Print the reversed array
    print(f"Reversed array is: {rev_arr}")
