import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ldn_database.db')
cursor = conn.cursor()

# Add the address column to the customers table if it doesn't exist
cursor.execute("PRAGMA table_info(customers);")
columns = cursor.fetchall()
address_column_exists = any(column[1] == 'address' for column in columns)

if not address_column_exists:
    cursor.execute("ALTER TABLE customers ADD COLUMN address TEXT;")

#Insert a new customers 
cursor.execute("INSERT INTO customers (first_name, last_name, email, city) VALUES ('Souad', 'Ldn', 'souad@example.com', 'London');")
cursor.execute("INSERT INTO customers (first_name, last_name, email, city) VALUES ('hala', 'Ldn', 'souad@example.com', 'London');")
#Update the adrress

cursor.execute("UPDATE customers SET address = '101' WHERE first_name = 'Souad' AND last_name = 'Ldn';")
cursor.execute("UPDATE customers SET address = '111' WHERE first_name = 'hala' AND last_name = 'Ldn';")

#Run this part of code when you want to delete inactive customers 
# Delete customers with NULL address
#cursor.execute("DELETE FROM customers WHERE address IS NULL;")

conn.commit()
cursor.close()
conn.close()
