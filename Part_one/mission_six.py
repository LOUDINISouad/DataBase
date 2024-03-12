import sqlite3

conn = sqlite3.connect('ldn_database.db') 
cursor = conn.cursor()
# First Challenge 
cursor.execute("""
  SELECT 
    first_name || ' ' || last_name AS full_name
  FROM customers
""")

results = cursor.fetchall()

for result in results:
  print(result[0])
  


  
conn.close()