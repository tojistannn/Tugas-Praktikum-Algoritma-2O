from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Initialize and configure custom UI elements
        self.setWindowTitle("PyQt Qwidget class")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWidget()
    window.show()
    sys.exit(app.exec_())
