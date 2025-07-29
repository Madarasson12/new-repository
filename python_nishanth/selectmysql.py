import mysql.connector

def insert_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user='root',
        password='roottoor',
        database='nural_schema'
    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from user")

    result = mycursor.fetchall()
    for row in result:
        print(row)
insert_data()
