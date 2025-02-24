# ------------------------------------------------------
# File: binary_tree_diameter.py
# Date: 2025-02-24
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the diameter (longest path in edges) of a given binary tree

class TreeNode:
    def __init__(self, data):
        self.data = data  # Store node value
        self.left = None  # Left child reference
        self.right = None  # Right child reference

def find_diameter(root):
    """Returns the diameter (longest path in edges) of the tree."""

    def height(node):
        """Recursive function to calculate height and update diameter."""
        
        nonlocal diameter  # Access global diameter variable
        if node is None:
            return -1  # No edges in an empty subtree
        
        # Recursively find the height of left and right subtrees
        left_height = height(node.left)
        right_height = height(node.right)

        # Update diameter: longest path between two nodes passes through root
        diameter = max(diameter, left_height + right_height + 2)

        # Height of current node = max(left, right) + 1 (counting edges)
        return max(left_height, right_height) + 1
    
    diameter = 0  # Initialize diameter to track the longest path
    height(root)  # Start recursion from root
    return diameter  # Final diameter value


if __name__ == "__main__":
    # Creating tree nodes
    root = TreeNode('R')
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    # Constructing the binary tree
    root.left = nodeA
    root.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeC.left = nodeG  # Deepest node in the left subtree

    # Printing tree structure for reference
    print("Root: ", root.data)
    print("R -> Left:", root.left.data, "| Right:", root.right.data)
    print("A -> Left:", nodeA.left.data, "| Right:", nodeA.right.data)
    print("B -> Left:", nodeB.left.data, "| Right:", nodeB.right.data)
    print("C -> Left:", nodeC.left.data, "| Right:", nodeC.right.data if nodeC.right else "None")

    # Calculate and print the tree diameter
    print(f"Diameter of the Binary Tree is: {find_diameter(root)}")
