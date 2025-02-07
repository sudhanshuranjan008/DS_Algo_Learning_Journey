# ------------------------------------------------------
# File: insertion_sort.py
# Date: 2025-02-07
# Author: Sudhanshu Ranian
# ------------------------------------------------------

# Implement Insertion Sort and sort an array in ascending order

def insertion_sort(num):
    """
    Insertion Sort Implementation
    Time Complexity:
        - Best Case (Already Sorted): O(n) (Only comparisons, no swaps)
        - Worst/Average Case: O(n^2) (Nested loops)
    Space Complexity: O(1) (Sorts in place)

    This function sorts a list using the Insertion Sort algorithm.
    Note: This modifies the input list in place.
    """
    if not num:  # Check for an empty list
        return "List is empty. Nothing to sort."
    
    n = len(num)
    if n == 1:  # Single element is already sorted
        return num

    for i in range(1, n):  # Start from the second element
        key = num[i]  # Element to be inserted
        j = i - 1

        # Shift elements to the right to make space for key
        while j >= 0 and num[j] > key:
            num[j + 1] = num[j]
            j -= 1

        # Insert the key at its correct position
        num[j + 1] = key

    return num


if __name__ == "__main__":
    num_list = [4, 5, 8, -7, 0, 1, 6]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {insertion_sort(num_list[:])}")  # Pass a copy to prevent modification
