import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abi1504oreo!",
    database="mydatabases"
)

print("Connected Successfully")

mycursor = mydb.cursor()

# Create table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS students(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
)
""")

print("Table created successfully")