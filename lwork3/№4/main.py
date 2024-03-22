import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication

class Pseudonym(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('qt.ui', self)
 
        self.startButton.clicked.connect(self.start)
        self.takeButton.clicked.connect(self.take)
 
    def start(self):
        self.kamney = int(self.stones.text())
        self.remainLcd.display(self.kamney)
        self.listWidget.clear()
        self.resultLabel.setText('')
 
    def take(self):
        self.take_chel = int(self.takeInput.text())
        if self.kamney - self.take_chel == 0:
            self.listWidget.addItem(f'Игрок взял - {self.take_chel}')
            self.remainLcd.display(self.kamney - self.take_chel)
            self.resultLabel.setText('Победа пользователя!')
        else:
            self.kamney -= self.take_chel
            b = self.kamney % 4
            if b == 0:
                b = 2
            if b == 1:
                self.take_komp = 1
            else:
                self.take_komp = b
            self.kamney -= self.take_komp
            self.remainLcd.display(self.kamney)
            self.listWidget.addItem(f'Игрок взял - {self.take_chel}')
            self.listWidget.addItem(f'Компьютер взял - {self.take_komp}')
            if self.kamney == 0:
                self.resultLabel.setText('Победа компьютера!')
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())