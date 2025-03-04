# ------------------------------------------------------
# File: min_max_in_bst.py
# Date: 2025-03-04
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the minimum and maximum values in a Binary Search Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child pointer
        self.right = None  # Right child pointer

# Inorder traversal (Left -> Root -> Right)
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

# Find the minimum value in BST
def get_min(root):
    if not root:
        return None  # If tree is empty, return None
    while root.left:  # Keep moving left to find the smallest value
        root = root.left
    return root.data  # Leftmost node holds the min value

# Find the maximum value in BST
def get_max(root):
    if not root:
        return None  # If tree is empty, return None
    while root.right:  # Keep moving right to find the largest value
        root = root.right
    return root.data  # Rightmost node holds the max value

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

    # Display BST in sorted order(inorder traversal)
    print(f"Inorder Traversal of BST after insertion: {inorder(root)}")

    # Print the min and max of the BST
    print(f"Minimum value in the tree is: {get_min(root)}")
    print(f"Maximum value in the tree is: {get_max(root)}")
