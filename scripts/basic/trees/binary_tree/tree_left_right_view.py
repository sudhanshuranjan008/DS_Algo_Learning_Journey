# ------------------------------------------------------
# File: tree_left_right_view.py
# Date: 2025-02-28
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Left & Right View of a given Binary Tree

from collections import deque

class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None  # Pointer to left child
        self.right = None  # Pointer to right child

def preorder(root):
    """Returns a list representing the preorder traversal of the tree."""
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)

def left_view(root):
    """
    Returns the left view of a binary tree.

    Parameters:
    root (TreeNode): Root of the binary tree.

    Returns:
    list: Left view of the tree.
    """
    if root is None:
        return []

    ans = []  # Stores final left view traversal
    queue = deque([root])  # Queue for level-order traversal

    while queue:
        level_size = len(queue)  # Number of nodes at current level

        for i in range(level_size):
            node = queue.popleft()  # Get the next node from queue

            # Capture the first node at each level (leftmost node)
            if i == 0:
                ans.append(node.value)

            # Enqueue child nodes for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

def right_view(root):
    """
    Returns the right view of a binary tree.

    Parameters:
    root (TreeNode): Root of the binary tree.

    Returns:
    list: Right view of the tree.
    """
    if root is None:
        return []

    ans = []  # Stores final right view traversal
    queue = deque([root])  # Queue for level-order traversal

    while queue:
        level_size = len(queue)  # Number of nodes at current level

        for i in range(level_size):
            node = queue.popleft()  # Get the next node from queue

            # Capture the last node at the current level (rightmost node)
            if i == level_size - 1:
                ans.append(node.value)

            # Enqueue left child first, then right (ensuring rightmost nodes are last)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

if __name__ == "__main__":
    # Creating nodes
    root = TreeNode('R')
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    # Building the tree structure
    root.left = nodeA
    root.right = nodeB

    nodeB.left = nodeC
    nodeB.right = nodeD

    nodeC.right = nodeE

    nodeE.left = nodeF
    nodeE.right = nodeG

    # Printing traversal outputs
    print(f"Preorder Traversal of the tree is: {preorder(root)}")
    print(f"Left view of the tree is: {left_view(root)}")
    print(f"Right view of the tree is: {right_view(root)}")
