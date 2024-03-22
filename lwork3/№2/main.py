import sys
from qt import Ui_MainWindow
from PyQt6.QtWidgets  import QApplication, QMainWindow
 
 
class Plan(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
 
    def run(self):
        date = self.calendarWidget.selectedDate().toString("dd-MM-yyyy")
        plan = self.lineEdit.text()
        dt = self.timeEdit.time().toString()
        self.listWidget.addItem(f'{date} {dt} - {plan}')
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    plan= Plan()
    plan.show()
    sys.exit(app.exec())