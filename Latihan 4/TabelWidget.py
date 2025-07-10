import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(os.path.join(os.path.dirname(__file__), 'TabelWid.ui'), self)
        self.setWindowTitle('DATA MAHASISWA')
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels([
            "NPM", "Nama Lengkap", "Nama Panggilan", "Telepon", "Email", "Kelas", "Mata Kuliah", "Lokasi Kampus"
        ])
        self.sqlload()  # Load data saat start

        # Fungsi Tombol
        self.btnhapus.clicked.connect(self.hapusData)
        self.btnsimpan.clicked.connect(self.simpanData)
        self.btnedit.clicked.connect(self.editData)
        self.btnbatal.clicked.connect(self.batal)
        self.tableWidget.cellClicked.connect(self.pilihData)

    def sqlload(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM mahasiswa ORDER BY nama_lengkap ASC")
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.label_9.setText("Data Berhasil Ditampilkan")

        except mc.Error:
            self.label_9.setText("Data Gagal Ditampilkan")

    def simpanData(self):
        npm = self.lineEdit.text()
        nama_lengkap = self.lineEdit_2.text()
        nama_panggilan = self.lineEdit_3.text()
        telepon = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        kelas = self.lineEdit_6.text()
        mata_kuliah = self.lineEdit_7.text()
        lokasi_kampus = self.lineEdit_8.text()

        if npm == "" or nama_lengkap == "":
            self.label_9.setText("Data tidak boleh kosong")
            return

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO mahasiswa(npm, nama_lengkap, nama_panggilan, telepon, email, kelas, mata_kuliah, lokasi_kampus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (npm, nama_lengkap, nama_panggilan, telepon, email, kelas, mata_kuliah, lokasi_kampus)
            mycursor.execute(sql, val)
            mydb.commit()
            self.label_9.setText("Data berhasil disimpan")
            self.sqlload()
            self.batal()
        except mc.Error:
            self.label_9.setText("Gagal menyimpan data")

    def pilihData(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            return

        self.lineEdit.setText(self.tableWidget.item(row, 0).text())        # NPM
        self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())      # Nama Lengkap
        self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())      # Nama Panggilan
        self.lineEdit_4.setText(self.tableWidget.item(row, 3).text())      # Telepon
        self.lineEdit_5.setText(self.tableWidget.item(row, 4).text())      # Email
        self.lineEdit_6.setText(self.tableWidget.item(row, 5).text())      # Kelas
        self.lineEdit_7.setText(self.tableWidget.item(row, 6).text())      # Mata Kuliah
        self.lineEdit_8.setText(self.tableWidget.item(row, 7).text())      # Lokasi Kampus

    def editData(self):
        row = self.tableWidget.currentRow()
        if row < 0 or self.tableWidget.item(row, 0) is None:
            self.label_9.setText("Pilih data terlebih dahulu sebelum mengedit")
            return

        npm_lama = self.tableWidget.item(row, 0).text()
        npm_baru = self.lineEdit.text()
        nama_lengkap = self.lineEdit_2.text()
        nama_panggilan = self.lineEdit_3.text()
        telepon = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        kelas = self.lineEdit_6.text()
        mata_kuliah = self.lineEdit_7.text()
        lokasi_kampus = self.lineEdit_8.text()

        if npm_baru == "" or nama_lengkap == "":
            self.label_9.setText("Form tidak boleh kosong")
            return
        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_mhs")
            mycursor = mydb.cursor()
            sql = "UPDATE mahasiswa SET npm=%s, nama_lengkap=%s, nama_panggilan=%s, telepon=%s, email=%s, kelas=%s, mata_kuliah=%s, lokasi_kampus=%s WHERE npm=%s"
            val = (npm_baru, nama_lengkap, nama_panggilan, telepon, email, kelas, mata_kuliah, lokasi_kampus, npm_lama)
            mycursor.execute(sql, val)
            mydb.commit()
            self.label_9.setText("Data berhasil diubah")
            self.sqlload()
            self.batal()
        except mc.Error:
            self.label_9.setText("Gagal ubah data")

    def hapusData(self):
        row = self.tableWidget.currentRow()
        if row < 0 or self.tableWidget.item(row, 0) is None:
            self.label_9.setText("Pilih data terlebih dahulu untuk dihapus")
            return

        npm = self.tableWidget.item(row, 0).text()
        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_mhs")
            mycursor = mydb.cursor()
            sql = "DELETE FROM mahasiswa WHERE npm=%s"
            mycursor.execute(sql, (npm,))
            mydb.commit()
            self.label_9.setText("Data berhasil dihapus")
            self.sqlload()
            self.batal()
        except mc.Error:
            self.label_9.setText("Gagal hapus data")

    def batal(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.tableWidget.clearSelection()
        self.label_9.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())
