# Eulerian Path - Create a program which will take as an input a graph and output either a Eulerian path or
# a Eulerian cycle, or state that it is not possible. A Eulerian Path starts at one node and
# traverses every edge of a graph through every node and finishes at another node.
# A Eulerian cycle is a eulerian Path that starts and finishes at the same node.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edges(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self):
        visited = set()

        start_vertex = None
        for v in self.graph:
            if self.graph[v]:
                start_vertex = v
                break

        if start_vertex is None:
            return True

        self.dfs(start_vertex, visited)

        for vertex in self.graph:
            if len(self.graph[vertex]) > 0 and vertex not in visited:
                return False
        return True

    def dfs(self, vertex, visited):
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def eulerian_path_or_cycle(self):
        if not self.is_connected():
            return "graph is not connected."

        odd_degree_count = sum(1 for vertex in self.graph if len(self.graph[vertex]) % 2 != 0)

        if odd_degree_count == 0:
            return " the graph has an eulerian cycle."
        elif odd_degree_count == 2:
            return " the graph has an eulerian path."
        else:
            return " graph doesn't have eulerian path or cycle."


g = Graph()

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("E", "A")
]

for u, v in edges:
    g.add_edges(u, v)

result = g.eulerian_path_or_cycle()
print(result)
