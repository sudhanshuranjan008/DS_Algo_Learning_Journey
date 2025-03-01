# ------------------------------------------------------
# File: doubly_linked_list_intro.py
# Date: 2025-03-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a doubly linked list

class Node:
    def __init__(self, value):
        self.value = value  # Store node value
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Pointer to first node
        self.tail = None  # Pointer to last node

    def prepend(self, value):
        # Insert a new node at the beginning
        new_node = Node(value)
        if not self.head:  # If list is empty, set both head and tail
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  # Link new node to current head
            self.head.prev = new_node  # Link current head back to new node
            self.head = new_node  # Update head pointer

    def append(self, value):
        # Insert a new node at the end
        new_node = Node(value)
        if not self.head:  # If list is empty, set both head and tail
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Link current tail to new node
            new_node.prev = self.tail  # Link new node back to current tail
            self.tail = new_node  # Update tail pointer

    def delete(self, value):
        # Delete a node by value
        if not self.head:  # Edge case: Empty list
            print("List is empty. Nothing to delete.")
            return
        
        current = self.head  # Start from head

        while current:
            if current.value == value:  # Node found
                if current == self.head == self.tail:  # If only one node exists
                    self.head = self.tail = None  # List becomes empty
                    print(f"Deleted {value}. List is now empty.")
                    return

                if current.prev:  
                    current.prev.next = current.next  # Bypass current node
                else:
                    self.head = current.next  # Update head

                if current.next:
                    current.next.prev = current.prev  # Update previous link
                else:
                    self.tail = current.prev  # Update tail

                print(f"Deleted {value} from list.")
                return
            current = current.next  # Move to next node

    def display(self):
        # Print the linked list
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("null")  # End of list marker

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.display()  # Output: 1 <-> 2 <-> 3 <-> null

    dll.delete(3)
    dll.display()  # Output: 1 <-> 2 <-> null

    dll.prepend(0)
    dll.append(5)
    dll.display()  # Output: 0 <-> 1 <-> 2 <-> 5 <-> null
