from PyQt5 import QtCore, QtGui, QtWidgets
from Rappoint import Ui_Dialog
from Rteacherside import Ui_Dialog as teachside
import sys
#
class Ui_QUeuer(object):
    def openWindowStu(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindowFac(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=teachside()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, QUeuer):
        QUeuer.setObjectName("QUeuer")
        QUeuer.resize(583, 452)
        self.LoginFrame = QtWidgets.QFrame(QUeuer)
        self.LoginFrame.setGeometry(QtCore.QRect(10, 20, 561, 341))
        self.LoginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginFrame.setObjectName("LoginFrame")
        self.apppic = QtWidgets.QGraphicsView(self.LoginFrame)
        self.apppic.setGeometry(QtCore.QRect(210, 10, 171, 101))
        self.apppic.setObjectName("apppic")
        self.lineEdit = QtWidgets.QLineEdit(self.LoginFrame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 160, 221, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.LoginFrame)
        self.label.setGeometry(QtCore.QRect(180, 130, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.LoginFrame)
        self.label_2.setGeometry(QtCore.QRect(180, 190, 81, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.LoginFrame)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 210, 221, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.loginbutton = QtWidgets.QPushButton(self.LoginFrame)
        self.loginbutton.setGeometry(QtCore.QRect(200, 250, 171, 28))
        self.loginbutton.setObjectName("loginbutton")
        self.loginbutton.clicked.connect(self.openWindowStu)
        self.loginbutton_2 = QtWidgets.QPushButton(self.LoginFrame)
        self.loginbutton_2.setGeometry(QtCore.QRect(200, 290, 171, 28))
        self.loginbutton_2.setObjectName("loginbutton_2")
        self.loginbutton_2.clicked.connect(self.openWindowFac)

        self.retranslateUi(QUeuer)
        QtCore.QMetaObject.connectSlotsByName(QUeuer)

    def retranslateUi(self, QUeuer):
        _translate = QtCore.QCoreApplication.translate
        QUeuer.setWindowTitle(_translate("QUeuer", "Dialog"))
        self.label.setText(_translate("QUeuer", "Email"))
        self.label_2.setText(_translate("QUeuer", "Password"))
        self.loginbutton.setText(_translate("QUeuer", " Login as a Student"))
        self.loginbutton_2.setText(_translate("QUeuer", " Login as Faculty"))
