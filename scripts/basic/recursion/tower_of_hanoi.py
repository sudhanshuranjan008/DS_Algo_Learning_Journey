# ------------------------------------------------------
# File: tower_of_hanoi.py
# Date: 2025-02-05
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Solve the Tower of Hanoi problem

def tower_hanoi(N, source, auxilary, destination):
    # Base case: If there's only one disc, move it directly
    if N == 1:
        print(f"Move disc from {source} to {destination}")
        return

    # Step 1: Move N-1 discs from source to auxiliary using destination as temporary storage
    tower_hanoi(N-1, source, destination, auxilary)

    # Step 2: Move the Nth disc from source to destination
    print(f"Move disc from {source} to {destination}")

    # Step 3: Move N-1 discs from auxiliary to destination using source as temporary storage
    tower_hanoi(N-1, auxilary, source, destination)

# Test the function with 3 discs
tower_hanoi(3, 'A', 'B', 'C')




