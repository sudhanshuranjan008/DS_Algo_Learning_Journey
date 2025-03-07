# ------------------------------------------------------
# File: max_heap.py
# Date: 2025-03-08
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a Max-Heap with operations: insert, delete, and heapify

class MaxHeap:
    def __init__(self):
        """Initialize the heap with a dummy 0 at index 0 (to simplify calculations)."""
        self.heap = [0] # Index 0 is not used
        self.size = 0  # Track number of elements in heap

    def perc_up(self, index):
        """Move the newly added element up to restore heap property."""
        while index // 2 > 0:  # Parent exists
            if self.heap[index] > self.heap[index // 2]:  # Swap if child > parent
                self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index //= 2  # Move up to parent

    def insert(self, value):
        """Insert value at the end and adjust position"""
        self.heap.append(value)
        self.size += 1  # Increase heap size
        self.perc_up(self.size)  # Restore heap property

    def perc_down(self, index):
        """Move the root element down to maintain heap property after deletion."""
        while (index * 2) <= self.size:  # While left child exists
            max_child_index = self.get_max_child_index(index)
            if self.heap[index] < self.heap[max_child_index]:  # Swap if child > parent
                self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
            index = max_child_index  # Move down to the swapped position

    def get_max_child_index(self, index):
        """Returns the index of the larger child"""
        if index * 2 + 1 > self.size:  # Only left child exists
            return index * 2
        # Return the larger of the two children
        if self.heap[index * 2] > self.heap[index * 2 + 1]:
            return index * 2
        return index * 2 + 1

    def del_max(self):
        """Deletes and returns the max element (root of heap)"""
        if self.size == 0:
            return "Heap is empty"

        if self.size == 1: # Only one element case
            self.size -= 1
            return self.heap.pop()  # Pop the last remaining element and return
        
        root_value = self.heap[1]  # Max element (root)
        self.heap[1] = self.heap[self.size]  # Move last element to root
        self.size -= 1
        self.heap.pop()  # Remove last element
        self.perc_down(1)  # Restore heap property
        return root_value  # Return the removed element

    def heapify(self, elements):
        """Converts an unordered list into a max-heap (Bottom-Up)"""
        self.size = len(elements)
        self.heap = [0] + elements[:]  # Maintain index 0 for easier calculations
        
        # Start from the last non-leaf node and heapify down
        index = self.size // 2  
        while index > 0:
            self.perc_down(index)
            index -= 1  # Move to the next parent node

    def display(self):
        """Prints heap elements excluding the dummy index 0"""
        print(self.heap[1:])

# ---- Driver Code ----
if __name__ == "__main__":
    my_heap = MaxHeap()

    # Insert elements
    my_heap.insert(5)
    my_heap.insert(8)
    my_heap.insert(2)
    my_heap.insert(9)
    my_heap.insert(3)
    my_heap.insert(1)

    print("The created Max Heap is:")
    my_heap.display()  # Expected: A valid max heap

    # Delete max element
    print(f"Deleted: {my_heap.del_max()}")  # Expected: 9
    my_heap.display()

    # Heapify an unsorted list
    my_heap.heapify([5, 7, 13, 17, 11, 3])
    print(f"The list [5, 7, 13, 17, 11, 3] after heapifying into a max-heap is:")
    my_heap.display()  # Expected: A valid max heap structure

    