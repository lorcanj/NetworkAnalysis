from .Node import Node
from Identifiers.GenerateIdentifiers import create_id_alphabet, generate_random_id


class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.graph_id: str = Graph.create_graph_id()

    @staticmethod
    def create_graph_id():
        # Graph IDs will start with the letter G
        graph_id = ["G"]
        return generate_random_id(create_id_alphabet(), graph_id)
