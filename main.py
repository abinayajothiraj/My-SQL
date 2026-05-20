import mysql.connector  # mysql.connector is the driver that allows to send sql queries,fetch,insert datas & update,delete records

# we use the connect() function from mysql.connector to connect python to mysql
# mydb creates a connection object , this connection object represents the communication btwn python application and mysql server
mydb = mysql.connector.connect(
    host="localhost",  # local host-> current machine which means mysql is running on your computer
    user="root", # root is the common default mysql username
    passwd="Abi1504oreo!", # password is for mysql authentication , this is required for security
    database = "mydatabases"
)

# username and password verify the identity of the user
print("Connected Successfully")
print(mydb)

