# ------------------------------------------------------
# File: bucket_sort_for_integers.py
# Date: 2025-02-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Bucket Sort for an array of floating-point integers(positive and negative both)

def bucket_sort(num):
    """
    Bucket Sort Implementation for Handling Negative & Positive Integers.
    
    Time Complexity:
        - Best/Average Case: O(n + k log k) (Where k = elements per bucket)
        - Worst Case: O(n^2) (If all elements go into one bucket)
    
    Space Complexity: 
        - O(n) (Extra space for buckets)
    
    This function sorts a list of floating-point numbers using the Bucket Sort algorithm.
    It adjusts for negative numbers and scales values into buckets.
    """
    n = len(num)
    if n <= 1:
        return num  # Edge case: Already sorted if 0 or 1 element.

    # Create empty buckets
    buckets = [[] for _ in range(n)]

    # Find the minimum and maximum values
    min_el, max_el = min(num), max(num)
    range_of_elements = max_el - min_el + 1  # Total range of values

    # Distribute elements into buckets using scaled index mapping
    for i in num:
        k = int((i - min_el) * (n - 1) // range_of_elements)  # Ensures valid bucket index
        buckets[k].append(i)

    # Sort each bucket individually
    for bucket in buckets:
        if bucket:  # Skip empty buckets
            bucket.sort()

    # Merge sorted buckets back into original list
    index = 0
    for bucket in buckets:
        if bucket:
            for i in bucket:
                num[index] = i
                index += 1

    return num

if __name__ == "__main__":
    num_list = [0.56, 0.23, -0.89, 0.23, -0.55, 0.74, 1.98, 1.03]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {bucket_sort(num_list[:])}")  # Ensures original list is not modified

