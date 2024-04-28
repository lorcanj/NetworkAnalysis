import os.path
import typer
import pandas as pd
import json

import DB.InMemoryDB.SessionData
from GraphCompontents.Graph import Graph

app = typer.Typer()

# global variable to store the session data, so that it can be accessed via other commands
session_data = None


@app.command()
def create_graph():
    global session_data
    path: str = input("Please paste the path to your csv: ")
    if os.path.isfile(path):
        df = pd.read_csv(path)
        g = Graph()
        # this is a bit ugly
        Graph.create_nodes_from_df(df, g)
        print(f'The graph with id {g.graph_id} was successfully created')
        graph_json = json.dumps(g.to_dict(), indent=4)
        if session_data:
            cursor = session_data.connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS graphs (id STRING PRIMARY KEY, graph TEXT)")
            cursor.execute("INSERT INTO graphs (graph) VALUES (?)", (graph_json,))
            cursor.execute("SELECT * FROM graphs")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    else:
        print("We cannot find the file that you have entered")
        exit()


@app.callback()
def session_callback():
    global session_data
    if not session_data:
        session_generator = DB.InMemoryDB.SessionData.manage_session()
        session_data = next(session_generator)
    return session_data


@app.command()
def verify_input():
    pass


if __name__ == '__main__':
    app()
