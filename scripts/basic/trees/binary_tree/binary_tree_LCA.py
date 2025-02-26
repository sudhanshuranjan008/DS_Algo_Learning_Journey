# ------------------------------------------------------
# File: binary_tree_LCA.py
# Date: 2025-02-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find Lowest Common Ancestor (LCA) of nodes in a Binary Tree

class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    """Returns a list representing the preorder traversal of the tree."""
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)

def lca(root: TreeNode, num1: int, num2: int) -> TreeNode:
    """
    Finds the Lowest Common Ancestor (LCA) of two given nodes in a Binary Tree.
    
    The LCA is the deepest node that has both num1 and num2 as descendants.
    
    Parameters:
    root (TreeNode): Root of the binary tree.
    num1 (int): First node value.
    num2 (int): Second node value.
    
    Returns:
    TreeNode: The LCA node if both values exist, else None.
    """
    if root is None:
        return None  # Base case: if tree is empty or reached a leaf

    if root.value == num1 or root.value == num2:
        return root  # If either num1 or num2 is found, return current node
    
    # Recursively check left and right subtrees
    left_lca = lca(root.left, num1, num2)
    right_lca = lca(root.right, num1, num2)

    if left_lca and right_lca:
        return root  # If both sides return a node, this is the LCA
    
    return left_lca if left_lca else right_lca  # Otherwise, return the non-null result

if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    # Constructing tree structure
    root.left = node2
    root.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    node4.left = node8

    # Preorder traversal output
    print("Binary Tree Preorder Traversal: ", preorder(root))

    # Test cases
    print(f"LCA of 4 and 5: {lca(root, 4, 5).value}")  # Expected: 2
    print(f"LCA of 6 and 7: {lca(root, 6, 7).value}")  # Expected: 3
    print(f"LCA of 4 and 8: {lca(root, 4, 8).value}")  # Expected: 4
    print(f"LCA of 2 and 8: {lca(root, 2, 8).value}")  # Expected: 2


