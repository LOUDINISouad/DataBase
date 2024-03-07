import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ldn_database.db')
cursor = conn.cursor()

# Create authors table
cursor.execute("INSERT INTO authors (name, country) VALUES ('J.K. Rowling', 'United Kingdom');")
# Create books table
cursor.execute("INSERT INTO authors (name, country) VALUES ('George Orwell', 'United Kingdom');")

# Create customers table
cursor.execute("INSERT INTO books (title, author_id, year_published, price) VALUES ('Harry Potter and the Philoso', 1, 1998, 23.5);")
cursor.execute("INSERT INTO books (title, author_id, year_published, price) VALUES ('1984', 2, 1949, 14.99);")

cursor.execute("INSERT INTO customers (first_name, last_name, email, city) VALUES ('John', 'Doe', 'john.doe@example.com', 'New York');")
cursor.execute("INSERT INTO customers (first_name, last_name, email, city) VALUES ('Jane', 'Doe', 'jane.doe@example.com', 'Los Angeles');")

# Commit the transaction
conn.commit()

# Close the cursor
cursor.close()

# Close the connection to the database
conn.close()
