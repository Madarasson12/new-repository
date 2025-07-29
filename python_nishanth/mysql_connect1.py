import mysql.connector

def inser_data(id, name, email):
    mydb = mysql.connector.connect(
        host="localhost",
        user='root',
        password='roottoor',
        database='nural_schema'
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO user(id, name, email) VALUES (%s, %s, %s)"
    val = (id, name, email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
    mycursor.close()
    mydb.close()

id = input("Enter the id: ")
name = input("Enter your name: ")
email = input("Enter your email: ")
inser_data(id, name, email)
