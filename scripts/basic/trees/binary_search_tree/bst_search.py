# ------------------------------------------------------
# File: bst_search.py
# Date: 2025-03-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Search Operation in a Binary Search Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child pointer
        self.right = None  # Right child pointer

# Inorder traversal (Left -> Root -> Right)
def inorder(root):
    return [] if not root else inorder(root.left) + [root.data] + inorder(root.right)

# Insert a node into BST
def insert(root, value):
    if not root:
        return TreeNode(value)  # Create new node if root is None
    
    if root.data > value:
        root.left = insert(root.left, value)  # Insert in left subtree if value is smaller
    else:
        root.right = insert(root.right, value)  # Insert in right subtree if value is greater

    return root  # Return updated root

# Search for a node in BST
def search(root, value):
    if not root:
        return None  # Base case: Not found
    
    if root.data == value:
        return root  # Value found, return node
    
    elif root.data > value:
        return search(root.left, value)  # Search in left subtree if value is smaller
    else:
        return search(root.right, value)  # Search in right subtree if value is greater

if __name__ == "__main__":
    # Construct BST
    root = None
    root = insert(root, 25)
    root = insert(root, 20)
    root = insert(root, 35)
    root = insert(root, 17)
    root = insert(root, 24)
    root = insert(root, 34)
    root = insert(root, 40)

    print(f"Inorder Traversal of BST after insertion: {inorder(root)}")

    # Input for search operation
    input_num = int(input("Enter the number to be searched: "))

    # Perform search and print result
    result = search(root, input_num)
    if result:
        print(f"Found! Node: {result.data}")
    else:
        print("Not Found!")
