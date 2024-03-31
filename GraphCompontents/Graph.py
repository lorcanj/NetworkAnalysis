import Node
import random


class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.graph_id: str = Graph.create_graph_id()

    @staticmethod
    def create_graph_id():
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = alphabet.upper()
        numbers = '0123456789'
        full_alphabet = alphabet + alphabet_upper + numbers
        graph_id = []
        for i in range(10):
            graph_id.append(full_alphabet[random.randint(0, 61)])
        return ''.join(graph_id)
