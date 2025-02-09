# ------------------------------------------------------
# File: quick_sort.py
# Date: 2025-02-09
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Quick Sort to sort an array using the last element as the pivot.

def quick_sort(num):
    """
    Quick Sort Implementation (Not In-Place)
    Time Complexity:
        - Best/Average Case: O(n log n) (Balanced partitioning)
        - Worst Case: O(n^2) (When pivot is always the largest/smallest)
    Space Complexity: O(n) (Creates new lists for partitioning)

    This function sorts a list using the Quick Sort algorithm.
    """
    # Base case: If list has 0 or 1 element, it's already sorted.
    if len(num) <= 1:
        return num
    
    # Choosing the last element as pivot.
    pivot = len(num)-1

    # Partitioning: Elements < pivot, == pivot, and > pivot.
    left = [x for x in num if x < num[pivot]]    # Elements smaller than pivot.
    equal = [x for x in num if x == num[pivot]]  # All occurrences of pivot.
    right = [x for x in num if x > num[pivot]]   # Elements greater than pivot.

    # Combining sorted parts.
    return quick_sort(left) + equal + quick_sort(right)

if __name__ == "__main__":
    num_list = [4, 5, 8, 3, 0, 5, 2, -8, 5]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {quick_sort(num_list[:])}")  # Ensures original list is not modified.



