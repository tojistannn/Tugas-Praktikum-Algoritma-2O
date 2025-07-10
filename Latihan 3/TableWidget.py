import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(os.path.join(os.path.dirname(__file__), 'TabelWid.ui'), self)
        self.setWindowTitle('PYTHON GUI TABLEWIDGET')
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        self.sqlload()  # Load data saat start

        # Fungsi Tombol
        self.btnhapus.clicked.connect(self.hapusData)
        self.btnsimpan.clicked.connect(self.simpanData)
        self.btnedit.clicked.connect(self.editData)
        self.btnloaddata.clicked.connect(self.sqlload)
        self.btnbatal.clicked.connect(self.batal)
        self.tableWidget.cellClicked.connect(self.pilihData)  # Fix typo: cellCliked → cellClicked

    def hapus(self):
        self.tableWidget.clear()
        self.label_3.setText("Tabel Dibersihkan")

    def sqlload(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_latihan"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM mahasiswa ORDER BY nama ASC")
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.label_3.setText("Data Berhasil Ditampilkan")

        except mc.Error:
            self.label_3.setText("Data Gagal Ditampilkan")

    def simpanData(self):
        nama = self.lineEdit.text()  # Fix: .Text() → .text()
        jurusan = self.lineEdit_2.text()

        if nama == "" or jurusan == "":
            self.label_3.setText("Data tidak boleh kosong")
            return

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_latihan"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO mahasiswa(nama, jurusan) VALUES (%s, %s)"
            val = (nama, jurusan)
            mycursor.execute(sql, val)
            mydb.commit()
            self.label_3.setText("Data berhasil disimpan")
            self.sqlload()
            self.batal()
        except mc.Error:
            self.label_3.setText("Gagal menyimpan data")

    def pilihData(self):
        row = self.tableWidget.currentRow()

        if row < 0:
            return

        item_nama = self.tableWidget.item(row, 0)
        item_jurusan = self.tableWidget.item(row, 1)

        if item_nama and item_jurusan:
            self.lineEdit.setText(item_nama.text())
            self.lineEdit_2.setText(item_jurusan.text())

    def editData(self):
        row = self.tableWidget.currentRow()

        if row < 0 or self.tableWidget.item(row, 0) is None:
            self.label_3.setText("Pilih data terlebih dahulu sebelum mengedit")
            return

        namaLama = self.tableWidget.item(row, 0).text()
        namaBaru = self.lineEdit.text()
        jurusanBaru = self.lineEdit_2.text()

        if namaBaru == "" or jurusanBaru == "":
            self.label_3.setText("Form tidak boleh kosong")
            return
        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_latihan")
            mycursor = mydb.cursor()
            sql = "UPDATE mahasiswa SET nama=%s, jurusan=%s WHERE nama=%s"
            val = (namaBaru, jurusanBaru, namaLama)
            mycursor.execute(sql, val)
            mydb.commit()
            self.label_3.setText("Data berhasil diubah")
            self.sqlload()
            self.batal()
        except mc.Error:
            self.label_3.setText("Gagal ubah data")

    def hapusData(self):
        row = self.tableWidget.currentRow()

        if row < 0 or self.tableWidget.item(row, 0) is None:
            self.label_3.setText("Pilih data terlebih dahulu untuk dihapus")
            return

        nama = self.tableWidget.item(row, 0).text()

        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_latihan")
            mycursor = mydb.cursor()
            sql = "DELETE FROM mahasiswa WHERE nama=%s"
            mycursor.execute(sql, (nama,))
            mydb.commit()
            self.label_3.setText("Data berhasil dihapus")
            self.sqlload()
            self.batal()
        except mc.Error:
            self.label_3.setText("Gagal hapus data")

    def batal(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.tableWidget.clearSelection()
        self.label_3.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())
