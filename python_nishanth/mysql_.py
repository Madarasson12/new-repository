import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user ='root',
    password='roottoor',
    database='nural_schema',
)
print('connected to database')