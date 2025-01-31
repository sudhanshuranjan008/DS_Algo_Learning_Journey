# ------------------------------------------------------
# File: circular_queue_using_list_array.py
# Date: 2025-01-29
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a circular queue using list as array

class CircularQueue:
    # Constructor to initialize the circular queue
    def __init__(self, size):
        self.size = size  # Maximum size of the queue
        self.cir_queue = [None] * size  # Create a list with None values to represent the queue
        self.front = -1  # Pointer to the front element
        self.rear = -1  # Pointer to the rear element

    # Method to check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Method to check if the queue is full
    def is_full(self):
        # The queue is full when the next rear position overlaps with the front
        return (self.rear + 1) % self.size == self.front

    # Method to add an element to the queue
    def enqueue(self, item):
    # Check if the queue is full
        if self.is_full():
            print(f"Queue is full. Overwriting {self.cir_queue[self.front]}.")
            # Move the front pointer forward to overwrite the oldest element
            self.front = (self.front + 1) % self.size
        
        # Initialize the front pointer if the queue is empty
        elif self.front == -1:
            self.front = 0

        # Move the rear pointer forward in a circular manner
        self.rear = (self.rear + 1) % self.size

        # Place the new item at the rear position
        self.cir_queue[self.rear] = item
        print(f"{item} enqueued.")


    # Method to get the front element of the queue without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Nothing to peek at.")  # Raise an error if the queue is empty
        return self.cir_queue[self.front]  # Return the front element

    # Method to remove an element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow. Nothing to delete.")  # Raise an error if the queue is empty

        # Retrieve the front item
        dequeued_item = self.cir_queue[self.front]

        # If there's only one element in the queue, reset the pointers
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move the front pointer to the next position in a circular manner
            self.front = (self.front + 1) % self.size

        print(f"{dequeued_item} dequeued.")
        return dequeued_item

    # Method to display the elements of the queue
    def display(self):
        if self.is_empty():
            return []  # Return an empty list if the queue is empty

        # If the rear pointer is ahead of or equal to the front pointer
        elif self.rear >= self.front:
            return self.cir_queue[self.front:self.rear + 1]  # Slice the list to get the queue elements

        # If the queue wraps around, combine the two slices
        else:
            return self.cir_queue[self.front:self.size] + self.cir_queue[0:self.rear + 1]


# Main code to test the CircularQueue class
if __name__ == "__main__":
    my_queue = CircularQueue(4)  # Create a circular queue of size 4
    try:
        # Enqueue elements into the queue
        my_queue.enqueue(2)
        my_queue.enqueue(4)
        my_queue.enqueue(6)
        my_queue.enqueue(8)

        # Display the queue and the front item
        print("Current queue:", my_queue.display())
        print(f"Front item: {my_queue.peek()}")

        # Dequeue an element and display the queue
        my_queue.dequeue()
        print("Current queue:", my_queue.display())

        # Enqueue another element
        my_queue.enqueue(10)
        print("Current queue:", my_queue.display())

        my_queue.enqueue(12)
        print("Current queue:", my_queue.display())

        # Dequeue all elements one by one
        while not my_queue.is_empty():
            my_queue.dequeue()

        # Display the queue after all elements are removed
        print("Current queue:", my_queue.display())

        # Attempt to dequeue from an empty queue (will raise an exception)
        my_queue.dequeue()


    except Exception as e:
        # Catch and print any exceptions
        print(e)
