import sqlite3

conn = sqlite3.connect('ldn_database.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
                   id INTEGER PRIMARY KEY,
                   book_name TEXT,
                   customer_name TEXT,
                   price REAL,
                   country TEXT,
                   sales_amount REAL,
                   order_date TEXT
                )""")

orders_data = [
    ('Harry Potter and the Philosopher\'s Stone', 'Mohammed', 23.5, 'UK', 10),
    ('1984', 'Dain', 14.99, 'USA', 5),  
    ('Hello world', 'Melly', 20, 'India', 15),
    ('1984', 'Joe', 14.99, 'India', 19),
    ('1984', 'melena', 14.99, 'India', 2),
    ('1984', 'elon', 14.99, 'USA', 7)
]
cursor.executemany("INSERT INTO orders (book_name, customer_name, price, country, sales_amount) VALUES (?, ?, ?, ?, ?);", orders_data)

cursor.execute("PRAGMA table_info(orders)")
table_info = cursor.fetchall()
column_names = [column[1] for column in table_info]

if "order_date" not in column_names:
    cursor.execute("ALTER TABLE orders ADD COLUMN order_date TEXT")

dates_to_insert = [
    ('2024-03-10',),
    ('2024-03-11',),
    ('2024-03-12',),
    ('2024-03-12',),
    ('2024-03-11',),
    ('2024-03-10',)
]
cursor.executemany("UPDATE orders SET order_date = ?", dates_to_insert)

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
    
query = """
    SELECT customer_name, 
           (SELECT MAX(order_date) FROM orders AS o2 WHERE o1.customer_name = o2.customer_name) AS last_order_date
    FROM orders AS o1
    GROUP BY customer_name;
"""

results = cursor.execute(query)
print("\nCustomer Last Order Dates:")
for row in results.fetchall():
    print(row)

cursor.close()
conn.close()
