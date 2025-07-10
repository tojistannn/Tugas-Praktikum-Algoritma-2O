import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
app = QApplication([])
window = QWidget()
window.setWindowTitle("PyQt5")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("Hello World!", parent=window)
helloMsg.move(60, 15)
window.show()
sys.exit(app.exec_())