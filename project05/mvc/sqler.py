# -*- coding: utf-8 -*-


def sqler(user_id):
    import sqlite3

    con = sqlite3.connect('books_db.sqlite')
    cur = con.cursor()

    cur.execute(
        'SELECT users.name \
         FROM users \
         WHERE users.id = %d' % user_id
    )
    user_name = cur.fetchone()[0]

    books = []
    for row in cur.execute(
                    'SELECT books.title \
                     FROM books \
                     JOIN buy \
                     ON books.id = buy.book_id \
                     WHERE buy.user_id = %d' % user_id
    ):
        books.append(row[0])

    con.commit()

    return {
        'user_name': user_name,
        'books': books
    }