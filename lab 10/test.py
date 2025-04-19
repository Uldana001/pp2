# import psycopg2

# conn = psycopg2.connect(
#     dbname="new_database",  # Replace with your database name
#     user="myuser",    # Replace with your PostgreSQL username
#     password="myuser",# Replace with your PostgreSQL password
#     host="localhost",        # Use the IP of the server if not local
#     port="5432"              # Default PostgreSQL port
# )

# # Create a cursor object to interact with the database
# cur = conn.cursor()

# # Execute a query
# cur.execute("SELECT version();")

# # Fetch and print the result
# db_version = cur.fetchone()
# print("Connected to:", db_version)

# # Close the connection
# cur.close()
# conn.close()

# def get_connection():
#     conn = psycopg2.connect(
#     dbname="new_database",  # Replace with your database name
#     user="myuser",    # Replace with your PostgreSQL username
#     password="myuser",# Replace with your PostgreSQL password
#     host="localhost",        # Use the IP of the server if not local
#     port="5432"              # Default PostgreSQL port
#     )
#     return conn

# cur = get_connection().cursor()

# cur.execute("SELECT table_name FROM information_schema.tables;")
# tables = cur.fetchall()

# print("Tables:", [table[0] for table in tables])

# cur.close()
# conn.close()

import os

file_path = 'Desfskfk/dsfsdkfjs/sjfdjsd/etxtt.csv'

a = os.path.splitext(file_path)

print(a)