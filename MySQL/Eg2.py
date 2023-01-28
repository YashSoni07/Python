import mysql.connector

conn = mysql.connector.connect(host="localhost", database='fisttable', user='root', password='root')

# Creating the Cursor for Connection
cursor = conn.cursor()

create = 'create table employee(eNo int, eName varchar(40), eAge int, eCity varchar(40), eCountry varchar(40));'
# Using cursor to execute one or more queries
print("Table Created")

# Closing the cursor
cursor.close()

# Closing the Connection Object
conn.close()