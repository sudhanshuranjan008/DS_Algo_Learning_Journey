# ------------------------------------------------------
# File: bst_validation.py
# Date: 2025-03-04
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to validate if a Tree is a Binary Search Tree

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

# Get the minimum value in BST
def get_min(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.data

# Get the maximum value in BST
def get_max(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.data

# BST validation using min-max range
def is_BST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True  # Empty tree is a BST

    if not (min_val < root.data < max_val):
        return False  # If node value is out of valid range, it's not a BST

    # Recursively check left subtree (should be within min_val and root.data)
    # Recursively check right subtree (should be within root.data and max_val)
    return is_BST(root.left, min_val, root.data) and is_BST(root.right, root.data, max_val)

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

    # Check if the tree is a BST
    if is_BST(root):
        print("It's a BST!")
    else:
        print("It's not a BST!")
