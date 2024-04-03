from GraphCompontents.Node import Node
import pytest


@pytest.fixture()
def create_test_nodes():
    n1 = Node(label="n1")
    n2 = Node(label="n2")
    n3 = Node(label="n3")
    n4 = Node(label="n4")
    n1_neighbours = [n2, n4]
    n2_neighbours = [n3]
    n3_neighbours = [n1]
    n4_neighbours = []
    n1.construct_neighbours(n1_neighbours)
    n2.construct_neighbours(n2_neighbours)
    n3.construct_neighbours(n3_neighbours)
    n4.construct_neighbours(n4_neighbours)
    return [n1, n2, n3, n4]


def test_neighbours_construction(create_test_nodes: list[Node], expected_neighbours_length: int):
    n1, n2, n3, n4 = create_test_nodes

    assert n2.node_id in n1.neighbours.keys()
    # check for undirected graph construction where nodes connected by an edge
    # should be contained in both neighbour dictionaries
    assert n1.node_id in n4.neighbours.keys()
    assert len(n1.neighbours) == expected_neighbours_length


@pytest.fixture()
def expected_neighbours_length():
    return 3
