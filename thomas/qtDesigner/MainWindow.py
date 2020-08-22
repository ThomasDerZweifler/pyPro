# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# use QT Designer design the ui and save as main.ui
#   pyuic5 -x -o MainWindow.py main.ui

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.incButton = QtWidgets.QPushButton(self.centralwidget)
        self.incButton.setGeometry(QtCore.QRect(130, 90, 113, 32))
        self.incButton.setObjectName("incButton")
        self.decButton = QtWidgets.QPushButton(self.centralwidget)
        self.decButton.setGeometry(QtCore.QRect(130, 280, 113, 32))
        self.decButton.setObjectName("decButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(70, 120, 251, 151))
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.incButton.clicked.connect(self.inc)
        self.decButton.clicked.connect(self.dec)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def inc(self):
        self.lcdNumber.display(self.lcdNumber.value() + 1)

    def dec(self):
        self.lcdNumber.display(self.lcdNumber.value() - 1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.incButton.setText(_translate("MainWindow", "+1"))
        self.decButton.setText(_translate("MainWindow", "-1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

