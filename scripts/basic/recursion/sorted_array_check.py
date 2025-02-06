# ------------------------------------------------------
# File: sorted_array_check.py
# Date: 2025-02-06
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check if an array is sorted using recursion

# Recursive function to check if the array is sorted in ascending order
def sorted_array_check_asc(num, index=0):
    # Base case: if we've reached the last element, the array is sorted up to this point
    if index == len(num) - 1:
        return True
    
    # Check if the current element is greater than the next element
    # If it is, the array is not sorted in ascending order
    if num[index] > num[index + 1]:
        return False
    
    # Recursively check the next elements in the array
    return sorted_array_check_asc(num, index + 1)

# Test the function with an example list
num_list = [1, 6, 8, 8, 9]
# Print the result (True if sorted in ascending order, False otherwise)
print(sorted_array_check_asc(num_list))
