# ------------------------------------------------------
# File: dfs_traversal.py
# Date: 2025-03-14
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Given a graph and a starting node, perform a Depth-First Search (DFS) traversal

class Graph:
    def __init__(self, size):
        # Initialize adjacency matrix with 0s (no edges initially)
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        # Stores labels/data for each vertex
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        # Add an edge between vertex 'u' and vertex 'v' (undirected graph)
        if 0 <= u < self.size and 0 <= v < self.size and u != v:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        # Assign label/data to a specific vertex
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def display(self):
        # Print adjacency matrix representation of the graph
        print("Adjacency matrix:")
        print("  ", " ".join(self.vertex_data))  # Print column headers
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertex_data[i]:<2}", ' '.join(map(str, row)))  # Print row headers

# Perform Depth-First Search (DFS) traversal
def dfs(graph, root, vertex_data=None, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set

    visited.add(root)  # Mark current node as visited
    print(str(vertex_data[root]), end=" ")  # Print the vertex label

    # Explore all adjacent vertices
    for neighbour, is_adjacent in enumerate(graph[root]):
        if is_adjacent == 1 and neighbour not in visited:
            dfs(graph, neighbour, vertex_data, visited)  # Recursive DFS call

# Driver code
if __name__ == "__main__":
    g = Graph(5)  # Create a graph with 5 vertices

    # Assign labels to vertices
    g.add_vertex_data(0, 'A')
    g.add_vertex_data(1, 'B')
    g.add_vertex_data(2, 'C')
    g.add_vertex_data(3, 'D')
    g.add_vertex_data(4, 'E')

    # Define edges (connections between vertices)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    g.display()  # Print adjacency matrix

    print("\nDFS Traversal starting from vertex A:")
    dfs(g.adj_matrix, 0, g.vertex_data)  # Start DFS from vertex 0 ('A')
