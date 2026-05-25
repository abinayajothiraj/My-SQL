import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Abi1504oreo!",
    database="mydatabases"
)

mycursor = mydb.cursor()

# INSERT INTO: is a sql statement used to add records (rows)into a table.

sql = ("INSERT INTO customers(name,address) VALUES(%s,%s)")

val = ("Abi", "Chennai") # this tuple contains actual values

mycursor.execute(sql, val) # execute() sends the sql query and values to mysql server for excution
mydb.commit() # permanently saves changes
print(mycursor.rowcount , "records inserted.")

"""
why do we use %s ?
    % acts as a placeholder for values. it helps to safely insert dynamic data into sql queries
    using %s helps to prevent : SQL INJECTION
2. matching happens like this:
    %s -> Abi
    %s -> Chennai
    
3. why is commit() important in mysql?
    commit() permanently saves changes to the database.
    without commit() inserted data will not be stored permanently.-> why?
    because Mysql uses TRANSACTIONS : changes remain temporary until committed. 

4.what is rowcount?
    rowcount returns the number of rows affected by the query.
"""

# II) INSERT MULTIPLE ROWS: We use executemany()

vals = [
    ("Abi", "Chennai"),
    ("Hoshi","LA"),
    ("Joshua","LA"),
    ("klaus", "New Orleans"),
    ("Hayley","New York"),
    ("Joe","Korea")
]

mycursor.executemany(sql, vals)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
# mycursor.execute("DELETE FROM customers WHERE name = 'Abi' ")
# mydb.commit()
# print(mycursor.rowcount, "record deleted.")


"""
1. executemany() - executes the same sql query  multiple times using different values
2. why it is better? executemany() is faster and more efficient for inserting multiple rows.

"""

# lastrowid  - returns the ID of the last inserted row

print(" Inserted ID: ", mycursor.lastrowid)