# ------------------------------------------------------
# File: square_root_using_binary_search.py
# Date: 2025-02-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the square root of a number using Binary Search

def square_root(num, precision=3):
    # Check for negative numbers and raise an error
    if num < 0:
        raise ValueError("Invalid input! Square of any number is always positive.")
    
    # Edge cases: return num directly for 0 and 1
    if num == 0 or num == 1:
        return num
    
    # Initialize binary search range
    start = 0
    end = num
    answer = 0  # This will hold the integer part of the square root
    
    # Perform binary search to find the integer part of the square root
    while start <= end:
        mid = start + (end - start) // 2  # Calculate middle point

        if mid**2 == num:  # Perfect match, return mid
            return mid
        elif mid**2 < num:  # If mid squared is less, search right half
            answer = mid  # Update answer to mid
            start = mid + 1
        else:  # If mid squared is greater, search left half
            end = mid - 1
    
    # Refining the result with decimals
    increment = 0.1  # Start with 0.1 increment
    for _ in range(precision):  # Loop for the desired precision
        while answer**2 <= num:  # Keep increasing answer until it's too big
            answer += increment
        answer -= increment  # Step back to last valid value
        increment /= 10  # Reduce increment to refine further
    
    # Return the rounded result
    return round(answer, precision)

if __name__ == "__main__":
    # Loop until valid integer input is entered
    while True:
        try:
            number = int(input("Enter the number to find its square root: "))
            break  # Exit loop if valid input is provided
        except ValueError:
            print("Invalid input! Please enter a valid integer.")  # If invalid input, prompt again
    
    try:   
        # Call the square_root function and display the result
        result = square_root(number)
        print(f"Square root of {number} is {result}")  # Print the result
    except ValueError as e:
        # Display any errors (e.g., negative numbers)
        print(e)
