# ------------------------------------------------------
# File: heap_kth_min.py
# Date: 2025-03-09
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Given an array, find the K-th smallest element using a Min-Heap

class MinHeap:
    def __init__(self):
        self.heap = [0]  # Initialize heap with a dummy 0 for easier index calculations
        self.size = 0

    def perc_down(self, index):
        """Heapify down to maintain Min-Heap property"""
        while (index * 2) <= self.size:
            min_child_index = self.get_min_child_index(index)
            if self.heap[index] > self.heap[min_child_index]:  # Swap if parent is greater than child
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
            index = min_child_index  # Move down to the swapped position

    def get_min_child_index(self, index):
        """Returns index of the smaller child"""
        if (index * 2) + 1 > self.size:  # If only left child exists
            return index * 2

        # Return the index of the smaller of the two children
        return index * 2 if self.heap[index * 2] < self.heap[index * 2 + 1] else index * 2 + 1

    def del_min(self):
        """Removes and returns the minimum element (root)"""
        if self.size == 0:
            return None  # Return None if heap is empty

        if self.size == 1:
            self.size -= 1
            return self.heap.pop()  # Return the only element

        root_value = self.heap[1]  # Extract the root (minimum element)
        self.heap[1] = self.heap.pop()  # Replace root with the last element
        self.size -= 1
        self.perc_down(1)  # Restore heap property

        return root_value

    def heapify(self, elements):
        """Builds a Min-Heap from an unordered list"""
        self.size = len(elements)
        self.heap = [0] + elements[:]  # Maintain 1-based indexing
        # Start heapifying from the last non-leaf node
        index = self.size // 2
        while index > 0:
            self.perc_down(index)
            index -= 1  # Move to the previous parent node

def get_kth_min(arr, k):
    """Returns the k-th smallest element from the given list"""
    if k > len(arr) or k <= 0:
        return None

    heap = MinHeap()
    heap.heapify(arr)

    # Extract min k times to get the k-th smallest element
    for i in range(k):
        k_min = heap.del_min()
    return k_min  # Return k-th extracted minimum

if __name__ == "__main__":
    num = [12, 11, 17, 28, 5, 19]
    k = int(input("Enter the minima position: "))
    print(f"The {k}-th smallest element is {get_kth_min(num, k)}")


    