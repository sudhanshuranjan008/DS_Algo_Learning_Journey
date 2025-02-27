# ------------------------------------------------------
# File: zig_zag_traversal.py
# Date: 2025-02-27
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Zig-Zag Level Order Traversal in a Binary Tree

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

def zigzag_level_order(root):
    """
    Returns the zig-zag level order traversal of a binary tree.
    
    Parameters:
    root (TreeNode): Root of the binary tree.
    
    Returns:
    list: Zig-zag level order traversal.
    """
    if root is None:
        return []

    ans = []  # Stores final zig-zag order traversal
    queue = deque([root])  # Queue for level-order traversal
    left_to_right = True  # Direction flag (left-to-right or right-to-left)

    while queue:
        level_size = len(queue)  # Number of nodes at current level
        level_values = deque()  # Stores values for the current level

        for _ in range(level_size):
            node = queue.popleft()  # Get the next node from queue

            # Append value based on current direction
            if left_to_right:
                level_values.append(node.value)  # Append normally
            else:
                level_values.appendleft(node.value)  # Append at front for reverse order

            # Enqueue child nodes for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        ans.extend(level_values)  # Add processed level values to final result
        left_to_right = not left_to_right  # Toggle direction for next level

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

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeC.left = nodeG

    # Printing traversal outputs
    print(f"Preorder Traversal of tree is: {preorder(root)}")
    print(f"Zig Zag Order Traversal is: {zigzag_level_order(root)}")
