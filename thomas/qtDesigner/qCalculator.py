import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, 
                             QGridLayout, QLCDNumber)

# sudo apt-get install python3-pyqt5

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        self.setGeometry(750, 300, 400, 300)
        self.setWindowTitle('QGridLayout-QLCDNumber-calculator')

        grid = QGridLayout()
        self.setLayout(grid)        

        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        grid.setSpacing(10)

        names = ['Cls', 'Bc', '',  'Close',
                 '7',   '8',  '9', '/',
                 '4',   '5',  '6', '*',
                 '1',   '2',  '3', '-',
                 '0',   '.',  '=', '+']

        positions = [(i,j) for i in range(4,9) for j in range(4,8)]

        for position, name in zip(positions, names):
            print("position=`{}`, name=`{}`".format(position, name))
            if name == '':
                continue

            button = QPushButton(name)

            grid.addWidget(button, *position)

            button.clicked.connect(self.Cli)

        self.show()

    def Cli(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())