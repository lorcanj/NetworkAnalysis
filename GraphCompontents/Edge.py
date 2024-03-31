from GraphCompontents.Node import Node


class Edge:
    def __init__(self, edge_id: int, node_1: Node, node_2: Node, weight: int = 1, capacity: int = 1, bi_directional=True):
        self.edge_id = edge_id
        self.node_1 = node_1
        self.node_2 = node_2
        self.weight = weight
        self.capacity = capacity
        self.bi_directional = bi_directional

    def __str__(self):
        print(f"Edge connects {self.node_1} to {self.node_2} with a weight of {self.weight}")
