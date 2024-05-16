import sqlite3


def create_table():
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    cur.execute("""CREATE TABLE Book(
    book_name text,
    book_author text,
    book_genre text
  )""")
    print("Done")

    connection.commit()
    connection.close()


def add_record(name, author, genre):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        cur.execute("INSERT INTO Book VALUES(?,?,?)", (name, author, genre))
    except:
        create_table()
        add_record(name, author, genre)

    connection.commit()
    connection.close()


def show_all():
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        return cur.execute("SELECT * FROM Book ORDER BY book_name ASC").fetchall()
    except:
        create_table()
        show_all()

    connection.commit()
    connection.close()


def show_one(word, mode):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        if mode == 1:
            cur.execute("SELECT * FROM Book WHERE book_name=?", (word,))
        elif mode == 2:
            cur.execute("SELECT * FROM Book WHERE book_author=?", (word,))
        elif mode == 3:
            cur.execute("SELECT * FROM Book WHERE book_genre=?", (word,))
        results = cur.fetchall()

        if results:
            return results
        else:
            return False
    except sqlite3.Error as e:
        return e
        create_table()

    connection.commit()
    connection.close()


def update_record(name, author, genre):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        cur.execute("UPDATE Book SET book_author = ? WHERE book_name = ?", (author, name))
    except:
        create_table()

    connection.commit()
    connection.close()


def delete_record(name):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        cur.execute("DELETE from Book WHERE book_name=?", (name,))
    except:
        create_table()

    connection.commit()
    connection.close()
