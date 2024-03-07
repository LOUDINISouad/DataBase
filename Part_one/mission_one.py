import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ldn_database.db')
cursor = conn.cursor()

# Query to select customers from a specific city and order by last name
query = """
    SELECT * 
    FROM customers 
    WHERE city = 'New York' 
    ORDER BY last_name;
"""

# Execute the query
results = cursor.execute(query)

# Fetch all the results and print them
for row in results.fetchall():
    print(row)

# Close the cursor
cursor.close()

# Close the connection to the database
conn.close()
