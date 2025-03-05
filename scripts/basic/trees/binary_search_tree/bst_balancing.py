# ------------------------------------------------------
# File: bst_balancing.py
# Date: 2025-03-06
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Convert BST to a Balanced BST

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child pointer
        self.right = None  # Right child pointer

# Perform inorder traversal (Left -> Root -> Right) to get a sorted list of node values
def inorder(root):
    return [] if not root else inorder(root.left) + [root.data] + inorder(root.right)

# Perform preorder traversal (Root -> Left -> Right) to verify tree structure
def preorder(root):
    return [] if not root else [root.data] + preorder(root.left) + preorder(root.right)

# Insert a node into BST while maintaining BST properties
def insert(root, value):
    if not root:
        return TreeNode(value)  # Create a new node if root is None
    
    if root.data > value:
        root.left = insert(root.left, value)  # Insert in left subtree if value is smaller
    else:
        root.right = insert(root.right, value)  # Insert in right subtree if value is greater

    return root  # Return updated root

# Construct a balanced BST from a sorted list of node values
def build_balance_bst(nodes, start, end):
    if start > end:
        return None  # Base condition: no elements to construct subtree
    
    mid = (start + end) // 2  # Select middle element as root to maintain balance
    root = TreeNode(nodes[mid])

    # Recursively construct left and right subtrees
    root.left = build_balance_bst(nodes, start, mid - 1)
    root.right = build_balance_bst(nodes, mid + 1, end)

    return root  # Return balanced root

# Convert an unbalanced BST into a balanced BST
def balance_bst(root):
    if not root:
        return None  # Return None if tree is empty
    
    nodes = inorder(root)  # Get sorted list of nodes using inorder traversal

    return build_balance_bst(nodes, 0, len(nodes) - 1)  # Construct balanced BST

if __name__ == "__main__":
    # Construct an unbalanced BST
    root = None
    root = insert(root, 25)
    root = insert(root, 20)
    root = insert(root, 15)
    root = insert(root, 19)
    root = insert(root, 34)

    # Display BST in preorder traversal before balancing
    print(f"Preorder Traversal of BST after insertion (Unbalanced): {preorder(root)}")

    # Convert BST to a balanced BST
    balanced_root = balance_bst(root)

    # Display BST in preorder traversal after balancing
    print(f"Preorder Traversal of Balanced BST: {preorder(balanced_root)}")
