# ------------------------------------------------------
# File: binary_tree_mirror_image.py
# Date: 2025-02-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find Mirror Image of a given Binary Tree

from collections import deque

class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child node
        self.right = None  # Right child node

def level_order(root):
    """Level Order Traversal (Breadth-First Search using a queue)"""
    
    if not root:
        return  # If tree is empty, return

    queue = deque([root])  # Initialize queue with root
    
    while queue:
        node = queue.popleft()  # Dequeue front node
        print(node.data, end=" ")  # Print node data
        
        if node.left:
            queue.append(node.left)  # Enqueue left child
        if node.right:
            queue.append(node.right)  # Enqueue right child

def find_mirror(root):
    """Recursively swaps left and right subtrees to create a mirror image."""
    
    if root is None:
        return  # Base case: if node is None, return
    
    find_mirror(root.left)  # Recur for left subtree
    find_mirror(root.right)  # Recur for right subtree

    root.left, root.right = root.right, root.left  # Swap left and right subtrees
    return root  # Return root for clarity

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
    node7.left = node8

    print("\nLevel Order Traversal of Binary Tree:")
    level_order(root)  # Print original tree level order

    find_mirror(root)  # Convert tree to its mirror image

    print("\nLevel Order Traversal of Mirror Image of Binary Tree:")
    level_order(root)  # Print mirrored tree level order
