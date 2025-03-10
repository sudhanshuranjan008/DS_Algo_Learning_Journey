# ------------------------------------------------------
# File: heap_sort_using_heapq.py
# Date: 2025-03-10
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Sort an array using heap and heapq module

import heapq  # Importing heapq for heap operations

def heap_sort(arr):
    """
    Sorts an array using heap sort.

    This function first heapifies the array to create a min-heap, 
    then extracts elements one by one in sorted order.

    Parameters:
    arr (list): List of elements to be sorted.

    Returns:
    list: Sorted list in ascending order.
    """
    n = len(arr)
    if n < 2:  # No sorting needed for an empty or single-element array
        return arr  
    
    sorted_arr = []  # Store sorted elements
    
    heapq.heapify(arr)  # Convert list into a min-heap in-place
    for _ in range(n):  
        sorted_arr.append(heapq.heappop(arr))  # Pop elements in sorted order and append

    return sorted_arr  # Return the sorted list

if __name__ == "__main__":
    nums = [11, 13, 7, 5, 56, 67]  # Sample input array
    print(f"Original array: {nums}")
    print(f"Sorted array  : {heap_sort(nums[:])} ")  # Sort the array by passing a duplicate and print

