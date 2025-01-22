# ------------------------------------------------------
# File: insertion_deletion_at_position.py
# Date: 2025-01-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to do insertion and deletion in a linked list at a specifc position

# Node class represents an individual element in the linked list
class Node:
    # Constructor to initialize the node with data and next pointer
    def __init__(self, data):
        self.data = data  # Holds the data of the node
        self.next = None  # Pointer to the next node, initially None

# LinkedList class represents the entire linked list
class LinkedList:
    # Constructor to initialize the linked list with an empty head
    def __init__(self):
        self.head = None  # Initially, the linked list is empty (head is None)

    # Method to append a new node with given data to the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # If the list is empty, the new node becomes the head
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            # Traverse the list until we find the last node
            while current.next:
                current = current.next

            # Set the next pointer of the last node to the new node
            current.next = new_node

    # Method to display the linked list as a string representation
    def display(self):
        # If the list is empty, return a message indicating that
        if not self.head:
            return "List is empty."
        
        result = []  # List to store string representations of node data
        current = self.head
        # Traverse through the list and append the data to result
        while current:
            result.append(str(current.data))
            current = current.next
        
        # Join the result with " -> " and append " -> Null" at the end
        return " -> ".join(result) + " -> Null"
    
    # Method to insert a new node at a specified position in the list
    def insert_at_pos(self, pos, value):
        insert_node = Node(value)  # Create a new node to be inserted
        # If the position is 1, insert at the beginning
        if pos == 1:
            insert_node.next = self.head
            self.head = insert_node
            return (f"Inserted '{value}' at '{pos}st' position.")
        
        else:
            current = self.head
            count = 1
            # Traverse the list to find the node just before the insertion position
            while current and count < pos - 1:
                current = current.next
                count += 1
            
            # If position is invalid (out of range), return an error message
            if current is None:
                return("Invalid Position")
            
            # Insert the new node at the desired position
            insert_node.next = current.next
            current.next = insert_node
            return (f"Inserted '{value}' at position '{pos}'.")
    
    # Method to delete a node at a specified position in the list
    def delete_at_pos(self, pos):
        # If the list is empty or the position is invalid, return an error message
        if pos < 1 or self.head is None:
            return ("Nothing to delete. List is empty.")
        
        # If position is 1, delete the head node
        if pos == 1:
            if not self.head.next:
                self.head = None  # If it's the only node, set head to None
                return (f"Deleted data at position '{pos}'. It was the last remaining node.")
            else:
                self.head = self.head.next  # Set head to the next node
                return (f"Deleted data at position '{pos}'.")
            
        current = self.head
        count = 1
        # Traverse the list to find the node just before the one to delete
        while count < pos - 1 and current:
            count += 1
            current = current.next

        # If the position is invalid (out of range), return an error message
        if current.next is None:
            return ("Invalid position.")
        
        # Delete the node by skipping it in the list
        current.next = current.next.next
        return (f"Deleted data at position '{pos}'.")

# Driver code
if __name__ == "__main__":
    ll = LinkedList()  # Create a new linked list instance

    # Append some initial values to the linked list
    for i in range(3, 13, 3):
        ll.append(i)

    # Display the original list
    print(f"The original list is: \n {ll.display()}\n")
    
    # Interactive loop for user input to perform various linked list operations
    while True:
        try:
            # Prompt the user for an operation
            selection = int(input("Please enter: \n'1' for inserting a value in the list.\n'2' for deleting a value from the list.\n'3' for displaying the updated list.\n'4' to EXIT\nEnter here: "))

            # If the input is invalid, raise an exception
            if selection <= 0:
                raise ValueError("Please enter a valid input.")
            
            # If the user selects 1, insert a value at a specified position
            elif selection == 1:
                value = int(input("Enter the value to be inserted: "))
                position = int(input("Enter the position at which you want to insert above value: "))
                print(ll.insert_at_pos(position, value))
            
            # If the user selects 2, delete a value at a specified position
            elif selection == 2:
                value = int(input("Enter the position at which you want value to be deleted: "))
                print(ll.delete_at_pos(value))
            
            # If the user selects 3, display the updated list
            elif selection == 3:
                print(f"List status: \n {ll.display()}")
            
            # If the user selects 4, exit the program
            elif selection == 4:
                print("Exiting program. Thank you")
                break
            
            # If the input is invalid, raise an exception
            elif selection > 3:
                raise ValueError("Please enter a valid input.")
            
        # Handle invalid input errors and prompt the user again
        except ValueError as e:
            print("Please enter a valid input.")

        
