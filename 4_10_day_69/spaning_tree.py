# Minimum Spanning Tree - Create a program which takes a connected, undirected graph
# with weights and outputs the minimum spanning tree of the graph i.e., a subgraph that
# is a tree, contains all the vertices,
# and the sum of its weights is the least possible.
import heapq
def prims(graph):
    vertices=len(graph)
    in_mst= [False]*vertices
    min_heap=[(0, 0, -1)]
    total_weight=0
    mst_edges=[]

    while min_heap:
        weight,u, parent=heapq.heappop(min_heap)

        if in_mst[u]:
            continue

        in_mst[u]=True
        total_weight +=weight

        if weight !=0:
            mst_edges.append((parent,u,weight))

        for v, edge_weight in graph[u]:
            if not in_mst[v]:
                heapq.heappush(min_heap, (edge_weight, v,u))
                prev_vertex = u

    return mst_edges, total_weight


graph1 = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}
mst_edges,total_weight = prims(graph1)

print("Edges:")
for u, v, weight in mst_edges:
    print(f"{u} - {v} (weight: {weight})")

print(f"Total weight of Minimum Spanning Tree:{total_weight}")