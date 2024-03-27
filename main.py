import os.path

import typer
import pandas

app = typer.Typer()


@app.command()
def upload_csv():
    path: str = input("Please paste the path to your csv: ")
    df = None
    if os.path.isfile(path):
        df = pandas.read_csv(path)
        print(df.values)
    else:
        print("We cannot find the file that you have entered")
        exit()


if __name__ == '__main__':
    app()
