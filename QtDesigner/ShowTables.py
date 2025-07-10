import mysql.connector

mydb = mysql.connector.connect(
    host = ("localhost"),
    user = ("root"),
    password = (""),
    database = ("db_python2O")
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x) 