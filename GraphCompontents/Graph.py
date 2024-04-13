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
    def create_nodes_from_df(df: pd.DataFrame, graph: Graph = None) -> dict[str, Node]:
        unique_nodes: dict[str, Node] = {}
        unique_starts: set[str] = set()

        if 'start' in df.columns:
            unique_starts = set(df['start'])
            for label in unique_starts:
                unique_nodes[label] = Node(label, graph)
                # assign the node to the graph
                if graph:
                    graph.nodes[label] = unique_nodes[label]
        if 'end' in df.columns:
            ends: set[str] = set(df['end'])
            unique_ends = ends - unique_starts
            for label in unique_ends:
                unique_nodes[label] = Node(label, graph)
                if graph:
                    graph.nodes[label] = unique_nodes[label]
        return unique_nodes

    @staticmethod
    def assign_neighbours(df: pd.DataFrame, unique_nodes: dict[str, Node], directed=False):

        for index, row in df.iterrows():
            start = row['start']
            end = row['end']

            if start not in unique_nodes.keys() or end not in unique_nodes.keys():
                continue

            if start not in unique_nodes[end].neighbours:
                unique_nodes[end].neighbours[start] = unique_nodes[start]

            if end not in unique_nodes[start].neighbours:
                unique_nodes[start].neighbours[end] = unique_nodes[end]


if __name__ == '__main__':
    pass
