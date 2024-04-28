from __future__ import annotations
import pandas as pd
import numpy as np
from .Node import Node
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
    def create_nodes_from_df(df: pd.DataFrame, graph):
        created_nodes: dict[str, Node] = {}

        for index, row in df.iterrows():
            start = row['start']
            end = row['end']

            # first create the nodes if they don't exist
            if start not in created_nodes.keys():
                created_nodes[start] = Node(start, graph)

            if end not in created_nodes.keys():
                created_nodes[end] = Node(end, graph)

            # then add each node to the other node's neighbour dictionary
            if start not in created_nodes[end].neighbours.keys():
                created_nodes[end].neighbours[start] = created_nodes[start]

            if end not in created_nodes[start].neighbours.keys():
                created_nodes[start].neighbours[end] = created_nodes[end]





if __name__ == '__main__':
    pass
