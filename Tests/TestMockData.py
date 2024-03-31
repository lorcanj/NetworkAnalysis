import pytest
from MockData.StaticTestData import create_mock_data
from GraphCompontents.Edge import Edge

"""
Know that data is of the below format so can manually check whether
values in the df conform to the example shown below
LinkId	Start	End	 Capacity	Weight
1	    A	    B	 10	        5
2	    B	    C	 10	        5
3	    C	    D	 10	        5
"""


@pytest.fixture
def edges():
    e1 = Edge(1, 'A', 'B', 5, 10)
    e2 = Edge(2, 'B', 'C', 5, 10)
    e3 = Edge(3, 'C', 'D', 5, 10)
    return [e1, e2, e3]


@pytest.fixture
def col_names():
    return ["LinkId", "Start", "End", "Capacity", "Weight"]


"""
TODO: This might be too complicated for a test function
"""


def test_data_creation(edges, col_names):
    df = create_mock_data()
    for i, edge in enumerate(edges):
        row = df.iloc[i]

        for col_name in col_names[1:]:
            match col_name:
                case "Start":
                    assert row["Start"] == edges[i].node_1
                case "End":
                    assert row["End"] == edges[i].node_2
                case "Capacity":
                    assert row["Capacity"] == edges[i].capacity
                case "Weight":
                    assert row["Weight"] == edges[i].weight
                case _:
                    raise Exception(f"Unknown column name found in Edge class. Col found was {col_name}")


if __name__ == '__main__':
    e = edges()
    f = col_names()
    test_data_creation(e, f)
