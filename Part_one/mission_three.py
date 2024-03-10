import sqlite3

conn = sqlite3.connect('ldn_database.db')
cursor = conn.cursor()

query = """SELECT books.title, authors.name
        FROM books
        INNER JOIN authors ON books.author_id = authors.author_id"""

query_join = """SELECT authors.author_id, books.title
                FROM authors
                LEFT JOIN books ON books.author_id = authors.author_id"""



results = cursor.execute(query)
print("\nResults of inner join:")
for row in results.fetchall():
    print(row)

results = cursor.execute(query_join)
print("\nResults of left join:")
for row in results.fetchall():
    print(row)

conn.commit()
cursor.close()
conn.close()
