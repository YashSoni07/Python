import mysql.connector

conn = mysql.connector.connect(host="localhost", database="base1", usre="root", password="root")

if(conn):
    print("Connection Tested")
else:
    print("Connection Not Tested")
