import mysql.connector
#create connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Abi1504oreo!",

)
#create cursor
mycursor = mydb.cursor()

#create database name called test
mycursor.execute("CREATE DATABASE IF NOT EXISTS test")
print("Database created successfully")

# SHOW DATABASES
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
