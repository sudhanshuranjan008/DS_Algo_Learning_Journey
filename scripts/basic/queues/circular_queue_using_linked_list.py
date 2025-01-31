# ------------------------------------------------------
# File: circular_queue_using_linked_list.py
# Date: 2025-01-31
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a circular queue using linked list

class CircularQueue:
    # Inner class representing a node in the circular queue
    class Node:
        def __init__(self, data):
            self.data = data  # Stores the data value of the node
            self.next = None  # Pointer to the next node (default is None)

    def __init__(self, size):
        self.size = size  # Maximum size of the circular queue
        self.front = None  # Points to the front node of the queue
        self.rear = None  # Points to the rear node of the queue
        self.count = 0  # Tracks the number of elements currently in the queue

    # Checks if the queue is empty
    def is_empty(self):
        return self.front is None

    # Checks if the queue is full
    def is_full(self):
        return self.count == self.size

    # Adds an item to the queue
    def enqueue(self, item):
        new_node = self.Node(item)  # Create a new node with the given data
        if self.is_empty():
            # If the queue is empty, initialize both front and rear to the new node
            self.front = self.rear = new_node
            self.rear.next = self.front  # Make it circular by linking rear to front
            self.count += 1  # Increment the count of items in the queue
        elif self.is_full():
            # If the queue is full, overwrite the front element and adjust pointers
            print(f"Queue is full. Overwriting: '{self.front.data}'")
            self.rear.next = new_node  # Link the current rear to the new node
            self.rear = new_node  # Update the rear to the new node
            self.front = self.front.next  # Move the front pointer to the next node
            self.rear.next = self.front  # Maintain the circular link
        else:
            # If the queue is not full, add the new node at the rear and adjust pointers
            self.rear.next = new_node  # Link the current rear to the new node
            self.rear = new_node  # Update the rear to the new node
            self.rear.next = self.front  # Maintain the circular link
            self.count += 1  # Increment the count of items in the queue

        print(f"{item} enqueued.")

    # Retrieves the front item without removing it
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek at.")
            return None
        return self.front.data  # Return the data of the front node

    # Removes and returns the front item from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow. Nothing to dequeue.")
            return None

        dequeued_item = self.front.data  # Store the data of the front node
        if self.front == self.rear:
            # If there is only one element in the queue, reset front and rear
            self.front = self.rear = None
        else:
            # Otherwise, move the front pointer to the next node and adjust rear
            self.front = self.front.next
            self.rear.next = self.front  # Maintain the circular link

        self.count -= 1  # Decrement the count of items in the queue
        print(f"{dequeued_item} dequeued.")
        return dequeued_item

    # Displays all elements in the queue
    def display(self):
        if self.is_empty():
            return []  # Return an empty list if the queue is empty

        result = []  # List to store the elements of the queue
        current = self.front  # Start from the front of the queue
        while True:
            result.append(current.data)  # Append the current node's data to the list
            current = current.next  # Move to the next node
            if current == self.front:  # Stop when the circular link completes
                break
        return result

# Driver code to test the CircularQueue class
if __name__ == "__main__":
    my_queue = CircularQueue(4)  # Create a circular queue with size 4

    # Enqueue operations
    my_queue.enqueue(5)
    my_queue.enqueue(10)
    my_queue.enqueue(15)
    print(f"Current queue: {my_queue.display()}")
    my_queue.enqueue(20)
    print(f"Current queue: {my_queue.display()}")

    # Dequeue operations
    my_queue.dequeue()
    print(f"Current queue: {my_queue.display()}")

    # Enqueue after dequeue
    my_queue.enqueue(25)
    print(f"Current queue: {my_queue.display()}")

    # Overwrite when the queue is full
    my_queue.enqueue(30)
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")

    # Additional dequeue operations
    my_queue.dequeue()
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")
    my_queue.dequeue()
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")

    # Dequeue until empty
    my_queue.dequeue()
    my_queue.dequeue()
    print(f"Front item: {my_queue.peek()}")
    print(f"Current queue: {my_queue.display()}")

    
