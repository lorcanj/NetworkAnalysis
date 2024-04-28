from __future__ import annotations
from Identifiers.GenerateIdentifiers import create_id_alphabet, generate_random_id
# below used to resolve circular dependency
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import Graph


class Node:
    # the node_id should come from the graph, but means can't have nodes without a graph related to it
    # should have different constructors depending on whether we know the neighbours or not
    def __init__(self, label: str = None, graph: Graph = None) -> None:
        # should be able to key the neighbours by node_id and get a reference to the neighbour
        self.neighbours = {}
        # not sure whether it should be graph or just graph_id
        self.graph = graph
        # below doesn't really seem to make sense wrt graph data with unlabeled nodes
        # surely can't have nodes being unlabeled
        if not label:
            self.node_id = Node.create_node_id(self)
        else:
            self.node_id = label

    def to_dict(self):
        return {"node_id": self.node_id}

    @classmethod
    def from_dict(cls, data):
        return cls(data["node_id"])

    def construct_neighbours(self, neighbours: list[Node], directed=False) -> None:
        for neighbour in neighbours:
            if neighbour.node_id not in self.neighbours.keys():
                self.neighbours[neighbour.node_id] = neighbour
                if not directed:
                    neighbour.neighbours[self.node_id] = self

    @staticmethod
    def create_node_id(node: Node) -> str:
        # Node IDs will start with the letter N
        node_id = ["N"]
        return generate_random_id(create_id_alphabet(), node_id)

    @property
    def get_associated_graph(self) -> str | None:
        return self.graph
