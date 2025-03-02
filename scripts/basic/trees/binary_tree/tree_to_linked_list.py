# ------------------------------------------------------
# File: tree_to_linked_list.py
# Date: 2025-03-02
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Convert Binary Tree to Doubly Linked List

class TreeNode:
    """Represents a node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    """Returns the preorder traversal of the tree (Root → Left → Right)."""
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)

prev = None  # Declare prev globally
head = None  # Declare head globally

def bt_2_dll(root):
    """Converts a Binary Tree to a Doubly Linked List using in-order traversal."""
    global prev, head  # Make head and prev global so they persist

    if root is None:
        return

    # Recursively convert the left subtree
    bt_2_dll(root.left)

    # Process current node
    if prev is None:
        head = root  # First node becomes head
    else:
        root.left = prev
        prev.right = root  # Link prev with current node

    prev = root  # Move prev to current node

    # Recursively convert the right subtree
    bt_2_dll(root.right)

# Test the function
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(30)

    # Display the preorder traversal
    print(f"Pre-order Traversal: {preorder(root)}")

    # Convert and display DLL
    bt_2_dll(root)
    temp = head  # Start from head of DLL
    while temp:
        print(temp.value, end=" <-> ")
        temp = temp.right
    print("Null")
