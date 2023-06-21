from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from view import MainWindow
import sys


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    sys.exit()
