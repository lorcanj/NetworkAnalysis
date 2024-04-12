import pytest
import pandas as pd
import random
from GraphCompontents.Graph import Graph
from GraphCompontents.Node import Node
from MockData.StaticTestData import create_mock_data, input_test_size


@pytest.fixture()
def df_static_data(input_test_size) -> pd.DataFrame:
    return create_mock_data(input_test_size)


# Mocked data contains nodes with identifiers below
@pytest.fixture()
def expected_nodes_length():
    return len(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'))


def test_create_nodes_from_df(df_static_data, expected_nodes_length):
    d: dict[str, Node] = Graph.create_nodes_from_df(df_static_data)
    assert d is not None
    assert len(d) == expected_nodes_length


def test_assign_nodes_to_graph(df_static_data):
    g = Graph()
    d: dict[str, Node] = Graph.create_nodes_from_df(df_static_data, g)
    assert len(g.nodes) != 0


def test_assign_neighbours(df_static_data: pd.DataFrame, create_unique_nodes: dict[str, Node]):
    Graph.assign_neighbours(df_static_data, create_unique_nodes)
    for node in create_unique_nodes.values():
        assert len(node.neighbours) != 0
        # all/ any of the assigned neighbours should be of type Node
        assert isinstance(node.neighbours[random.choice(list(node.neighbours.keys()))], Node)


@pytest.fixture()
def create_unique_nodes(df_static_data) -> dict[str, Node]:
    return Graph.create_nodes_from_df(df_static_data)


if __name__ == '__main__':
    print(test_assign_neighbours())
