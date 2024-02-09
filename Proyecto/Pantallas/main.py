from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from MainView_ui import Ui_MainWindow

class Main:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()

    def run(self):
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = Main()
    app.run()