# ------------------------------------------------------
# File: graph_using_adj_matrix.py
# Date: 2025-03-13
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Graph implementation using adjacency matrix

class Graph:
    def __init__(self, size):
        # Initialize adjacency matrix with 0s
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        # Store data for each vertex
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        # Add edge if indices are valid and no self-loops
        if 0 <= u < self.size and 0 <= v < self.size and u != v:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1  # Undirected graph, so mirror the connection

    def add_vertex_data(self, vertex, data):
        # Assign data to a valid vertex
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def display(self):
        # Print adjacency matrix with vertex labels
        print("Adjacency Matrix:")
        print("  ", " ".join(self.vertex_data))  # Column headers
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertex_data[i]:<2}", ' '.join(map(str, row)))  # Row labels

if __name__ == "__main__":
    # Create a graph with 4 vertices
    g = Graph(4)
    
    # Assign labels to vertices
    g.add_vertex_data(0, 'A')
    g.add_vertex_data(1, 'B')
    g.add_vertex_data(2, 'C')
    g.add_vertex_data(3, 'D')
    
    # Add edges between vertices
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)

    # Display the graph representation
    g.display()
