from utils.database_connection import DatabaseConnection, connect

def create_books_table():
    with connect() as connection:
        connection.cursor().execute(
            """CREATE TABLE IF NOT EXISTS `books` (name text primary key, author text, read integer)""")


def add_new_book(name, author):
    with DatabaseConnection() as connection:
        connection.cursor().execute("INSERT INTO `books` VALUES (?, ? , 0)", (name, author))


def get_all_books():
    with DatabaseConnection() as connection:
        records = connection.cursor().execute("SELECT * FROM `books`").fetchall()
    return [{
        'name': name,
        'author': author,
        'read': bool(int(read))
    }
        for name, author, read in records]


def mark_as_read(name):
    with DatabaseConnection() as connection:
        connection.cursor().execute("UPDATE books SET read=1 WHERE name=?", (name,))


def delete_book(name):
    with DatabaseConnection() as connection:
        connection.cursor().execute("DELETE FROM books WHERE name=?", (name,))
