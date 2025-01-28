# ------------------------------------------------------
# File: queue_using_list_array.py
# Date: 2025-01-28
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a queue using arrays(list)

def create_queue():
    # Function to create and return an empty queue
    return []

def is_empty(input_queue):
    # Function to check if the queue is empty
    # Returns True if the queue is empty, otherwise False
    return len(input_queue) == 0

def enqueue(input_queue, item):
    # Function to add an item to the end of the queue
    # Appends the given item to the list representing the queue
    input_queue.append(item)
    print(f"{item} enqueued. Current queue: {input_queue}")

def dequeue(input_queue):
    # Function to remove and return the front item of the queue
    # If the queue is empty, prints a message and returns None
    if is_empty(input_queue):
        print("Queue underflow. Nothing to delete.")
        return None
    item = input_queue.pop(0)  # Removes the first element in the list
    print(f"{item} dequeued. Current queue: {input_queue}")
    return item

def peek(input_queue):
    # Function to return the front item of the queue without removing it
    # If the queue is empty, prints a message and returns None
    if is_empty(input_queue):
        print("Queue is empty.")
        return None
    return input_queue[0]  # Returns the first element in the list

def display(input_queue: list) -> None:
    # Function to display the current state of the queue
    print(f"Current queue: {input_queue}")


if __name__ == "__main__":
    # Main block to test the queue implementation
    my_queue = create_queue()  # Create an empty queue
    enqueue(my_queue, 2)  # Enqueue 2
    enqueue(my_queue, 3)  # Enqueue 3
    enqueue(my_queue, 5)  # Enqueue 5
    enqueue(my_queue, 7)  # Enqueue 7
    print(f"Front item: {peek(my_queue)}")  # Peek at the front item
    dequeue(my_queue)  # Dequeue an item
    print(f"Front item: {peek(my_queue)}")  # Peek at the front item again
    dequeue(my_queue)  # Dequeue another item
    print(f"Front item: {peek(my_queue)}")  # Peek at the front item again
    display(my_queue)  # Display the current queue

