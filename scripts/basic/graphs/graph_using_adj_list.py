# ------------------------------------------------------
# File: graph_using_adj_list.py
# Date: 2025-03-12
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Graph implementation using adjacency list (linked list)

class AdjNode:
    def __init__(self, value):
        self.vertex = value  # Store vertex value
        self.next = None  # Pointer to the next node

class Graph:
    def __init__(self, num):
        self.V = num  # Number of vertices
        self.graph = [None] * self.V  # Array of adjacency lists (linked lists)

    def add_edge(self, s, d):
        """Add node to the start of adjacency list (for O(1) insertion)"""

        node = AdjNode(d)
        node.next = self.graph[s]  # Point to the old head
        self.graph[s] = node  # Update head

        # Since the graph is undirected, do the same for the other vertex
        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def display(self):
        """Print adjacency list representation"""

        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")  
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")  
                temp = temp.next
            print("\n")  # Newline for clarity

if __name__ == "__main__":
    graph = Graph(4)  # Create a graph with 4 vertices

    # Adding edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    graph.display()  # Print the adjacency list
