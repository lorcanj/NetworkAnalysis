from GraphCompontents.Graph import Graph

"""
Won't always be true but should be uncommon enough that this passes the test
"""


def test_graph_id():
    g1 = Graph()
    g2 = Graph()
    assert g1.graph_id != g2.graph_id
