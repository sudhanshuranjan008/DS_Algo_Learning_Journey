# ------------------------------------------------------
# File: bfs_traversal.py
# Date: 2025-03-14
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Given a graph and a starting node, perform a Breadth-First Search (BFS) traversal

from collections import deque  # Importing deque for efficient queue operations

class Graph:
    def __init__(self, size):
        # Initializing adjacency matrix with zeros
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        # Array to store vertex labels (like A, B, C, etc.)
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        # Adds an edge between vertex u and vertex v
        # Ensures indices are within bounds and avoids self-loops
        if 0 <= u < self.size and 0 <= v < self.size and u != v:
            self.adj_matrix[u][v] = 1  # Marking edge in adjacency matrix
            self.adj_matrix[v][u] = 1  # Since it's an undirected graph

    def add_vertex_data(self, vertex, data):
        # Assigns label (data) to a specific vertex
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def display(self):
        # Prints adjacency matrix with vertex labels
        print("Adjacency matrix:")
        print("  ", " ".join(self.vertex_data))  # Printing column headers
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertex_data[i]:<2}", ' '.join(map(str, row)))  # Row labels + matrix values

def bfs(graph, root, vertex_data):
    # BFS traversal starting from 'root'
    visited, queue = set(), deque([root])  # Set to track visited nodes, queue for traversal
    visited.add(root)

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex
        print(str(vertex_data[vertex]), end=" ")  # Print the vertex label

        # Exploring neighbors
        for neighbour, is_adjacent in enumerate(graph[vertex]):
            if is_adjacent == 1 and neighbour not in visited:
                visited.add(neighbour)  # Mark as visited
                queue.append(neighbour)  # Add to queue for further traversal

if __name__ == "__main__":
    g = Graph(5)  # Creating a graph with 5 vertices

    # Assigning labels to vertices
    g.add_vertex_data(0, 'A')
    g.add_vertex_data(1, 'B')
    g.add_vertex_data(2, 'C')
    g.add_vertex_data(3, 'D')
    g.add_vertex_data(4, 'E')

    # Adding edges to define connections
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    g.display()  # Print adjacency matrix

    # Perform BFS traversal starting from vertex 'A' (index 0)
    print("\nBFS Traversal of Graph is:")
    bfs(g.adj_matrix, 0, g.vertex_data)
