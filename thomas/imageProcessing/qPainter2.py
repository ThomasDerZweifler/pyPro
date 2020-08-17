import sys

import sympy as sp

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QPixmap, QBrush, QPen, QColor, QImage
from PyQt5.QtCore import Qt, QPoint, QRect

# http://openbook.rheinwerk-verlag.de/python/39_006.html

# book:
# https://www.learnpyqt.com/courses/custom-widgets/creating-your-own-custom-widgets/

FILL_COLOR = '#ff0000'

def tand(x):
        return sp.tan(x * sp.pi / 180)

def sind(x):
    return sp.sin(x * sp.pi / 180)

def cosd(x):
    return sp.cos(x * sp.pi / 180)

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image processing'
        self.left = 10
        self.top = 10
        self.width = 1240
        self.height = 800
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumWidth(self.width)
        self.setMinimumHeight(self.height)

        self.myWidget = MyWidget(self)

        self.setCentralWidget(self.myWidget)

        self.show()

        self.myWidget.rot(45)

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.title = 'PyQt5 painter'
        self.grafik = QImage("img/cinzano.ppm")
        self.copy = self.grafik.copy()
        self.copy.fill(0)
        self.ziel = QtCore.QRect(40, 40, 640, 640)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.show()

    def rot(self, angle):
        self.rotate(self.grafik, self.copy, angle)

    def rotate(self, source, dest, angle) :
        width = source.width()
        height = source.height()
        y = 1
        while y < height:
            x = 1
            while x < width: 

                inputRow = y * cosd(angle) - x * sind(angle)
                inputCol = y * sind(angle) + x * cosd(angle)

                if inputRow >= 0 and inputRow < height and inputCol >= 0 and inputCol < width:
                    color = QColor.fromRgb(source.pixel(inputCol, inputRow))
                    dest.setPixel(x, y, color.rgba())
                    super().repaint()

                x = x+5
            y = y+5

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(self.ziel, self.copy)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())