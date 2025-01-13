# ------------------------------------------------------
# File: string_word_reversal.py
# Date: 2025-01-13
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Reverse words in a given string

# Function to reverse the order of words in a given string
def reverse_words(my_string: str):
    # Split the input string into a list of words
    split_string = my_string.split()
    
    # Calculate the total number of words in the string
    N = len(split_string)

    # Loop to reverse the list of words in place using a two-pointer approach
    for i in range(0, N // 2):
        # Swap the words at the ith position and the (N-i-1)th position
        split_string[i], split_string[N-i-1] = split_string[N-i-1], split_string[i]

    # Join the reversed list of words into a single string
    result = ' '.join(split_string)
    
    # Return the reversed string
    return result

if __name__ == "__main__":
    # Define the input string to be reversed
    input_string = "Learn python in a good way"
    
    # Print the original string
    print(f"The original string is: \n {input_string}")
    print()
    
    # Call the function and print the reversed string
    print(f"The string reversed by words is: \n {reverse_words(input_string)}")

