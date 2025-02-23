# ------------------------------------------------------
# File: binary_tree_using_array.py
# Date: 2025-02-23
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Binary Tree using an Array Representation

# Function to get the index of the left child in an array-based binary tree
def left_child_index(index):
    return 2 * index + 1  # Formula for left child in a zero-based index array

# Function to get the index of the right child in an array-based binary tree
def right_child_index(index):
    return 2 * index + 2  # Formula for right child in a zero-based index array

# Function to retrieve the value of a node at a given index
def get_bt_data(bt_array, index):
    if 0 <= index < len(bt_array):  # Ensure index is within the valid range
        return bt_array[index]  # Return the node value
    
    return None  # Return None if index is out of bounds

# Function to perform Pre-order Traversal (Root -> Left -> Right)
def pre_order(bt_array, index):
    if index >= len(bt_array) or bt_array[index] is None:  # Base condition: Check if index is out of bounds or node is missing
        return []
    return [bt_array[index]] + pre_order(bt_array, left_child_index(index)) + pre_order(bt_array, right_child_index(index))

# Function to perform In-order Traversal (Left -> Root -> Right)
def in_order(bt_array, index):
    if index >= len(bt_array) or bt_array[index] is None:  # Base condition: Check if index is out of bounds or node is missing
        return []
    return in_order(bt_array, left_child_index(index)) + [bt_array[index]] + in_order(bt_array, right_child_index(index))

# Function to perform Post-order Traversal (Left -> Right -> Root)
def post_order(bt_array, index):
    if index >= len(bt_array) or bt_array[index] is None:  # Base condition: Check if index is out of bounds or node is missing
        return []
    return post_order(bt_array, left_child_index(index)) + post_order(bt_array, right_child_index(index)) + [bt_array[index]]

# Driver Code
if __name__ == "__main__":
    # Binary Tree represented as an array (Complete Binary Tree with some missing nodes)
    bt_array = [1, 2, 3, 4, 5, 6, 7, 8, None, None]

    if not bt_array:  # Check if the tree is empty
        print("The binary tree is empty.")
    else:
        print("\nTree Structure:")
        for i in range(len(bt_array)):  # Iterating through the array representation of the tree
            if bt_array[i] is not None:  # Ignore missing nodes
                left_child = get_bt_data(bt_array, left_child_index(i))  # Get left child
                right_child = get_bt_data(bt_array, right_child_index(i))  # Get right child
                print(f"Node {bt_array[i]} -> Left: {left_child}, Right: {right_child}")  # Display node and its children

        # Print different tree traversals
        print("Pre-order Traversal:", pre_order(bt_array, 0))
        print("In-order Traversal:", in_order(bt_array, 0))
        print("Post-order Traversal:", post_order(bt_array, 0))

