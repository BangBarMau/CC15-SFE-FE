from PyQt5 import QtCore, QtGui, QtWidgets
from RQueProt import Ui_QUeuer
import sys

class win1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__();
        self.ui = Ui_QUeuer()
        self.ui.setupUi(self)


if __name__=='__main__':
    Program =  QtWidgets.QApplication(sys.argv)
    MyWin1 = win1()
    MyWin1.show()
    sys.exit(Program.exec_())