def is_connected(graph):
    if not graph:
        return True
    start_node = next(iter(graph))

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start_node)

    return len(visited) == len(graph)

graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
print(f"Graph 1 is connected: {is_connected(graph1)}")

