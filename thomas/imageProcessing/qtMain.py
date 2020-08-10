import sys
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QAction, qApp, QMenu, QHBoxLayout, QLabel, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image as img
from PIL.ImageQt import ImageQt

import operations.imageProcessing as imgProc

import operations.qtImageProcessing as qtImgProc

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

        toolbar = self.addToolBar('Tools')
        toolbar.addAction(openAct)
        toolbar.addAction(exitAct)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
        
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            im = img.open(fileName)
            qim = ImageQt(im)
            pixmap = QPixmap.fromImage(qim)
            self.originalImg.setPixmap(pixmap)

            self.imageProcessing(pixmap)

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

    def imageProcessing(self, pixmap):
        image = pixmap.toImage()

        #imageA = qtImgProc.invert(image)

        #imageA = qtImgProc.flip_horizontal(image)

        #imageA = qtImgProc.interlace(image)

        #imageA = qtImgProc.gray(image)

        #imageA = qtImgProc.reduce(image)

        imageA = qtImgProc.mosaic(image,4)


        pixmapA = QPixmap(imageA)
        self.processedImg.setPixmap(pixmapA)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())