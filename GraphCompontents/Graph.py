from __future__ import annotations
import pandas as pd
import numpy as np
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

    @staticmethod
    def assign_neighbours(df: pd.DataFrame, unique_nodes: dict[str, Node], directed=False):
        # assume 'start' and 'end' column are in the dataframe for now

        for node in unique_nodes.values():
            # TODO: deal with directed graph later
            if not directed:
                start_matched = df.loc[(df['start'] == node.node_id)]
                unique_values_from_start = start_matched['end'].unique()
                end_matched = df.loc[df['end'] == node.node_id]
                unique_values_from_end = end_matched['start'].unique()
                combined = np.concatenate((unique_values_from_start, unique_values_from_end))
                for neighbour in combined:
                    node.neighbours[neighbour] = unique_nodes[neighbour]


if __name__ == '__main__':
    pass
