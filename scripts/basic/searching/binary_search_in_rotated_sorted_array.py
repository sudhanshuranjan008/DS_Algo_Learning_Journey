# ------------------------------------------------------
# File: binary_search_in_rotated_sorted_array.py
# Date: 2025-02-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Search for an element in a rotated sorted array

def rotated_array_search(arr, num):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2  # Find mid-point

        if arr[mid] == num:  # If mid is the target, return index
            return mid
        
        # Check if left half is sorted
        if arr[start] <= arr[mid]:  
            if arr[start] <= num < arr[mid]:  # If target lies in left half
                end = mid - 1  # Shift search to left
            else:
                start = mid + 1  # Otherwise, search in right half

        # Otherwise, right half is sorted
        else:
            if arr[mid] < num <= arr[end]:  # If target lies in right half
                start = mid + 1  # Shift search to right
            else:
                end = mid - 1  # Otherwise, search in left half

    return -1  # Target not found

if __name__ == "__main__":
    num_list = [45, 50, 30, 35, 40]

    while True:
        try:
            value = int(input("Enter the number to be searched: "))  # Take user input
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input! Please enter an integer.")  # Handle invalid input
    
    result = rotated_array_search(num_list, value)
    if result == -1:
        print(f"{value} is not present in the list.")  # Print if not found
    else:
        print(f"{value} is present in the list at index {result}")  # Print index if found

