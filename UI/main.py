from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from mainWindow import Ui_MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    # print(mainWindow.centralWidget)
    mainWindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
