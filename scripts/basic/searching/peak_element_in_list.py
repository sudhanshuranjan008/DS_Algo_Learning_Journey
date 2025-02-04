# ------------------------------------------------------
# File: peak_element_in_list.py
# Date: 2025-02-04
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the peak element in a list

def peak_element(arr):
    N = len(arr)

    # Handle edge case: if there's only one element or first element is greater than or equal to second, it's a peak
    if N == 1 or arr[0] >= arr[1]:
        return arr[0]

    # Check if last element is a peak
    if arr[N-1] >= arr[N-2]:
        return arr[N-1]
     
    start = 1  # Start from the second element
    end = N-2  # End at the second last element

    while start <= end:
        mid = start + (end - start) // 2  # Find middle element
        
        # If mid is peak, return it
        if arr[mid-1] <= arr[mid] >= arr[mid+1]:
            return arr[mid]
        
        # If right neighbor is greater, move to the right half
        if arr[mid] < arr[mid+1]:
            start = mid + 1

        # Otherwise, move to the left half
        else:
            end = mid - 1

    return -1  # This should never happen if the input is valid

if __name__ == "__main__":
    num_list = [2, 6, 4, 5, 3]
    result = peak_element(num_list)
    print(f"The peak element in the list is: {result}")

    

