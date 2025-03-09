# ------------------------------------------------------
# File: heap_kth_max.py
# Date: 2025-03-09
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the Kth largest elements using a Max-Heap

import heapq  # Importing heapq to use heap functions  

def kth_max(arr, k):
    if k > len(arr) or k <= 0:  # Boundary check, kth largest must be within range  
        return None  
    
    max_heap = [-num for num in arr]  # Negating to simulate max heap behavior  
    heapq.heapify(max_heap)  # Heapify to ensure min-heap property (negated values)  
    
    for _ in range(k):  # Extract max k times  
        k_max = -heapq.heappop(max_heap)  # Convert back to positive for actual value  
    
    return k_max  # k-th largest extracted  

if __name__ == "__main__":
    nums = [12, 3, 5, 7, 19]  # Sample list  
    k = int(input("Enter the maxima position: "))  # User input for k  
    print(f"{k}-th largest element is {kth_max(nums, k)}")  # Display result  



