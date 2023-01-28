import mysql.connector

conn = mysql.connector.connect(host="localhost", database='yash', user='root', password='root')

print('Connection Tested')
conn.close()
