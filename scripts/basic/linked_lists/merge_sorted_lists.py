# ------------------------------------------------------
# File: merge_sorted_lists.py
# Date: 2025-01-24
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Merge two sorted linked lists into one sorted list

class Node:
    # Initialize the node with data and set the next pointer to None
    def __init__(self, data):
        self.data = data  # The value the node will hold
        self.next = None  # Pointer to the next node, initially set to None

class LinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list, initially set to None
        self.tail = None  # Tail of the linked list, initially set to None

    def append(self, data):
        # Add a new node with the given data at the end of the list
        new_node = Node(data)  # Create a new node with the data
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node  # Both head and tail point to the new node
        else:
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node  # Update the tail to the new node

    def display(self):
        # Traverse the linked list and return a string representation
        current = self.head  # Start from the head
        result = []  # To store the string representation of the list
        while current:
            result.append(str(current.data))  # Append node data to result
            current = current.next  # Move to the next node

        return " -> ".join(result) + " -> Null"  # Join the result with " -> " and return the list representation
    
def merge_sorted_lists(list1, list2):
    # Merge two sorted linked lists into one sorted linked list
    dummy_node = Node(None)  # Create a dummy node to simplify the merging process
    current = dummy_node  # Pointer to the current node in the merged list

    # Merge the lists as long as both lists are not empty
    while list1 and list2:
        if list1.data < list2.data:  # Compare the data of the nodes from both lists
            current.next = list1  # Link the current node to the smaller node
            list1 = list1.next  # Move to the next node in list1
        else:
            current.next = list2  # Link the current node to the smaller node
            list2 = list2.next  # Move to the next node in list2
        current = current.next  # Move the current pointer to the newly added node

    # If either list1 or list2 is not empty, link the remaining nodes
    current.next = list1 if list1 else list2

    return dummy_node.next  # Return the merged list starting from the first valid node (skipping the dummy node)
   

if __name__ == "__main__":
    list1 = LinkedList()  # Create the first linked list
    list2 = LinkedList()  # Create the second linked list

    # Append odd numbers to the first list (sorted)
    for i in range(1, 10, 2):
        list1.append(i)
    print(f"The 1st sorted list is:\n{list1.display()}")

    # Append even numbers to the second list (sorted)
    for i in range(2, 11, 2):
        list2.append(i)
    print(f"The 2nd sorted list is:\n{list2.display()}")

    # Merge the two sorted lists
    merged_list_head = merge_sorted_lists(list1.head, list2.head)  # Get the head of the merged list
    merged_list = LinkedList()  # Create a new linked list for the merged result
    merged_list.head = merged_list_head  # Set the head of the merged list
    print(f"The merged sorted list is:\n{merged_list.display()}")


    



