import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ldn_database.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO customers (first_name, last_name, email, city) VALUES ('Souad', 'Ldn', 'soaud@example.com', 'London');")

# Commit the transaction
conn.commit()

# Close the cursor
cursor.close()

# Close the connection to the database
conn.close()
