import sys

from PyQt5.QtWidgets import QMainWindow, QScrollArea, QAction, qApp, QMenu, QHBoxLayout, QLabel, QComboBox, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QColor, QPixmap, QPainter, QImage
from PyQt5.QtCore import Qt, QPoint, QRect
from PIL import Image as img
from PIL.ImageQt import ImageQt

import sympy as sp

import operations.imageProcessing as imgProc

import operations.qtImageProcessing as qtImgProc

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
        self.width = 1800
        self.height = 800
        self.initUI()
    
    def initUI(self):

        # get icons from here:  https://material.io/resources/icons/?icon=perm_media&style=baseline

        openAct = QAction(QIcon('icon/open_folder.png'), 'Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open Image')
        openAct.triggered.connect(self.openFileNameDialog)

        exitAct = QAction(QIcon('icon/power.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.originalImg = QLabel(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.originalImg)

        self.processedImg = QLabel(self)
        scroll1 = QScrollArea()
        scroll1.setWidgetResizable(True)
        scroll1.setWidget(self.processedImg)

        layout= QHBoxLayout()

        layout.addWidget(scroll)
        layout.addWidget(scroll1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.cb = QComboBox()
        self.cb.addItems(["flip", "gray", "invert", "interlace", "reduce", "mosaic", "rotate"])
        self.cb.currentIndexChanged.connect(self.selectionchange)

        toolbar = self.addToolBar('Tools')
        toolbar.addAction(openAct)
        toolbar.addAction(exitAct)
        toolbar.addWidget(self.cb)

        self.setWindowTitle(self.title)
        self.setMinimumSize(self.width, self.height)
        
        self.show()
    
    def selectionchange(self,i):
        self.imageProcessing(self.pixmap,self.cb.itemText(i))


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            im = img.open(self.fileName)
            qim = ImageQt(im)
            self.pixmap = QPixmap.fromImage(qim)
            self.originalImg.setPixmap(self.pixmap)

            self.originalImg.setStatusTip(self.fileName)

            self.imageProcessing(self.pixmap,self.cb.currentText())

            # doesn't work under Windows
            #qim2 = ImageQt(imgProc.gray(im))
            #pixmap2 = QPixmap.fromImage(qim2)
            #self.processedImg.setPixmap(pixmap2)
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def imageProcessing(self, pixmap, operator):
        image = pixmap.toImage()

        self.imageA = image

        if operator == "flip":
            self.imageA = qtImgProc.flip_horizontal(image)
        elif operator == "gray":
            self.imageA = qtImgProc.gray(image)
        elif operator == "invert":
            self.imageA = qtImgProc.invert(image)
        elif operator == "interlace":
            self.imageA = qtImgProc.interlace(image)
        elif operator == "reduce":
            self.imageA = qtImgProc.reduce(image)
        elif operator == "mosaic":
            self.imageA = qtImgProc.mosaic(image,4)
        elif operator == "rotate":
            self.imageA = qtImgProc.rotate(image,45)
            self.myWidget.rot(45)

        self.pixmapA = QPixmap(self.imageA)
        self.processedImg.setPixmap(self.pixmapA)
        self.processedImg.setStatusTip(self.fileName)

    #def mouseMoveEvent(self, e):
     #   painter = QPainter(self.pixmapA)
      #  p = painter.pen()
      #  p.setWidth(10)
      #  p.setColor(QColor(255,0,0))
      #  painter.setPen(p)

      #  painter.drawPoint(e.x(), e.y())

      #  self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())