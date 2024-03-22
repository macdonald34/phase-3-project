import sqlite3
from contextlib import contextmanager

DATABASE_NAME = 'books.sqlite'


@contextmanager
def connect(database=DATABASE_NAME):
    connection = sqlite3.connect(database)
    yield connection
    connection.commit()
    connection.close()


class DatabaseConnection:

    def __init__(self, database_name=DATABASE_NAME):
        self.database_name = database_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type and not exc_val and not exc_tb:
            self.connection.commit()
        self.connection.close()