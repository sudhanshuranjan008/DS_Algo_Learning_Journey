# ------------------------------------------------------
# File: detect_cycle_in_graph.py
# Date: 2025-03-15
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

from collections import deque

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

def bfs(graph, root, visited):
    """Performs BFS and checks for cycles in an undirected graph."""
    
    queue = deque([(root, -1)])  # Initialize queue with (node, parent) pair
    visited.add(root)  # Mark the root as visited

    while queue:
        vertex, parent = queue.popleft()  # Dequeue the front element (current node, parent)

        # Traverse all neighbors of the current node
        for neighbor in graph[vertex]:  
            if neighbor not in visited:  
                visited.add(neighbor)  # Mark neighbor as visited
                queue.append((neighbor, vertex))  # Enqueue neighbor with current node as parent

            # If the neighbor is visited and not the parent, a cycle exists
            elif parent != neighbor:
                return True  # Cycle detected

    return False  # No cycle found in this BFS traversal

def is_cycle(graph):
    """Checks if the graph contains a cycle using BFS."""

    visited = set()  # Set to track visited nodes across all components

    # Traverse all nodes in case of disconnected components
    for node in graph:
        if node not in visited:  # If node is unvisited, start BFS
            if bfs(graph, node, visited):  
                return True  # If any component contains a cycle, return True

    return False  # No cycle found in the graph

# Example Usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "F")
    g.add_edge("C", "G")
    g.add_edge("F", "G")  # This creates a cycle

    g.print_matrix()
    
    print("Cycle Detected:", is_cycle(g.graph))

