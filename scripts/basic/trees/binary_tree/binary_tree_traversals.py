# ------------------------------------------------------
# File: binary_tree_traversals.py
# Date: 2025-02-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Traversal Techniques for a Binary Tree (Preorder, Inorder, Postorder, Level Order)

from collections import deque  # Importing deque for efficient queue operations

class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, data):
        self.data = data  # Node value
        self.left = None  # Left child reference
        self.right = None  # Right child reference

def pre_order(node):
    """Preorder Traversal (Root → Left → Right)"""
    if node is None:  # Base condition for recursion
        return
    
    print(node.data, end=" ")  # Process (print) the root node first
    pre_order(node.left)  # Recursively traverse the left subtree
    pre_order(node.right)  # Recursively traverse the right subtree

def in_order(node):
    """Inorder Traversal (Left → Root → Right)"""
    if node is None:  # Base condition for recursion
        return
    
    in_order(node.left)  # Recursively traverse the left subtree
    print(node.data, end=" ")  # Process (print) the root node
    in_order(node.right)  # Recursively traverse the right subtree

def post_order(node):
    """Postorder Traversal (Left → Right → Root)"""
    if node is None:  # Base condition for recursion
        return
    
    post_order(node.left)  # Recursively traverse the left subtree
    post_order(node.right)  # Recursively traverse the right subtree
    print(node.data, end=" ")  # Process (print) the root node after its children

def level_order(root):
    """Level Order Traversal (Breadth-First Search using a queue)"""
    if not root:  # If tree is empty, return
        return

    queue = deque([root])  # Initialize queue with the root node
    
    while queue:  # Iterate until queue is empty
        node = queue.popleft()  # Dequeue the front node
        print(node.data, end=" ")  # Process (print) the node
        
        if node.left:  # If left child exists, enqueue it
            queue.append(node.left)
        if node.right:  # If right child exists, enqueue it
            queue.append(node.right)

if __name__ == "__main__":
    # Creating nodes
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    # Constructing the binary tree
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node7.left = node8  # Additional depth on the right subtree

    # Printing tree structure for reference
    print("\nTree Structure:")
    print(f"Root: {root.data}, Left: {root.left.data}, Right: {root.right.data}")
    print(f"2 -> Left: {node2.left.data}, Right: {node2.right.data}")
    print(f"3 -> Left: {node3.left.data}, Right: {node3.right.data}")
    print(f"7 -> Left: {node7.left.data}")  # Node 7 has an additional left child

    # Performing different tree traversals
    print("\nPreorder Traversal (Root → Left → Right):")
    pre_order(root)

    print("\n\nInorder Traversal (Left → Root → Right):")
    in_order(root)

    print("\n\nPostorder Traversal (Left → Right → Root):")
    post_order(root)

    print("\n\nLevel Order Traversal (Breadth-First Search):")
    level_order(root)

