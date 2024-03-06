import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ldn_database.db')
cursor = conn.cursor()

# Create authors table
cursor.execute("""CREATE TABLE IF NOT EXISTS authors (
author_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
country TEXT);""")

# Create books table
cursor.execute("""CREATE TABLE IF NOT EXISTS books (
book_id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author_id INTEGER,
year_published INTEGER,
price DECIMAL(10, 2),
FOREIGN KEY (author_id) REFERENCES authors(author_id)
);""")
#Add indexing to book title
#cursor.execute("CREATE INDEX IF NOT EXISTS name ON books (title);")

res = cursor.execute("""SELECT
   *
FROM
   sqlite_master
WHERE
   type= 'index' and tbl_name = 'books' and name = 'name';""")
print(res.fetchone())


# Create customers table
cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
customer_id INTEGER PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT,
city TEXT
);""")


conn.commit()
cursor.close()
conn.close()
