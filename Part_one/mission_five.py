import sqlite3
conn = sqlite3.connect('ldn_database.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
                   id INTEGER PRIMARY KEY,
                   book_name TEXT,
                   customer_name TEXT,
                   price REAL,
                   country TEXT,
                   sales_amount REAL
                )""")

orders_data = [
        ('Harry Potter and the Philoso', 'Mohammed', 23.5, 'UK', 10),
        ('1984', 'Dain', 14.99, 'USA', 5),  
        ('Hello world', 'Melly', 20, 'India', 15),
        ('1984', 'Joe', 14.99, 'India', 19),
        ('1984', 'melena', 14.99, 'India', 2),
        ('1984', 'elon', 14.99, 'USA', 7)
    ]
cursor.executemany("INSERT INTO orders (book_name, customer_name, price, country, sales_amount) VALUES (?, ?, ?, ?, ?);", orders_data)
# Challenge one  
query = """
        SELECT book_name, sales_amount
        FROM orders
        WHERE sales_amount > (
        SELECT AVG(sales_amount)
        FROM orders
        );
        """

results = cursor.execute(query)
print("Books Sold Above Average Sales:")
for row in results.fetchall():
  print(row)

# Challenge Two 
    

cursor.close()
conn.close()