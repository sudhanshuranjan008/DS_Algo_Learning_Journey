# ------------------------------------------------------
# File: floor_and_ceil_in_bst.py
# Date: 2025-03-06
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find Floor & Ceil of a number in Binary Search Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child pointer
        self.right = None  # Right child pointer

# Inorder traversal (Left -> Root -> Right) to display BST in sorted order
def inorder(root):
    return [] if not root else inorder(root.left) + [root.data] + inorder(root.right)

# Insert a node into BST
def insert(root, value):
    if not root:
        return TreeNode(value)  # Create new node if root is None
    
    if root.data > value:
        root.left = insert(root.left, value)  # Insert in left subtree if value is smaller
    else:
        root.right = insert(root.right, value)  # Insert in right subtree if value is greater

    return root  # Return updated root

# Function to find the floor of a given value in BST
def floor(root, value):
    if root is None:
        return None  # No floor exists if BST is empty
    
    if root.data == value:
        return root.data  # Exact match, floor is the value itself
    
    elif root.data > value:
        return floor(root.left, value)  # Search left for a smaller value
    
    else:
        # Store potential floor and check if a larger valid floor exists in right subtree
        right_floor = floor(root.right, value)
        return right_floor if right_floor is not None else root.data

# Function to find the ceil of a given value in BST
def ceil(root, value):
    if root is None:
        return None  # No ceil exists if BST is empty
    
    if root.data == value:
        return root.data  # Exact match, ceil is the value itself
    
    elif root.data < value:
        return ceil(root.right, value)  # Search right for a larger value
    
    else:
        # Store potential ceil and check if a smaller valid ceil exists in left subtree
        left_ceil = ceil(root.left, value)
        return left_ceil if left_ceil is not None else root.data


if __name__ == "__main__":
    # Construct BST
    root = None
    root = insert(root, 25)
    root = insert(root, 20)
    root = insert(root, 35)
    root = insert(root, 17)
    root = insert(root, 24)
    root = insert(root, 34)
    root = insert(root, 40)

    # Display BST in sorted order (inorder traversal)
    print(f"Inorder Traversal of BST after insertion: {inorder(root)}")

    # Take user input to find floor and ceil
    num = int(input("Enter the number to find its floor and ceil value: "))
    print(f"The floor value of {num} is {floor(root, num)}")
    print(f"The ceil value of {num} is {ceil(root, num)}")
