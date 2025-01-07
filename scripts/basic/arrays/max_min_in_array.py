# ------------------------------------------------------
# File: max_min_in_array.py
# Date: 2025-01-07
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the maximum and minimum element in an array

# Function to find the maximum element in an array
def maximum(arr: list) -> int:
    # Check if the array is empty and raise an error if it is
    if not arr:
        raise ValueError("The array is empty. Cannot determine the maximum value.")
    
    # Initialize the maximum element as the first element of the array
    max_el = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update max_el if the current element is greater than max_el
        if arr[i] > max_el:
            max_el = arr[i]
    
    # Return the largest element found
    return max_el

# Function to find the minimum element in an array
def minimum(arr: list) -> int:
    # Check if the array is empty and raise an error if it is
    if not arr:
        raise ValueError("The array is empty. Cannot determine the minimum value.")
    
    # Initialize the minimum element as the first element of the array
    min_el = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update min_el if the current element is smaller than min_el
        if arr[i] < min_el:
            min_el = arr[i]
    
    # Return the smallest element found
    return min_el

if __name__ == "__main__":
    # Define an array to test the functions
    myarray = [2, 8, 56, 75, 3, 9]
    
    # Call the maximum function and print the largest element
    print(f"The element with the largest value in the array is: {maximum(myarray)}")
    
    # Call the minimum function and print the smallest element
    print(f"The element with the smallest value in the array is: {minimum(myarray)}")

