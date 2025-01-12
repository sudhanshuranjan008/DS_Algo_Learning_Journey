# ------------------------------------------------------
# File: contiguous_subarray_sum.py
# Date: 2025-01-12
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the sum of contiguous subarray with the maximum sum (Kadane’s Algorithm)

def max_sum_contiguous_subarray(arr: list) -> int:
    # Initialize max_sum to the smallest possible value and current_sum to 0
    max_sum = arr[0]
    current_sum = 0

    for num in arr:
        # Add the current number to the current sum
        current_sum += num

        # Update max_sum if current_sum exceeds max_sum
        max_sum = max(max_sum, current_sum)

        # Reset current_sum to 0 if it becomes negative
        if current_sum < 0:
            current_sum = 0
    
    return max_sum


if __name__ == "__main__":
    my_array = [-11, 2, 3, -4, 5]
    print(f"The sum of contiguous subarray with maximum sum is: {max_sum_contiguous_subarray(my_array)}")
