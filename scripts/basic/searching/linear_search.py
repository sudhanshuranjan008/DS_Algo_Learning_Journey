# ------------------------------------------------------
# File: linear_search.py
# Date: 2025-02-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Linear Search

def linear_search(num_list, num):
    # Loop through each element of the list
    for i, val in enumerate(num_list):
        # If the element matches the number, return its index
        if val == num:
            return i
    # If the number is not found, return None
    return None

if __name__ == "__main__":
    # Example list to search in
    my_list = [4, 5, 89, 23, 47]

    try:
        # Take input from the user and convert it to an integer
        input_num = int(input("Enter the number to be searched: "))
    except ValueError:
        # If user enters a non-integer value, print an error message and exit
        print("Invalid input! Please enter an integer.")
        exit()

    # Call the linear_search function to get the index of the input number
    index = linear_search(my_list, input_num)

    # If the number is found, print its index, otherwise, print a not-found message
    if index is not None:
        print(f"Found {input_num} in list at index {index}")
    else:
        print(f"{input_num} is not present in the list.")


