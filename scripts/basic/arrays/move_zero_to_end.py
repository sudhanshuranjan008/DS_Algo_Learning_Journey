# ------------------------------------------------------
# File: move_zero_to_end.py
# Date: 2025-01-08
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Move all zeroes to the end of the array

# Function to move all zeroes to the end of the array
def move_zero(arr:list) -> list:
    count = 0  # This will track the position to place the non-zero element
    
    # Iterate through the array
    for i in range(len(arr)):
        # If the current element is not zero
        if arr[i] != 0:
            # Swap the non-zero element with the element at 'count' position
            arr[i], arr[count] = arr[count], arr[i]
            count += 1  # Increment 'count' to move it to the next position

    # Return the updated array with all zeros at the end
    return arr

# Driver code to test the function
if __name__ =="__main__":
    # Test array with zeros scattered in between
    my_array = [65, 5, 0, 0, 23, 0, 11, 0, 8]
    # Calling the function and storing the result
    result = move_zero(my_array)
    # Printing the result
    print(result)
