# ------------------------------------------------------
# File: binary_search.py
# Date: 2025-02-02
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Binary Search

def binary_search(num_list, num):
    # Sort the list before performing binary search
    sorted_num_list = sorted(num_list)
    
    # Initialize start and end pointers for the search range
    start = 0
    end = len(sorted_num_list) - 1  

    # Perform the binary search loop
    while start <= end:
        # Find the middle index of the current range
        mid_index = start + (end - start) // 2

        # Check if the middle element is the number we are looking for
        if num == sorted_num_list[mid_index]:
            return True  # Return True if the number is found

        # If the number is larger, narrow the search to the right half
        elif num > sorted_num_list[mid_index]:
            start = mid_index + 1  # Update the start pointer to search the right half
        else:
            end = mid_index - 1  # Update the end pointer to search the left half

    return False  # Return False if the number is not found after searching

if __name__ == "__main__":
    # Example list to search in
    input_list = [5, 45, 63, 2, 13]

    # Try to take the user's input as an integer
    try:
        find_num = int(input("Enter the number to be searched: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")  # Handle invalid input
        exit()

    # Call binary_search function and print the result
    if binary_search(input_list, find_num):
        print(f"{find_num} is present in the list.")  # If number found
    else:
        print(f"{find_num} is not present in the list.")  # If number not found



