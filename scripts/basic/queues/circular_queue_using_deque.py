# ------------------------------------------------------
# File: circular_queue_using_deque.py
# Date: 2025-01-30
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a circular queue using collections.deque

# Import deque from collections to use it for the queue
from collections import deque

class CircularQueue:
    def __init__(self, size):
        # Initialize deque with a maximum size and set the size attribute
        self.cir_deque = deque(maxlen=size)  # deque automatically handles circular nature
    
    def enqueue(self, item):
        # If the queue is full, the first item will be overwritten
        if len(self.cir_deque) == self.cir_deque.maxlen:
            print(f"Queue is full! Overwriting: {self.cir_deque[0]}")  # Inform the user that an item will be overwritten
        self.cir_deque.append(item)  # Append the new item, deque handles wrapping automatically
        print(f"{item} enqueued.")  # Inform the user of the enqueued item

    def peek(self):
        # Check if the queue is empty, raise an error if so
        if not self.cir_deque:
            raise IndexError("Queue is empty! Nothing to peek at.")  # Handle empty queue error
        return self.cir_deque[0]  # Return the item at the front of the queue (first element)

    def dequeue(self):
        # Check if the queue is empty, raise an error if so
        if not self.cir_deque:
            raise IndexError("Queue is empty! Nothing to dequeue.")  # Handle empty queue error
        dequeued_item = self.cir_deque.popleft()  # Pop from the left (front of the queue)
        print(f"{dequeued_item} dequeued.")  # Inform the user of the dequeued item
        return dequeued_item  # Return the dequeued item

    def display(self):
        # Display the current state of the queue
        print("Current Queue: ", list(self.cir_deque))  # Convert deque to list for easy display

# Example usage
if __name__ == "__main__":
    my_deque = CircularQueue(4)  # Create a circular queue of size 4
    try:
        # Enqueue elements into the queue
        my_deque.enqueue(2)
        my_deque.enqueue(4)
        my_deque.enqueue(6)
        my_deque.enqueue(8)

        my_deque.display()  # Show current state of the queue
        print(f"Front item: {my_deque.peek()}")  # Peek the front item

        my_deque.dequeue()  # Dequeue an item
        my_deque.display()  # Show current state of the queue

        my_deque.enqueue(10)  # Enqueue another item, which will overwrite 2 due to the fixed size
        my_deque.display()  # Show current state of the queue

        my_deque.enqueue(12)  # Enqueue another item, which will overwrite 4
        my_deque.display()  # Show current state of the queue

    except Exception as e:
        print(e)  # Catch and print any exceptions raised in the try block

