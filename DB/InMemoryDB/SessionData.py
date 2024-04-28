import sqlite3


class SessionData:
    def __init__(self):
        self.connection = None

    def initialise_database(self):
        self.connection = sqlite3.connect(':memory:')

    def close_connection(self):
        if self.connection:
            self.connection.close()


def manage_session():
    # Initialise the database for the session
    print("Creating in-memory database for the session")
    session_data = SessionData()
    session_data.initialise_database()
    # pause execution here when first called
    # next call will continue from after the yield and will close the connection
    yield session_data
    print("Closing in-memory database")
    session_data.close_connection()
