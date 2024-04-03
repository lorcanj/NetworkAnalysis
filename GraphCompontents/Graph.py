from __future__ import annotations
import pandas as pd
from .Node import Node
from .Edge import Edge
from Identifiers.GenerateIdentifiers import create_id_alphabet, generate_random_id


class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.graph_id: str = Graph._create_graph_id()

    @staticmethod
    def _create_graph_id():
        # Graph IDs will start with the letter G
        graph_id = ["G"]
        return generate_random_id(create_id_alphabet(), graph_id)

    @staticmethod
    def create_nodes_from_df(df: pd.DataFrame, graph: Graph = None) -> dict[str, Node]:
        unique_nodes: dict[str, Node] = {}
        unique_starts: set[str] = set()

        if 'start' in df.columns:
            unique_starts = set(df['start'])
            for label in unique_starts:
                unique_nodes[label] = Node(label, graph)
        if 'end' in df.columns:
            ends: set[str] = set(df['end'])
            unique_ends = ends - unique_starts
            for label in unique_ends:
                unique_nodes[label] = Node(label, graph)
        return unique_nodes



if __name__ == '__main__':
    pass