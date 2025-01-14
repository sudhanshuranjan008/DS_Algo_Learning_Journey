# ------------------------------------------------------
# File: string_compression.py
# Date: 2025-01-14
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement string compression (e.g., "aaabb" → "a3b2")

def compress_string(my_string: str):
    # Initialize the result string and a counter
    new_string = ''
    count = 1

    # Iterate through the string starting from the second character
    for i in range(1, len(my_string)):
        # Compare the current character with the previous one
        if my_string[i] == my_string[i - 1]:
            count += 1  # Increment the count if the characters are the same
        else:
            # Append the character and its count to the new string
            new_string += my_string[i - 1] + str(count)
            count = 1  # Reset count for the new character

    # After the loop, add the last character and its count
    new_string += my_string[-1] + str(count)

    # Return the compressed string
    return new_string


if __name__ == "__main__":
    # Input the string to compress it
    input_string = 'success'

    # Print the result
    print(f"The original string is: {input_string}")
    print(f"The compressed string is: {compress_string(input_string)}")
