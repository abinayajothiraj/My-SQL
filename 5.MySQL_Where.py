import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Abi1504oreo!",
    database ="mydatabases"

)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = 'LA'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

"""
WHERE clause - is used to filter records based on a condition.
                it retrives only rows that match the specified condition.
                retrives only required data instead of all records.
                it improves performance and reduces unnecessary data retrival.

"""

# ii) LIKE - is used for pattern matching in sql.It helps search partial text values.
# eg: LIKE "%New%" - find rows where address contains the word 'New' anywhere.

sql1 = "SELECT * FROM customers WHERE address LIKE '%New%'"
mycursor.execute(sql1)
myresult1 = mycursor.fetchall()
for x in myresult1:
    print(x)

"""
1. what is % in SQL LIKE?
     % is a wildcard character representing zero or more characters
eg1: starts with:
    LIKE 'A%'
matches:
    Abi
    Amy
    Alex
eg2: Ends with:
    LIKE '%A'
matches:
    LA
eg3: contains:
        LIKE '%New%'
matches:
    New york
    New orleans
"""