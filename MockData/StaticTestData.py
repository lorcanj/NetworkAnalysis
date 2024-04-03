import pandas as pd
import pytest


@pytest.fixture
def input_test_size():
    return 15


"""
Create a copy of an example csv file that contains information modelling a network
TODO: An ugly reconstruction of the csv file, will re-do this in a nicer way
"""


def create_mock_data(input_test_size) -> pd.DataFrame:
    # might want to change this to just set the index of the df rather than a different column
    column_names: list[str] = ["start", "end", "capacity", "weight"]
    index: list[int] = [_ for _ in range(1, input_test_size)]
    df = pd.DataFrame(columns=column_names, index=index)
    # really should change this to dict and then pass it to the dataframe
    capacity: list[int] = [10 for _ in range(input_test_size-1)]
    weights: list[int] = [5, 5, 5, 5, 5, 5, 5, 5, 1, 5, 1, 5, 3, 1]
    starts: list[str] = ["A", "B", "C", "D", "E", "G", "H", "A", "B", "C", "D", "I", "F", "A"]
    ends: list[str] = ["B", "C", "D", "E", "F", "H", "A", "I", "I", "G", "F", "G", "G", "J"]
    col_names: dict[str, list[int | str]] = {"capacity": capacity, "weight": weights,
                                             "start": starts, "end": ends}
    for name in col_names:
        df[name] = col_names[name]

    return df


if __name__ == '__main__':
    create_mock_data()
