# ------------------------------------------------------
# File: identical_binary_trees.py
# Date: 2025-02-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check if two binary trees are identical

class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, value):
        self.value = value  # Initialize node with given value
        self.left = None    # Left child reference
        self.right = None   # Right child reference


def are_identical(root1, root2):
    """
    Recursively checks if two binary trees are identical.
    
    Two trees are identical if:
    1. They have the same structure.
    2. Each corresponding node has the same value.

    Parameters:
    root1 (TreeNode): Root of the first tree.
    root2 (TreeNode): Root of the second tree.

    Returns:
    bool: True if both trees are identical, False otherwise.
    """
    
    # Base case: If both nodes are None, trees are identical
    if not root1 and not root2:
        return True
    
    # If one of them is None while the other isn't, trees are not identical
    if not root1 or not root2:
        return False
    
    # If values at the current nodes are different, trees are not identical
    if root1.value != root2.value:
        return False
    
    # Recursively check left and right subtrees
    return are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)


def preorder(root):
    """Returns a list representing the preorder traversal of the tree."""
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)


if __name__ == "__main__":
    # Constructing Tree 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    # Constructing Tree 2 (with one different node)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(6)  # Different value from root1.left.right

    # Print tree structures using preorder traversal
    print("\nTree 1 Preorder Traversal:", preorder(root1))
    print("Tree 2 Preorder Traversal:", preorder(root2))

    # Compare trees and print result
    if are_identical(root1, root2):
        print("Both trees are identical.")
    else:
        print("Trees are not identical.")
