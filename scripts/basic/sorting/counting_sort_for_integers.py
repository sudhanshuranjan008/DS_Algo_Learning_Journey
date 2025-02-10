# ------------------------------------------------------
# File: counting_sort_for_integers.py
# Date: 2025-02-10
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Counting Sort for an array of positive and negative integers both

def counting_sort(num):
    """
    Counting Sort Implementation for Sorting Integers (Handles Negative and Positive Integers).
    
    Time Complexity:
        - Best/Average/Worst Case: O(n + k), where n is the number of elements and k is the range of elements (max value - min value).
    Space Complexity:
        - O(k) (Extra space for count array)
    
    This function sorts a list using the Counting Sort algorithm.
    It works efficiently for sorting integers, including both negative and positive values.
    """

    n = len(num)
    if n <= 1:  # Edge case: If list has 0 or 1 element, return as is.
        return num
    
    # Find the minimum and maximum values to determine the range.
    min_el = min(num)
    max_el = max(num)

    # Calculate the range of elements to determine the size of the count array.
    range_of_elements = max_el - min_el + 1
    count = [0] * range_of_elements  # Initialize count array with zeros.

    # Count occurrences of each number, adjusting indices to handle negative numbers.
    for i in num:
        count[i - min_el] += 1  

    # Compute the cumulative count (prefix sum) to determine positions in the sorted array.
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    # Create an output array to store the sorted elements.
    sorted_num = [0] * n

    # Place elements in their correct sorted position (right-to-left for stability).
    for i in range(n - 1, -1, -1):
        sorted_num[count[num[i] - min_el] - 1] = num[i]
        count[num[i] - min_el] -= 1  # Decrease count for duplicate handling.

    return sorted_num

if __name__ == "__main__":
    num_list = [5, 9, 5, 2, 2, -3, -1, 0]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {counting_sort(num_list[:])}")  # Ensures original list is not modified
