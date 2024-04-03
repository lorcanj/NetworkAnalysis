from GraphCompontents.Node import Node


# probably don't need an edge
class Edge:
    def __init__(self, weight: int = 1, capacity: int = 1, directed=False):
        self.weight = weight
        self.capacity = capacity
        self.directed = directed

    def __str__(self):
        print(f"Edge connects {self.node_1} to {self.node_2} with a weight of {self.weight}")
