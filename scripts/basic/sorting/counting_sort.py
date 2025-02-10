# ------------------------------------------------------
# File: counting_sort.py
# Date: 2025-02-10
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Counting Sort for an array of non-negative integers

def counting_sort(num):
    """
    Counting Sort Implementation.
    
    Sorting Algorithm: Non-comparison-based, stable sorting.
    
    Time Complexity: 
        - Best/Average/Worst Case: O(n + k), where n is the number of elements, and k is the max value.
    Space Complexity: 
        - O(k) (Uses extra space for count array).
    
    Works best when the range of numbers (max value - min value) is small.
    """

    n = len(num)
    
    # Edge case: If list has 0 or 1 element, it is already sorted.
    if n <= 1:
        return num

    # Find the maximum element to determine count array size.
    max_el = max(num)

    # Initialize count array of size (max_el + 1) with zeros.
    count = [0] * (max_el + 1)

    # Count occurrences of each number in the input list.
    for i in num:
        count[i] += 1

    # Compute cumulative count to determine sorted positions.
    for i in range(1, max_el + 1):
        count[i] += count[i - 1]

    # Create output array for sorted elements.
    sorted_num = [0] * n

    # Place elements in the correct sorted position (right-to-left for stability).
    for i in range(n - 1, -1, -1):  
        sorted_num[count[num[i]] - 1] = num[i]
        count[num[i]] -= 1  # Reduce count for duplicate handling.

    return sorted_num

if __name__ == "__main__":
    num_list = [5, 9, 23, 45, 5, 2, 2, 23]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {counting_sort(num_list[:])}")  # Ensures original list is not modified.
