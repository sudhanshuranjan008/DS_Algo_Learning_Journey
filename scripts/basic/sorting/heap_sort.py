# ------------------------------------------------------
# File: heap_sort.py
# Date: 2025-03-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Heap Sort using a max heap to sort an array in ascending order

def heapify(arr, size, index):
    """Ensures the subtree rooted at 'index' follows the max-heap property."""

    root = index  # Assume current index is the largest
    lchild_index = 2 * index + 1  # Left child index
    rchild_index = 2 * index + 2  # Right child index

    # Compare left child with root
    if lchild_index < size and arr[root] < arr[lchild_index]:
        root = lchild_index

    # Compare right child with the current largest
    if rchild_index < size and arr[root] < arr[rchild_index]:
        root = rchild_index

    # If root is not the largest, swap and continue heapifying
    if root != index:
        arr[index], arr[root] = arr[root], arr[index]  # Swap
        heapify(arr, size, root)  # Heapify the affected subtree

def heap_sort(arr):
    """Performs heap sort using a max heap to sort the array in ascending order."""

    size = len(arr)
    if size < 2:  # No sorting needed for an empty or single-element array
        return arr
    
    # Step 1: Build a max heap
    for i in range((size // 2) - 1, -1, -1):  # Start from last non-leaf node
        heapify(arr, size, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move the max element to its correct position
        heapify(arr, i, 0)  # Restore heap property for the reduced heap
    
    return arr  # Sorted array

if __name__ == "__main__":
    # Driver code to test heap sort
    nums = [45, 12, 19, 34, 88, 3]
    print(f"Original array: {nums}")
    # Sorting and displaying result
    print(f"Sorted array  : {heap_sort(nums[:])}")  # Using slicing to preserve original list

