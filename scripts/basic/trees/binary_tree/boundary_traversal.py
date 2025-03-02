# ------------------------------------------------------
# File: boundary_traversal.py
# Date: 2025-03-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Boundary Traversal in a Binary Tree

class TreeNode:
    """Represents a node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    """Returns the preorder traversal of the tree (Root → Left → Right)."""
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)

def is_leaf(node):
    """Returns True if the node is a leaf (i.e., has no children)."""
    return node and not node.left and not node.right

def leaf_nodes(root, ans):
    """
    Collects all leaf nodes of the tree.

    A leaf node is a node that has no children.
    These nodes are collected separately as they should not be included
    in the left or right boundary.
    """
    if root is None:
        return

    if is_leaf(root):
        ans.append(root.value)
        return

    # Recursively collect leaf nodes from left and right subtrees.
    leaf_nodes(root.left, ans)
    leaf_nodes(root.right, ans)

def left_boundary(root, ans):
    """
    Collects the left boundary of the tree, excluding:
      - The root node (handled separately)
      - Leaf nodes (they are handled in leaf_nodes function)

    Traverses the tree down the **left side**, prioritizing the left child.
    If no left child exists, it moves to the right child.
    """
    if root is None or is_leaf(root):  # Stop if it's a leaf or None
        return

    ans.append(root.value)  # Add the current node to the boundary

    # Prefer left child; if absent, move to right child.
    if root.left:
        left_boundary(root.left, ans)
    else:
        left_boundary(root.right, ans)

def right_boundary(root, ans):
    """
    Collects the right boundary of the tree, excluding:
      - The root node (handled separately)
      - Leaf nodes (they are handled in leaf_nodes function)

    Traverses the tree down the **right side**, prioritizing the right child.
    If no right child exists, it moves to the left child.

    Nodes are added **after recursion**, ensuring bottom-up order.
    """
    if root is None or is_leaf(root):  # Stop if it's a leaf or None
        return

    # Prefer right child; if absent, move to left child.
    if root.right:
        right_boundary(root.right, ans)
    else:
        right_boundary(root.left, ans)

    ans.append(root.value)  # Add after recursion to maintain bottom-up order.

def boundary_traversal(root):
    """
    Returns the boundary traversal of the binary tree.

    The boundary traversal consists of:
      1. The root node (if it's not a leaf)
      2. The left boundary (excluding root & leaf nodes)
      3. All leaf nodes (collected separately)
      4. The right boundary (excluding root & leaf nodes, collected in bottom-up order)

    Parameters:
    root (TreeNode): The root of the binary tree.

    Returns:
    list: A list representing the boundary traversal of the tree.
    """
    if root is None:
        return []

    ans = []

    # Step 1: Include root node (if it's not a leaf)
    if not is_leaf(root):
        ans.append(root.value)

    # Step 2: Collect left boundary (excluding leaves)
    left_boundary(root.left, ans)

    # Step 3: Collect all leaf nodes
    leaf_nodes(root, ans)

    # Step 4: Collect right boundary (excluding leaves, in bottom-up order)
    right_boundary(root.right, ans)

    return ans

if __name__ == "__main__":
    # Constructing the tree
    root = TreeNode('R')
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    node3.left = node7
    node4.right = node8

    node6.left = node9
    node6.right = node10

    # Disply the traversal of the tree for better visualization
    print(f"Pre-order Traversal: {preorder(root)}")
    print(f"Boundary Traversal : {boundary_traversal(root)}")

