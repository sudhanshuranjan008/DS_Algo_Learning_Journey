# ------------------------------------------------------
# File: bst_Kth_min_max.py
# Date: 2025-03-05
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find Kth Smallest & Kth Largest element in a Binary Search Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child pointer
        self.right = None  # Right child pointer

# Insert a node into BST
def insert(root, value):
    if not root:
        return TreeNode(value)  # Create new node if root is None
    
    if root.data > value:
        root.left = insert(root.left, value)  # Insert in left subtree if value is smaller
    else:
        root.right = insert(root.right, value)  # Insert in right subtree if value is greater

    return root  # Return updated root

# Approach 1: Get Kth Smallest using Inorder Traversal (Left -> Root -> Right)
def get_kth_min(root, k):
    count = 0  # Counter to track the number of nodes visited
    result = None  # To store the kth smallest value

    def inorder_traversal(node):
        nonlocal count, result  # To modify outer variables inside recursion
        if not node or result is not None:
            return  # Stop if node is None or kth smallest is already found
        
        inorder_traversal(node.left)  # Traverse left subtree first (smallest values first)

        count += 1  # Increment count when visiting a node
        if count == k:  
            result = node.data  # Found the kth smallest, store it
            return

        inorder_traversal(node.right)  # Traverse right subtree

    inorder_traversal(root)
    return result

# Approach 2: Get Kth Largest using Reverse Inorder Traversal (Right -> Root -> Left)
def kth_largest_util(root, k, counter):
    if not root:
        return None
    
    # Search in right subtree first (since larger values are on the right)
    right = kth_largest_util(root.right, k, counter)
    if right is not None:
        return right  # If kth largest found in right subtree, return it
    
    # Increment counter
    counter[0] += 1
    if counter[0] == k:
        return root.data  # Found the kth largest, return it
    
    # Search in left subtree (for remaining nodes)
    return kth_largest_util(root.left, k, counter)

# Wrapper function to handle mutable counter for kth largest
def get_kth_max(root, k):
    counter = [0]  # Use a list to keep counter mutable across recursive calls
    return kth_largest_util(root, k, counter)

# Driver code to test the functions
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

    pos = int(input("Enter the position of maxima and minima: "))

    print(f"Kth maximum for K={pos} is: {get_kth_max(root, pos)}")
    print(f"Kth minimum for K={pos} is: {get_kth_min(root, pos)}")
