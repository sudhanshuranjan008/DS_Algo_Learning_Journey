# ------------------------------------------------------
# File: binary_tree_intro.py
# Date: 2025-02-21
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Simple Binary Tree Implementation

class TreeNode:
    """Class to represent a node in a binary tree."""
    
    def __init__(self, value):
        """
        Initializes a tree node with a given value.
        Each node has:
        - A 'value' to store data.
        - A 'left' reference for the left child (initially None).
        - A 'right' reference for the right child (initially None).
        """
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    # Creating individual nodes of the binary tree
    root = TreeNode('R')  # Root node
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeX = TreeNode('X')
    nodeY = TreeNode('Y')
    nodeZ = TreeNode('Z')

    # Establishing parent-child relationships (forming the tree)
    root.left = nodeA   # A is the left child of root (R)
    root.right = nodeB  # B is the right child of root (R)

    nodeA.left = nodeC  # C is the left child of A
    nodeA.right = nodeD # D is the right child of A

    nodeB.left = nodeX  # X is the left child of B
    nodeB.right = nodeY # Y is the right child of B

    nodeY.left = nodeZ  # Z is the left child of Y (deeper level)

    # Printing values to verify tree structure
    print("Root Node:", root.value)  # Output: R
    print("Root Left:", root.left.value)  # Output: A
    print("Root Right:", root.right.value)  # Output: B

    print("A -> Left:", nodeA.left.value, "| Right:", nodeA.right.value)  # Output: C | D
    print("B -> Left:", nodeB.left.value, "| Right:", nodeB.right.value)  # Output: X | Y

    print("Y -> Left:", nodeY.left.value)  # Output: Z





