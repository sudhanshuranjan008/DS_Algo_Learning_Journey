# ------------------------------------------------------
# File: merge_sort.py
# Date: 2025-02-08
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Merge Sort to sort an array

def merge_sort(num): 
    """
    Merge Sort Implementation
    Time Complexity:
        - Best/Average/Worst Case: O(n log n) (Always divides in half)
    Space Complexity: O(n) (Temporary arrays for merging)

    This function sorts a list using the Merge Sort algorithm.
    """  
    # Base case: If list has 0 or 1 element, it’s already sorted.
    n = len(num)
    if n <= 1:
        return num
    
    # Find the middle index to divide the list.
    mid = n // 2

    # Recursively sort both halves of the list.
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])

    # Merge the sorted halves.
    return merge(left, right)

def merge(left, right):
    """Merge two sorted subarrays"""
    # Initialize two pointers for merging.
    i = j = 0
    merged_num = []

    # Compare elements from both lists and insert the smaller one.
    while i < len(left) and j < len(right):  
        if left[i] <= right[j]:  # Ensures stability of sorting.
            merged_num.append(left[i])
            i += 1
        else:
            merged_num.append(right[j])
            j += 1

    # If any elements are left in either list, add them to the result.
    return merged_num + left[i:] + right[j:]  # Concatenation instead of extend().

if __name__ == "__main__":
    num_list = [4, 3, 0, 8, -7, 11, 6]
    print(f"Original List: {num_list}")
    print(f"Sorted List  : {merge_sort(num_list[:])}")  # Pass a copy to prevent modification.

