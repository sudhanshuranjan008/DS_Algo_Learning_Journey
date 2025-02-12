# ------------------------------------------------------
# File: shell_sort.py
# Date: 2025-02-12
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement Shell Sort and test with shell's original gap sequence

def shell_sort_swap(num):
    """
    Shell Sort Implementation (Original Swapping Method)

    Time Complexity:
        - Best Case: O(n log n) (for certain gap sequences)
        - Worst Case: O(n^2) (Shell's original gap sequence)

    Space Complexity:
        - O(1) (In-place sorting)

    This function sorts a list using Shell Sort with the original swapping method.
    Instead of shifting elements, it swaps them while sorting with decreasing gap sizes.
    """
    n = len(num)
    gap = n // 2  # Initialize gap to half of the list size

    while gap > 0:
        # Perform gap-based sorting
        for i in range(gap, n):
            j = i  # Start comparing from index `i`

            # Swap elements if they are out of order
            while j >= gap and num[j - gap] > num[j]:
                num[j], num[j - gap] = num[j - gap], num[j]
                j -= gap  # Move back by `gap` and check previous elements

        gap //= 2  # Reduce gap size for next iteration

    return num

if __name__ == "__main__":
    num_list = [5, 56, -5, 63, 0, 2, 7]
    print(f"Original list: {num_list}")
    print(f"Sorted list  : {shell_sort_swap(num_list[:])}")  # Pass a copy to prevent modification

