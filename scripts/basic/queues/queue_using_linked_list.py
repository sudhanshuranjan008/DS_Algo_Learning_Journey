# ------------------------------------------------------
# File: queue_using_linked_list.py
# Date: 2025-01-29
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a queue using a linked list

class Queue:
    # A nested class to represent a Node in the linked list
    class Node:
        def __init__(self, data):
            # Initialize a node with the given data and set the next pointer to None
            self.data = data
            self.next = None
        
    def __init__(self):
        # Initialize an empty queue with head and tail pointers set to None
        self.head = None
        self.tail = None

    def is_empty(self):
        # Check if the queue is empty by verifying if the head is None
        return self.head is None
        
    def enqueue(self, item):
        # Add an item to the queue
        new_node = self.Node(item)  # Create a new node with the given data
        if self.is_empty():
            # If the queue is empty, both head and tail point to the new node
            self.head = self.tail = new_node
        else:
            # Otherwise, add the new node to the end of the queue
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node       # Update the tail to the new node
        
        # Provide feedback to the user
        print(f"{item} enqueued.")

    def peek(self):
        # Retrieve the front item of the queue without removing it
        if self.is_empty():
            # If the queue is empty, print a message and return None
            print("Queue is empty. Nothing to peek at.")
            return None
        
        # Return the data of the head node
        return self.head.data
    
    def dequeue(self):
        # Remove and return the front item of the queue
        if self.is_empty():
            # If the queue is empty, print a message and return None
            print("Queue underflow. Nothing to delete.")
            return None
        else:
            # Store the data of the front node before removing it
            dequeued_item = self.head.data
            self.head = self.head.next  # Update the head to the next node

        # Provide feedback to the user
        print(f"{dequeued_item} dequeued.")
        return dequeued_item  # Return the removed item's data
    
    def display(self):
        # Return a list of all items in the queue
        result = []
        if self.is_empty():
            # If the queue is empty, print a message
            print("Queue is empty.")
        else:
            # Traverse the queue starting from the head
            current = self.head
            while current:
                result.append(current.data)  # Add each node's data to the result list
                current = current.next       # Move to the next node
            
        return result  # Return the list representation of the queue
    

if __name__ == "__main__":
    # Main function to test the Queue implementation
    my_queue = Queue()
    # Enqueue some items into the queue
    my_queue.enqueue(5)
    my_queue.enqueue(10)
    my_queue.enqueue(15)
    my_queue.enqueue(20)
    my_queue.enqueue(25)

    # Peek and display the queue
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")

    # Dequeue items from the queue and display the updated state
    my_queue.dequeue()
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")
    my_queue.dequeue()
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")
    my_queue.dequeue()
    my_queue.dequeue()
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")
    my_queue.dequeue()
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")
