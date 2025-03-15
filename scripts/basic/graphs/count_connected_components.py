# ------------------------------------------------------
# File: count_connected_components.py
# Date: 2025-03-15
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Given an undirected graph, count the number of connected components

class Graph:
    """Represents an undirected graph using an adjacency list."""

    def __init__(self):
        self.graph = {}  # Using dictionary to store adjacency list
    
    def add_edge(self, u, v, weight=1):
        """Adds an undirected edge between u and v with the given weight."""

        if u not in self.graph:
            self.graph[u] = {}  # Initialize adjacency list for vertex u
        if v not in self.graph:
            self.graph[v] = {}  # Initialize adjacency list for vertex v

        self.graph[u][v] = weight  # Assign weight (default is 1) for undirected edge
        self.graph[v][u] = weight  # Ensure bidirectional connection

    def print_matrix(self):
        """Prints the adjacency matrix representation of the graph."""

        nodes = sorted(self.graph.keys())  # Sort for consistent display
        print("  ", " ".join(nodes))  # Header row
        for u in nodes:
            row = [str(self.graph[u].get(v, 0)) for v in nodes]  # Get weight or default to 0
            print(f"{u}: " + " ".join(row))

def dfs(graph, root, visited):
    """Performs Depth-First Search (DFS) to mark all reachable vertices."""

    visited.add(root)  # Mark current node as visited
    for neighbor in graph[root]:  # Traverse all connected nodes
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursive DFS call

def count_connected_components(graph):
    """Counts the number of connected components in the graph."""
    
    visited = set()  # Track visited nodes
    components = 0  # Counter for connected components

    for vertex in graph:  # Iterate over all vertices
        if vertex not in visited:  # If vertex not visited, it's a new component
            components += 1
            dfs(graph, vertex, visited)  # Explore the whole component

    return components  # Return total number of components

# Example Usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "F")
    g.add_edge("C", "G")

    g.add_edge("X", "Y")  # Separate component

    g.print_matrix()  # Display adjacency matrix

    print("Number of connected components:", count_connected_components(g.graph))  # Count and print components


