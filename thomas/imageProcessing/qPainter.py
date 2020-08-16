import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt, QPoint 

FILL_COLOR = '#ff0000'

# https://www.learnpyqt.com/blog/implementing-qpainter-flood-fill-pyqt5pyside/
# https://www.learnpyqt.com/courses/custom-widgets/bitmap-graphics/

class Window(QtWidgets.QLabel):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.p = QtGui.QPixmap(600, 500)
        self.p.fill(QtGui.QColor('#ffffff')) # Fill entire canvas.
        self.setPixmap(self.p)

    def paintEvent(self, event): 
        # create custom QPainter‚
        self.my_painter = QPainter() 
        # start and set my_painter
        self.my_painter.begin(self) 
        self.my_painter.setRenderHint(self.my_painter.TextAntialiasing, True)
        self.my_painter.setRenderHint(self.my_painter.Antialiasing, True)
        #set color for pen by RGB
        self.my_painter.setPen(QColor(0,0,255)) 
        # draw a text on fixed coordinates
        self.my_painter.drawText(220,100, "Text at 220, 100 fixed coordinates") 
        # draw a text in the centre of my_painter   
        self.my_painter.drawText(event.rect(), Qt.AlignCenter, "Text centerd in the drawing area") 
        #set color for pen by Qt color  
        self.my_painter.setPen(QPen(Qt.green, 1)) 
        # draw a ellipse
        self.my_painter.drawEllipse(QPoint(100,100),60,60) 
        # set color for pen by property
        self.my_painter.setPen(QPen(Qt.blue, 3, join = Qt.MiterJoin)) 
        # draw a rectangle
        self.my_painter.drawRect(80,160,100,100) 
        # set color for pen by Qt color 
        self.my_painter.setPen(QPen(Qt.red, 2))
        # set brush 
        self.my_brush = QBrush(QColor(33, 33, 100, 255), Qt.DiagCrossPattern)
        self.my_painter.setBrush(self.my_brush)
        # draw a rectangle and fill with the brush 
        self.my_painter.drawRect(300, 300,180, 180)
        self.my_painter.end() 

    # def mouseMoveEvent(self, e):

        # queue the points and lets draw in pantEvent only

        # self.my_painter.setPen(QColor(255,0,0))

        # self.my_painter.drawPoint(e.x(), e.y())

        # self.update()

app = QtWidgets.QApplication(sys.argv)
w = Window()
w.show()
app.exec_()