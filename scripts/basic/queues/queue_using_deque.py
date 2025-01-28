# ------------------------------------------------------
# File: queue_using_deque.py
# Date: 2025-01-28
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a queue using collections.deque

from collections import deque

# Creates a new queue using deque, which is optimized for O(1) operations at both ends.
def create_queue():
    return deque()  # O(1) - deque initialization is constant time.

# Checks if the queue is empty by comparing its length to 0.
def is_empty(input_queue: deque):
    return len(input_queue) == 0  # O(1) - len() is an O(1) operation on deque.

# Adds an item to the end of the queue.
def enqueue(input_queue: deque, item: int):
    input_queue.append(item)  # O(1) - appending to the end of deque is O(1).
    print(f"{item} enqueued.")

# Removes an item from the front of the queue if it's not empty.
def dequeue(input_queue: deque):
    if is_empty(input_queue):
        print("Queue underflow. Nothing to delete.")
        return None
    item = input_queue.popleft()  # O(1) - popping from the front of deque is O(1).
    print(f"{item} dequeued.")
    return item

# Returns the front item of the queue without removing it.
def peek(input_queue: deque):
    if is_empty(input_queue):
        print("Queue is empty. Nothing to peek at.")
        return None
    return input_queue[0]

# Displays the contents of the queue.
# Time complexity: O(n), where n is the number of elements in the queue.
def display(input_queue: deque):
    print(f"Current queue: {list(input_queue)}")  # O(n) - converting deque to list is O(n), where n is the number of items in the queue.

if __name__ == "__main__":
    my_queue = create_queue()  # creates an empty queue.
    # Add elements to the end of the queue.
    enqueue(my_queue, 2)
    enqueue(my_queue, 3)
    enqueue(my_queue, 5)
    enqueue(my_queue, 7)
    # Access the front item in the queue
    print(f"Front item: {peek(my_queue)}")
    # Display the queue
    display(my_queue)
    # Remove an element from the queue
    dequeue(my_queue)
    print(f"Front item: {peek(my_queue)}")
    display(my_queue)
    dequeue(my_queue)
    print(f"Front item: {peek(my_queue)}")
    display(my_queue)



