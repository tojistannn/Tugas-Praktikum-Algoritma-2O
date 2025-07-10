import mysql.connector

mydb = mysql.connector.connect(
    host = ("localhost"),
    user = ("root"),
    password = (""),
    database = ("db_python2O")
)

mycursor = mydb.cursor()
sql = "insert into customer (nama, alamat) values (%s, %s)"
val = ("budi", "Banjarmasin")
mycursor.execute(sql, val)
mydb.commit()
print (mycursor.rowcount,"data berhasil diinsert") 