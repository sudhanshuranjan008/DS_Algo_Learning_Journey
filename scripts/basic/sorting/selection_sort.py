# ------------------------------------------------------
# File: selection_sort.py
# Date: 2025-02-07
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Selection Sort to sort an array

def selection_sort(num):
    """
    Selection Sort Implementation
    Time Complexity:
        - Best/Worst/Average Case: O(n^2) (Nested loops)
    Space Complexity: O(1) (Sorts in place)
    
    This function sorts a list using the Selection Sort algorithm.
    Note: This modifies the input list in place.
    """
    if not num:  # Check for an empty list
        return "List is empty. Nothing to sort."
    
    n = len(num)
    if n == 1:  # Single element is already sorted
        return num

    for i in range(n):
        min_index = i  # Assume the first element of the unsorted part is the minimum
        for j in range(i + 1, n):  # Find the minimum element in the unsorted portion
            if num[j] < num[min_index]:
                min_index = j  # Update min_index if a smaller element is found
        
        if min_index != i:  # Swap only if a smaller element is found
            num[i], num[min_index] = num[min_index], num[i]

    return num


if __name__ == "__main__":
    num_list = [5, 6, 1, 8, 3, -8]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {selection_sort(num_list[:])}")  # Pass a copy to prevent modification
