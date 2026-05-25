import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Abi1504oreo!",
    database="mydatabases"
)

mycursor = mydb.cursor()

#SELECT - retrieves datas from the database table

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

"""
SELECT - retrives data
*      - all columns
FROM customers -  retrives data from customers table

SELECT * FROM customers - get all rows and all columns from customers table

2. what is fetchall()?
 retrives all rows from the query result.
 
 
        SELECT - decides columns
        fetchall() - decides rows quantity
        
3. Does fetchall() retrieve columns or rows?
    fetchall() retrives all rows from the query result.
    the columns retrived depend on the SELECT statement used in the query.
"""

# fetchone() - retrives only one row from the query result. usually the first matching row.

myresult1 = mycursor.fetchone()
print(myresult1)

"""
how do you select only specific columns?
     we mention the column names after SELECT.
2. why not always use SELECT *?
     selecting only required columns improves performance and reduces unnecessary data retrieval
"""

mycursor.execute("SELECT name,address FROM customers")

"""
why SELECT queries not need commit()?
     because SELECT only retrieves data and does not modify the database.
     commit() is required only for INSERT, UPDATE , DELETE or other changes.
"""