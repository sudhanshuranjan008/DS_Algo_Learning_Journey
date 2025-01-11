# ------------------------------------------------------
# File: array_rotation.py
# Date: 2025-01-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Rotate an array by K positions to the right
def rotate_array(arr: list, K: int) -> list:
    if not arr:
        return []  # Handle empty array case

    n = len(arr)
    K %= n  # Adjust K to be within the array length
    
    # Perform K rotations
    for _ in range(K):
        # Store the last element
        last = arr[n - 1]

        # Shift elements to the right
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]

        # Place the last element at the first position
        arr[0] = last

    return arr


if __name__ == "__main__":
    # Input array
    my_array = [1, 2, 3, 4, 5]

    # Number of positions to rotate
    K = 2

    # Rotate and print the result
    rotated_array = rotate_array(my_array, K)
    print(f"Original array after {K} rotations: {rotated_array}")

