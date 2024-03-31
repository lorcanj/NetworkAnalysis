from __future__ import annotations
# below used to resolve circular dependency
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import Graph


class Node:
    # the node_id should come from the graph, but means can't have nodes without a graph related to it
    def __init__(self, graph: Graph):
        # should be able to key the neighbours by node_id and get a reference to the neighbour
        self.neighbours = {}
        self.graph = graph
        Node.assign_node_id(self, graph)

    def construct_neighbours(self, neighbours: list[Node]):
        pass

    # this implementation means we cannot merge 2 separate graphs to create a single graph
    @staticmethod
    def assign_node_id(node: Node, graph: Graph):
        node.node_id = graph.node_id
        graph.node_id += 1
