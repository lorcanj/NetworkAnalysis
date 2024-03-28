import pandas as pd

"""
Create a copy of an example csv file that contains information modelling a network
TODO: An ugly reconstruction of the csv file, will re-do this in a nicer way
"""


def create_mock_data() -> pd.DataFrame:
    # might want to change this to just set the index of the df rather than a different column
    column_names: list[str] = ["Start", "End", "Capacity", "Weight"]
    index: list[int] = [_ for _ in range(1, 14)]
    df = pd.DataFrame(columns=column_names, index=index)
    # really should change this to JSON and then pass it to the dataframe
    capacity: list[int] = [10 for _ in range(13)]
    weights: list[int] = [5, 5, 5, 5, 5, 5, 5, 5, 1, 5, 1, 5, 3]
    starts: list[str] = ["A", "B", "C", "D", "E", "G", "H", "A", "B", "C", "D", "I", "F"]
    ends: list[str] = ["B", "C", "D", "E", "F", "H", "A", "I", "I", "G", "F", "G", "G"]
    col_names: dict[str, list[int | str]] = {"Capacity": capacity, "Weight": weights,
                                             "Start": starts, "End": ends}
    for name in col_names:
        df[name] = col_names[name]

    return df


if __name__ == '__main__':
    create_mock_data()
