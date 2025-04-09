class Graph:
    def __init__(self):
        self.graph={}

    def add_link(self,node1,node2):
        if node1 not in self.graph:
            self.graph[node1]=[]
        if node2 not in self.graph:
            self.graph[node2] =[]

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def display(self):
        print(self.graph)

links = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("E", "A")
]

graph = Graph()
for link in links:
    graph.add_link(link[0], link[1])

graph.display()