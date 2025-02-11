# ------------------------------------------------------
# File: bucket_sort.py
# Date: 2025-02-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Bucket Sort for an array of floating-point numbers

def bucket_sort(num):
    """
    Bucket Sort Implementation (Without Using Any Other Sorting Algorithm)
    
    Time Complexity:
        - Best/Average Case: O(n) (If elements distribute well across buckets)
        - Worst Case: O(n^2) (If all elements go into one bucket)
    
    Space Complexity: 
        - O(n) (Extra space for buckets)
    
    This function sorts a list of floating-point numbers using Bucket Sort 
    without explicitly using another sorting algorithm.
    """
    n = len(num)
    if n <= 1:
        return num  # Edge case: Already sorted if 0 or 1 element.

    # Create empty buckets
    buckets = [[] for _ in range(n)]

    # Distribute elements into buckets and insert in sorted order
    for i in num:
        k = min(n - 1, int(i * n))  # Ensure valid bucket index

        # Insert element into bucket in sorted order
        bucket = buckets[k]
        if not bucket or i >= bucket[-1]:  # If bucket is empty or `i` is largest, append
            bucket.append(i)
        else:
            # Find correct position to insert `i`
            j = len(bucket) - 1
            while j >= 0 and bucket[j] > i:
                j -= 1
            bucket.insert(j + 1, i)  # Insert at correct position

    # Merge sorted buckets back into original list
    index = 0
    for bucket in buckets:
        for i in bucket:
            num[index] = i
            index += 1

    return num

if __name__ == "__main__":
    num_list = [0.56, 0.23, 0.89, 0.23, 0.55, 0.74, 1.98, 1.03]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {bucket_sort(num_list[:])}")  # Ensures original list is not modified
