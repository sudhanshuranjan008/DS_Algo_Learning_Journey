# ------------------------------------------------------
# File: bubble_sort.py
# Date: 2025-02-07
# Author: Sudhanshu Ranian
# ------------------------------------------------------

# Write a function to implement Bubble Sort and sort an array in ascending order

def bubble_sort(num):
    """
    Bubble Sort Implementation
    Time Complexity:
        - Best Case (Already Sorted): O(n)
        - Worst/Average Case: O(n^2)
    Space Complexity: O(1) (Sorts in place)
    
    This function sorts a list using the Bubble Sort algorithm.
    Note: This modifies the input list in place.
    """
    n = len(num)
    if not num:  # Check for an empty list
        return "List is empty. Nothing to sort."
    if n == 1:  # Single element is already sorted
        return num

    for pass_num in range(n - 1):  # Each pass places the next largest element at the end
        swapped = False
        for i in range(n - pass_num - 1):  # Compare adjacent elements up to the unsorted portion
            if num[i] > num[i + 1]:  # Swap if needed
                num[i], num[i + 1] = num[i + 1], num[i]
                swapped = True
        if not swapped:  # If no swaps, the list is already sorted
            break

    return num


if __name__ == "__main__":
    num_list = [-3, 4, -5, 2, 0, 8, 9, 3]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {bubble_sort(num_list[:])}")  # Pass a copy to prevent modification



