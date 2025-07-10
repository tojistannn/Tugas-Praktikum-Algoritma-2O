import mysql.connector

mydb = mysql.connector.connect(
    host = ("localhost"),
    user = ("root"),
    password = (""),
    database = ("db_mhs")
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE mahasiswa (nama varchar(200) NOT NULL, jurusan varchar(200))")
print ("Table berhasil dibuat!") 