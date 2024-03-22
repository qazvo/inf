import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('qt.ui', self)
        self.a = self.lineEdit.text()
        self.b = self.lineEdit_2.text()

        self.pushButton.clicked.connect(self.dobavit)

    def dobavit(self):
        self.listWidget.addItem(self.lineEdit.text())
        self.listWidget.addItem(self.lineEdit_2.text())
        

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
