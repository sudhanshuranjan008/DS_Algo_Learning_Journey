# ------------------------------------------------------
# File: min_heap.py
# Date: 2025-03-07
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a Min-Heap with operations: insert, delete, and heapify

class MinHeap:
    def __init__(self):
        """Initialize the heap with a dummy 0 at index 0 (to simplify calculations)."""
        self.heap = [0]  # Index 0 is not used
        self.size = 0  # Track number of elements in heap

    def perc_up(self, index):
        """Move the newly added element up to restore heap property."""
        while index // 2 > 0:
            # If child is smaller than its parent, swap them
            if self.heap[index] < self.heap[index // 2]:
                self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index //= 2  # Move up to parent

    def insert(self, value):
        """Insert a value into the heap."""
        self.heap.append(value)  # Add new value at the end
        self.size += 1  # Increase heap size
        self.perc_up(self.size)  # Restore heap property

    def perc_down(self, index):
        """Move the root element down to maintain heap property after deletion."""
        while (index * 2) <= self.size:
            min_child_index = self.get_min_child_index(index)
            # If the parent is larger than the smallest child, swap them
            if self.heap[index] > self.heap[min_child_index]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
            index = min_child_index  # Continue moving down

    def get_min_child_index(self, index):
        """Return the index of the smaller child."""
        if index * 2 + 1 > self.size:  # Only one child exists (left child)
            return index * 2
        
        # Compare left and right child, return the smaller one
        if self.heap[index * 2] < self.heap[index * 2 + 1]:
            return index * 2
        return index * 2 + 1
            
    def del_min(self):
        """Remove and return the minimum element (root)."""
        if self.size == 0:
            return "Heap is empty"

        root_value = self.heap[1]  # Store the root value (Min element)

        if self.size == 1:  # Only one element case
            self.size -= 1
            return self.heap.pop()  # Remove and return the only element

        self.heap[1] = self.heap[self.size]  # Move last element to root
        self.size -= 1
        self.heap.pop()  # Remove last element (as it's now redundant)
        self.perc_down(1)  # Restore heap property

        return root_value  # Return the removed element

    def heapify(self, elements):
        """Heapify an existing list into a min-heap in O(n) time."""
        self.size = len(elements)
        self.heap = [0] + elements[:]  # Maintain index 0 for easier calculations

        index = self.size // 2  # Start from the last non-leaf node and heapify down
        while index > 0:
            self.perc_down(index)
            index -= 1  # Move to the next parent node

    def display(self):
        """Print the heap as a list (excluding index 0)."""
        print(self.heap[1:])

if __name__ == "__main__":
    my_heap = MinHeap()

    # Insert values into heap
    my_heap.insert(5)
    my_heap.insert(8)
    my_heap.insert(2)
    my_heap.insert(9)
    my_heap.insert(3)
    my_heap.insert(1)

    print("The created Min Heap is: ")
    my_heap.display()

    # Delete the minimum element
    print(f"Deleted: {my_heap.del_min()}")
    my_heap.display()

    # Heapify a given list
    my_heap.heapify([5, 7, 13, 17, 11, 3])
    print(f"The list [5, 7, 13, 17, 11, 3] after heapifying into a min-heap is:")
    my_heap.display()


