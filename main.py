import os.path
import typer
import pandas as pd
from GraphCompontents.Graph import Graph

app = typer.Typer()


@app.command()
def create_graph():
    path: str = input("Please paste the path to your csv: ")
    if os.path.isfile(path):
        df = pd.read_csv(path)
        g = Graph()
        # this is a bit ugly
        Graph.create_nodes_from_df(df, g)
        Graph.assign_neighbours(df, g.nodes)
        print(f'The graph with id {g.graph_id} was successfully created')
    else:
        print("We cannot find the file that you have entered")
        exit()


if __name__ == '__main__':
    app()
