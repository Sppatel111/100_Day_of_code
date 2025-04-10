# Dijkstra’s Algorithm - Create a program that finds the shortest path through a graph using its edges.
import heapq

def dijksra(graph, start):
    distances = {}
    for node in graph:
        distances[node] = float('infinity')

    distances[start]=0
    priority_queue=[(0,start)]

    while priority_queue:
        current_distance,current_node =heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor,weight in graph[current_node].items():
            distance=current_distance+weight

            if distance < distances[neighbor]:
                distances[neighbor]= distance
                heapq.heappush(priority_queue,(distance,neighbor))

    return distances

graph1 = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node='A'
shortest_path=dijksra(graph1,start_node)
print(shortest_path)