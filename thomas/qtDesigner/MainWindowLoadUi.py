from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

        self.lcdNumber = self.findChild(QtWidgets.QLCDNumber, 'lcdNumber')

        self.incButton = self.findChild(QtWidgets.QPushButton, 'incButton')
        self.decButton = self.findChild(QtWidgets.QPushButton, 'decButton')

        self.incButton.clicked.connect(self.inc)
        self.decButton.clicked.connect(self.dec)

    def inc(self):
        self.lcdNumber.display(self.lcdNumber.value() + 1)

    def dec(self):
        self.lcdNumber.display(self.lcdNumber.value() - 1)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()