# ------------------------------------------------------
# File: second_max_min_in_array.py
# Date: 2025-01-08
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the "2nd" smallest/largest element in an array

def second_maximum(arr: list) -> int:
    # Check if the input array is empty and raise an error if true
    if not arr:
        raise ValueError("The array is empty. Cannot determine the maximum value.")
    
    # Initialize the largest and second largest elements to negative infinity
    max_el = float('-inf')  # Maximum element
    second_max_el = float('-inf')  # Second maximum element

    # Iterate through the array to find the largest and second largest elements
    for el in arr:
        if el > max_el:
            # If current element is greater than max_el, update both max_el and second_max_el
            second_max_el = max_el
            max_el = el
        elif max_el > el > second_max_el:
            # If current element is smaller than max_el but larger than second_max_el, update second_max_el
            second_max_el = el

    return second_max_el  # Return the second largest element

def second_minimum(arr: list) -> int:
    # Check if the input array is empty and raise an error if true
    if not arr:
        raise ValueError("The array is empty. Cannot determine the minimum value.")
    
    # Initialize the smallest and second smallest elements to positive infinity
    min_el = float('inf')  # Minimum element
    second_min_el = float('inf')  # Second minimum element
    
    # Iterate through the array to find the smallest and second smallest elements
    for el in arr:
        if el < min_el:
            # If current element is smaller than min_el, update both min_el and second_min_el
            second_min_el = min_el
            min_el = el
        elif min_el < el < second_min_el:
            # If current element is larger than min_el but smaller than second_min_el, update second_min_el
            second_min_el = el

    return second_min_el  # Return the second smallest element

if __name__ == "__main__":
    # Example array to test the functions
    my_array = [-5, 4, 85, 6, 12, 14]
    
    # Find and print the second largest element in the array
    print(f"The second largest element in the array is: {second_maximum(my_array)}")
    
    # Find and print the second smallest element in the array
    print(f"The second smallest element in the array is: {second_minimum(my_array)}")