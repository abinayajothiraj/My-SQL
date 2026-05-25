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


# create another table called customers

mycursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255)
)
""")

# show tables: to check whether table exists

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

"""
why tuple output?
 Mysql connector returns rows as tuples. 
 Each table name is returned as : ('customers',)

"""

#II) ALTER TABLE

"""
ALTER TABLE is used to modify an existing table structure.
eg: Add column, modify datatype, delete column, add primary key.
"""

mycursor.execute("ALTER TABLE students ADD COLUMN address VARCHAR(255) NOT NULL")