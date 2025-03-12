# ------------------------------------------------------
# File: graph_using_dict.py
# Date: 2025-03-12
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a graph using dictionary as an adjacency list and print it

class Graph:
    def __init__(self):
        # Dictionary to store adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Add nodes if not present
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        # Add edges (Undirected graph)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        # Print adjacency list representation
        for v, e in self.graph.items():
            print(f"{v} -> {e}")

if __name__ == "__main__":
    g = Graph()
    
    # Add edges to form the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    # Print the graph structure
    g.print_graph()
