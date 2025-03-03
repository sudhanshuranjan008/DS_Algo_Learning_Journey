# ------------------------------------------------------
# File: bst_insertion_deletion.py
# Date: 2025-03-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a Binary Search Tree with Insertion & Deletion operations

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child pointer
        self.right = None  # Right child pointer

# Perform Inorder Traversal (LNR -> Left, Node, Right)
# Returns sorted order of elements in BST
def inorder(root):
    return [] if not root else inorder(root.left) + [root.data] + inorder(root.right)

# Insert a new value into BST
def insert(root, value):
    if root is None:
        return TreeNode(value)  # New node is created when root is None
    
    if root.data == value:
        return root  # No duplicate values in BST
    
    elif root.data < value:
        root.right = insert(root.right, value)  # Insert in right subtree

    else:
        root.left = insert(root.left, value)  # Insert in left subtree

    return root  # Return the updated root

# Find the inorder successor (smallest node in right subtree)
def successor(node):
    node = node.right  # Move to right subtree first
    while node and node.left:
        node = node.left  # Find the leftmost node
    return node  # Return inorder successor

# Delete a node from BST
def delete(root, value):
    if not root:
        print(f"Value {value} not found in BST.")  # Nudge: Added debug print
        return root  # Base case: Empty tree or value not found

    # Navigate to the node to be deleted
    if root.data > value:
        root.left = delete(root.left, value)

    elif root.data < value:
        root.right = delete(root.right, value)

    else:
        # Case 1 & 2: Node has 0 or 1 child
        if not root.left:
            return root.right  # Replace with right child (can be None)
        if not root.right:
            return root.left  # Replace with left child (can be None)

        # Case 3: Node has 2 children -> Replace with inorder successor
        successor_node = successor(root)  # Find smallest node in right subtree
        if successor_node:
            root.data = successor_node.data  # Copy successor's value
            root.right = delete(root.right, successor_node.data)  # Delete successor

    return root  # Return updated root


# Driver Code
if __name__ == "__main__":
    root = None  # Start with an empty BST

    # Insert nodes into BST
    root = insert(root, 55)
    root = insert(root, 50)
    root = insert(root, 60)
    root = insert(root, 45)
    root = insert(root, 47)
    root = insert(root, 67)
    root = insert(root, 43)

    print(f"Inorder Traversal of BST after insertion: {inorder(root)}")

    # Test Deletions
    print("Deleting 45 (Parent Node with 2 Children)...")
    root = delete(root, 45)
    print(f"Inorder after deleting 45: {inorder(root)}")

    print("Deleting 50 (Node with One Child)...")
    root = delete(root, 50)
    print(f"Inorder after deleting 50: {inorder(root)}")

    print("Deleting 505 (No Such Node)...")
    root = delete(root, 505)  # This should print "Value 505 not found in BST."
    print(f"Inorder after deleting 505: {inorder(root)}")


