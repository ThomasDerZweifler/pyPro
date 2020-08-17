import sys
import time
from PyQt5 import QtWidgets, QtCore
 
class WorkerThread(QtCore.QObject):
    updateUI = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.count = 0
        self.interrupt = True
 
    @QtCore.pyqtSlot()
    def run(self):
        while self.interrupt:
            # Long running task ...
            self.count = self.count +1
            self.updateUI.emit(self.count)
            time.sleep(1)
 
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = WorkerThread()
        self.workerThread = QtCore.QThread()
        self.workerThread.started.connect(self.worker.run)  # Init worker run() at startup (optional)
        self.worker.updateUI.connect(self.updateUI)  # Connect your signals/slots
        self.worker.moveToThread(self.workerThread)  # Move the Worker object to the Thread object
        self.workerThread.start()
 
    def updateUI(self, count):
        print("updateUI() " + str(count))

        if count > 4:
            self.worker.interrupt = False
 
if __name__== '__main__':
    app = QtWidgets.QApplication([])
    gui = Main()
    sys.exit(app.exec_())