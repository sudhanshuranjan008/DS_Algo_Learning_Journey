# ------------------------------------------------------
# File: binary_tree_height_and_depth.py
# Date: 2025-02-24
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement functions to find the height and depth of a given binary tree.
# - Height is the longest path from the root to a leaf, measured in edge count.
# - Depth is the distance from the root to a given node, also measured in edge count.

class TreeNode:
    """Class representing a node in a binary tree."""
    
    def __init__(self, data):
        self.data = data  # Store node value
        self.left = None  # Pointer to left child
        self.right = None  # Pointer to right child

def find_height(node):
    """
    Returns the height of the binary tree in terms of edge count.
    Change base case to return 0 instead of -1 if node count is required.
    """
    
    if node is None:  # Base case: empty tree has height -1 (edge count)
        return -1
    
    # Recursively find the height of left and right subtrees
    left_height = find_height(node.left)
    right_height = find_height(node.right)

    # The height of the current node is max of left and right subtree heights + 1
    return max(left_height, right_height) + 1

def find_depth(node, value):
    """
    Returns the depth (edge count) of a given value in the binary tree.
    If the value is not found, returns -1.
    """

    if node is None:  # Base case: node not found
        return -1

    if node.data == value:  # If the current node matches the value, depth is 0
        return 0
    
    # Recursively search in the left subtree
    left_depth = find_depth(node.left, value)
    if left_depth >= 0:
        return left_depth + 1  # Add 1 for the edge to the parent
    
    # Recursively search in the right subtree
    right_depth = find_depth(node.right, value)
    if right_depth >= 0:
        return right_depth + 1  # Add 1 for the edge to the parent
    
    return -1  # Value not found in either subtree

if __name__ == "__main__":
    # Constructing the binary tree
    root = TreeNode('R')
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    # Connecting nodes to form the tree
    root.left = nodeA
    root.right = nodeB
    nodeA.left = nodeC
    nodeA.right = nodeD
    nodeB.left = nodeE
    nodeB.right = nodeF
    nodeC.left = nodeG

    # Printing tree structure for reference
    print("Root: ", root.data)
    print("R -> Left:", root.left.data, "| Right:", root.right.data)
    print("A -> Left:", nodeA.left.data, "| Right:", nodeA.right.data)
    print("B -> Left:", nodeB.left.data, "| Right:", nodeB.right.data)
    print("C -> Left:", nodeC.left.data, "| Right:", nodeC.right.data if nodeC.right else "None")

    # Finding and printing the height of the tree
    print(f"The height (edge-count) of the Binary Tree is: {find_height(root)}")

    # Finding and printing the depth of node 'D'
    depth_D = find_depth(root, 'D')
    print(f"The depth of 'D' in Binary Tree is: {depth_D}" if depth_D != -1 else "Value Not Found!")




