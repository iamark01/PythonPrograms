from mysql.connector import (connection)
import json

# establishing the connection
conn = connection.MySQLConnection(user='root', password='@taurKhan1', host='127.0.0.1')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

'''# Dropping database MYDATABASE if already exists.
cursor.execute("DROP database IF EXISTS MyDatabase")

# Preparing query to create a database
sql = "CREATE database MYDATABASE"

# Creating a database
cursor.execute(sql)

# Retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

'''
# Use one DB and create table
print("Creating tables in mydatabase")
cursor.execute("USE mydatabase")

# Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Creating table as per requirement
sql = '''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)

# Insert records in Employee table
sql = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES(%s, %s, %s, %s, %s)"
val = [('John', 'Wick', 36, 'M', 320000), ('Winston', 'Churchill', 50, 'M', 450300)
    , ('John', 'Travolta', 46, 'M', 210000), ('Hillary', 'Clinton', 26, 'F', 320139)]

cursor.executemany(sql, val)
conn.commit()
print(cursor.rowcount, "rows inserted.")

sql = "UPDATE EMPLOYEE SET INCOME = %s WHERE FIRST_NAME = %s"
val = (200000, "John")
cursor.execute(sql, val)
conn.commit()
print(cursor.rowcount, "row(s) affected.")

# Creating table as per requirement
sql = '''SELECT * FROM EMPLOYEE'''
cursor.execute(sql)

recordSet = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
json_string = json.dumps(recordSet, indent=4)
print(json_string)


# Closing the connection
conn.close()
