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
        ('Hello world', 'Melly', 20, 'India', 15)
    ]
cursor.executemany("INSERT INTO orders (book_name, customer_name, price, country, sales_amount) VALUES (?, ?, ?, ?, ?);", orders_data)

#challenge One : 
query = """SELECT country, SUM(sales_amount) AS total_sales
            FROM orders
            GROUP BY country;
            """
results = cursor.execute(query)
for row in results.fetchall():
    print(row)

# Challenge Two: Customer with Most Orders 
second_query = f"""SELECT TOP 1 customer_name
            FROM Orders
            GROUP BY customer_name
            ORDER BY COUNT(order_number) DESC;
            LIMIT 1;
        """
res = cursor.execute(second_query)
for row in res.fetchall():
    print("\nCustomer with Most Orders:")
    print(row[2])
conn.commit()
cursor.close()
conn.close()
