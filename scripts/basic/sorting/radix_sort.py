# ------------------------------------------------------
# File: radix_sort.py
# Date: 2025-02-12
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Radix Sort to sort a list of non-negative integers

def radix_sort(num):
    """
    Radix Sort Implementation (For Non-Negative Integers)
    
    Time Complexity:
        - Best/Average/Worst Case: O(d * (n + 10)), where d = number of digits, n = array size, k = 10 (digit range)
    
    Space Complexity:
        - O(n) (Extra space for Counting Sort)
    
    This function sorts a list of non-negative integers using Radix Sort.
    It sorts numbers digit-by-digit using Counting Sort as a stable sorting method.
    """
    n = len(num)
    if n <= 1:
        return num  # Already sorted if 0 or 1 element.

    max_el = max(num)  # Find the max number to know the number of digits
    exp = 1  # Start sorting from the least significant digit

    while max_el // exp > 0:
        num = counting_sort(num, exp)  # Properly update num after sorting each digit
        exp *= 10  # Move to next significant digit

    return num  # Fully sorted list

def counting_sort(num, exp):
    """
    Counting Sort for Radix Sort (Sorts numbers based on a specific digit place).
    """
    n = len(num)
    count = [0] * 10  # Only 10 digits (0-9)
    sorted_num = [0] * n  # Output array

    # Count occurrences of each digit at the `exp` place
    for i in num:
        index = (i // exp) % 10  # Extract digit at `exp` place
        count[index] += 1

    # Compute cumulative count (prefix sum)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place elements in sorted order (Right to Left for stability)
    for i in range(n - 1, -1, -1):
        index = (num[i] // exp) % 10  # Extract digit again
        sorted_num[count[index] - 1] = num[i]
        count[index] -= 1  # Reduce count for duplicate handling

    return sorted_num  # Return sorted array for this digit

if __name__ == "__main__":
    num_list = [555, 89, 6, 0, 488, 102, 3, 45, 6]
    print(f"Original List: {num_list}")
    print(f"Sorted List  : {radix_sort(num_list[:])}")  # Ensures original list is not modified
