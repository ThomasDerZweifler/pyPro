import math, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# https://wiki.python.org/moin/PyQt5/Threading%2C_Signals_and_Slots

class Window(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)        
        self.thread = Worker()
       
        self.startButton = QPushButton(self.tr("&Load image"))
        self.stopButton = QPushButton(self.tr("&Stop image loading"))
        self.stopButton.setEnabled(False)
        self.viewer = QLabel()
        self.viewer.setFixedSize(1200, 1200)

        self.thread.finished.connect(self.updateUi)
        #self.thread.terminated.connect(self.updateUi)
        self.thread.output['QRect', 'QImage'].connect(self.addImage)
        self.startButton.clicked.connect(self.makePicture)
        self.stopButton.clicked.connect(self.stopLoadingPicture)

        layout = QGridLayout()
        layout.addWidget(self.startButton, 0, 0)
        layout.addWidget(self.stopButton, 0, 1)
        layout.addWidget(self.viewer, 1, 0, 1, 3)
        self.setLayout(layout)        
        self.setWindowTitle(self.tr("Loading image by thread"))

    def makePicture(self):
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        pixmap = QPixmap(self.viewer.size())
        pixmap.fill(Qt.black)
        self.viewer.setPixmap(pixmap)
        self.thread.render("img/man.jpg")

    def stopLoadingPicture(self):
        self.stopButton.setEnabled(False)
        self.thread.__del__()

    def addImage(self, rect, image):    
        pixmap = self.viewer.pixmap()
        painter = QPainter()
        painter.begin(pixmap)
        painter.drawImage(rect, image)
        painter.end()
        self.viewer.update(rect)

    def updateUi(self):
        self.startButton.setEnabled(True)

class Worker(QThread):
    output = pyqtSignal(QRect, QImage)
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False

    def __del__(self):    
        self.exiting = True
        self.wait()

    def render(self, name):
        self.exiting = False
        self.name = name
        self.start()

    def run(self):        
        # Note: This is never called directly. It is called by Qt once the
        # thread environment has been set up.
     
        img = QPixmap(self.name).toImage()

        width = img.width()
        height = img.height()

        image = QImage(width, height,
                        QImage.Format_ARGB32)
        image.fill(qRgba(0, 0, 0, 0))

        y = 0
        while y < height:
            x = 0
            while x < width: 

                if self.exiting:
                    return

                painter = QPainter()
                painter.begin(image)
    
                red = y % 255
                green = x % 255
                blue = x % 255
                alpha = 255

                c = img.pixel(x,y)
                color = QColor(c)

                painter.setPen(color)

                painter.drawPoint(x,y)
                
                painter.end()

                x = x+1
        
            if y % 30 == 0:
                self.output.emit( QRect(0, 0, width, height), image)
            y = y +1

        self.output.emit( QRect(0, 0, width, height), image)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
