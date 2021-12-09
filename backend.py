import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # primary key, jest pierwszy
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER ) ")
    conn.commit()
    conn.close()
# running function everytime we run frontend


# inserting data
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # null is about Id
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


# show the data
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


# need to add empty values to prevent error for not implementing argument
def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # select book if some of parameters equals
    cur.execute("SELECT * FROM book WHERE title = ? OR author=? OR year = ? OR isbn = ?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# deleting by id column name


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title =?, author=?,year=?,isbn=? WHERE id=?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
