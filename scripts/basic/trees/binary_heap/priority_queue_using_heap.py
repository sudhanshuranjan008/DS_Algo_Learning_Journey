# ------------------------------------------------------
# File: priority_queue_using_heap.py
# Date: 2025-03-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Priority Queue using Min Heap

class PriorityQueue:
    """Class to implement a priority queue using a Min Heap."""

    def __init__(self):
        """Initialize an empty priority queue."""
        self.queue = []
        self.size = 0

    def heapify(self, index):
        """Heapify down to maintain heap property after deletion."""
        root = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Compare with left child
        if left_child_index < self.size and self.queue[index] > self.queue[left_child_index]:
            root = left_child_index

        # Compare with right child
        if right_child_index < self.size and self.queue[root] > self.queue[right_child_index]:
            root = right_child_index

        # Swap if needed and heapify the affected subtree
        if root != index:
            self.queue[index], self.queue[root] = self.queue[root], self.queue[index]
            self.heapify(root)

    def perc_up(self, index):
        """Move the newly added element up to restore heap property."""
        while index > 0:
            parent_index = (index - 1) // 2
            if self.queue[index] < self.queue[parent_index]:
                self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]
            else:
                break  # Stop when heap property is satisfied
            index = parent_index

    def insert(self, value):
        """Insert a new element into the priority queue."""
        self.queue.append(value)
        self.size += 1
        self.perc_up(self.size - 1)  # Restore heap order

    def delete(self):
        """Remove and return the highest priority element (smallest value)."""
        if self.size == 0:
            return None  # Queue is empty

        if self.size == 1:
            self.size -= 1
            return self.queue.pop()  # Only one element present

        # Swap root with last element and remove it
        root_value = self.queue[0]
        self.queue[0] = self.queue[self.size - 1]
        self.queue.pop()
        self.size -= 1

        # Restore heap property
        self.heapify(0)
        return root_value

    def peek(self):
        """Return the highest priority element without removing it."""
        return self.queue[0] if self.size > 0 else None

    def display(self):
        """Display the current state of the priority queue."""
        print(self.queue)


if __name__ == "__main__":
    # Test the priority queue implementation
    p_queue = PriorityQueue()
    p_queue.insert(45)
    p_queue.insert(12)
    p_queue.insert(23)
    p_queue.insert(9)
    p_queue.insert(2)

    print(f"Top Element: {p_queue.peek()}")
    p_queue.display()

    print(f"Deleted: {p_queue.delete()}")
    print(f"Top Element: {p_queue.peek()}")
    p_queue.display()


        