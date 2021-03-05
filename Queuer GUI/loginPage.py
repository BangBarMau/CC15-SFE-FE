# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from registrationPage import Ui_registrationWindow
from studentPage import Ui_studentAppointmentWindow
from teacherMain import Ui_teacherAppointmentWindow



class Ui_loginWindow(object):

    def openRegistrationWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_registrationWindow()
        self.ui.setupUi(self.window)
        #loginWindow.hide()
        self.window.show()

    def openTeacheraWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_teacherAppointmentWindow()
        self.ui.setupUi(self.window)
        loginWindow.hide()
        self.window.show()

    def openStudentWindow(self):
        email = self.inputEmail.text()
        password = self.inputPassword.text()
        print('Successfully logged in')

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_studentAppointmentWindow()
        self.ui.setupUi(self.window)
        loginWindow.hide()
        self.window.show()

    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(1051, 700)
        loginWindow.setStyleSheet("background-color: rgb(21, 31, 41);\n"
"font: 12pt \"Nunito\";")
        self.loginFrame = QtWidgets.QFrame(loginWindow)
        self.loginFrame.setGeometry(QtCore.QRect(560, 0, 491, 701))
        self.loginFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginFrame.setObjectName("loginFrame")
        self.queuingSystemLabel = QtWidgets.QLabel(self.loginFrame)
        self.queuingSystemLabel.setGeometry(QtCore.QRect(130, 170, 251, 51))
        self.queuingSystemLabel.setStyleSheet("font: 36pt \"Bebas Neue\";\n"
"color: rgb(21, 31, 41);")
        self.queuingSystemLabel.setObjectName("queuingSystemLabel")
        self.emailLabel = QtWidgets.QLabel(self.loginFrame)
        self.emailLabel.setGeometry(QtCore.QRect(100, 340, 71, 16))
        self.emailLabel.setStyleSheet("font: 14pt bold \"Poppins\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(21, 31, 41);")
        self.emailLabel.setObjectName("emailLabel")
        self.passwordLabel = QtWidgets.QLabel(self.loginFrame)
        self.passwordLabel.setGeometry(QtCore.QRect(100, 410, 111, 16))
        self.passwordLabel.setStyleSheet("font: 14pt bold \"Poppins\";\n"
"color: rgb(21, 31, 41);")
        self.passwordLabel.setObjectName("passwordLabel")
        self.inputPassword = QtWidgets.QLineEdit(self.loginFrame)
        self.inputPassword.setGeometry(QtCore.QRect(100, 430, 281, 31))


        self.inputPassword.setObjectName("inputPassword")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.loginFrame)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 910, 281, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.inputEmail = QtWidgets.QLineEdit(self.loginFrame)
        self.inputEmail.setGeometry(QtCore.QRect(100, 360, 281, 31))
        self.inputEmail.setObjectName("inputEmail")
        self.studentButton = QtWidgets.QPushButton(self.loginFrame)
        self.studentButton.setGeometry(QtCore.QRect(160, 490, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.studentButton.setFont(font)
        self.studentButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.studentButton.setStyleSheet("font: 75 10pt \"Montserrat\";\n"
"color: rgb(230, 230, 230);\n"
"background-color: rgb(21, 31, 41);")


        self.studentButton.setObjectName("studentButton")
        self.studentButton.clicked.connect(self.openStudentWindow) #to open student window


        self.teacherButton = QtWidgets.QPushButton(self.loginFrame)
        self.teacherButton.setGeometry(QtCore.QRect(160, 530, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.teacherButton.setFont(font)
        self.teacherButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.teacherButton.setStyleSheet("font: 75 10pt \"Montserrat\";\n"
"color: rgb(230, 230, 230);\n"
"background-color: rgb(21, 31, 41);")


        self.teacherButton.setObjectName("teacherButton")
        self.teacherButton.clicked.connect(self.openTeacheraWindow)


        self.signupLink = QtWidgets.QPushButton(self.loginFrame)
        self.signupLink.setGeometry(QtCore.QRect(200, 570, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.signupLink.setFont(font)
        self.signupLink.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupLink.setStyleSheet("font: 75 10pt \"Montserrat\";\n"
"color: rgb(230, 230, 230);\n"
"background-color: rgb(21, 31, 41);")


        self.signupLink.setObjectName("signupLink")
        self.signupLink.clicked.connect(self.openRegistrationWindow) #to open register form


        self.cssLabel = QtWidgets.QLabel(self.loginFrame)
        self.cssLabel.setGeometry(QtCore.QRect(220, 110, 101, 81))
        self.cssLabel.setStyleSheet("font: 46pt \"Bebas Neue\";\n"
"color: rgb(21, 31, 41);")
        self.cssLabel.setObjectName("cssLabel")
        self.cssLabel.raise_()
        self.queuingSystemLabel.raise_()
        self.emailLabel.raise_()
        self.passwordLabel.raise_()
        self.inputPassword.raise_()
        self.lineEdit_2.raise_()
        self.inputEmail.raise_()
        self.studentButton.raise_()
        self.teacherButton.raise_()
        self.signupLink.raise_()
        self.nowServingLogin = QtWidgets.QLabel(loginWindow)
        self.nowServingLogin.setGeometry(QtCore.QRect(180, 470, 201, 51))
        self.nowServingLogin.setStyleSheet("font: 36pt \"Bebas Neue\";\n"
"color: rgb(255, 255, 255);")
        self.nowServingLogin.setObjectName("nowServingLogin")
        self.priorityNumberLogin = QtWidgets.QLabel(loginWindow)
        self.priorityNumberLogin.setGeometry(QtCore.QRect(240, 530, 81, 51))
        self.priorityNumberLogin.setStyleSheet("font: 46pt \"Bebas Neue\";\n"
"color: rgb(255, 255, 255);")
        self.priorityNumberLogin.setObjectName("priorityNumberLogin")
        self.rightFrame = QtWidgets.QFrame(loginWindow)
        self.rightFrame.setGeometry(QtCore.QRect(10, 0, 541, 701))
        self.rightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightFrame.setObjectName("rightFrame")
        self.logoLogin = QtWidgets.QLabel(self.rightFrame)
        self.logoLogin.setGeometry(QtCore.QRect(-40, 140, 441, 331))
        self.logoLogin.setText("")
        self.logoLogin.setPixmap(QtGui.QPixmap("logoQueuing.png"))
        self.logoLogin.setScaledContents(False)
        self.logoLogin.setObjectName("logoLogin")
        self.rightFrame.raise_()
        self.loginFrame.raise_()
        self.nowServingLogin.raise_()
        self.priorityNumberLogin.raise_()

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Dialog"))
        self.queuingSystemLabel.setText(_translate("loginWindow", "Queuing System"))
        self.emailLabel.setText(_translate("loginWindow", "Email"))
        self.passwordLabel.setText(_translate("loginWindow", "Password"))
        self.studentButton.setText(_translate("loginWindow", "LOGIN AS A STUDENT"))
        self.teacherButton.setText(_translate("loginWindow", "LOGIN AS A TEACHER"))
        self.signupLink.setText(_translate("loginWindow", "REGISTER"))
        self.cssLabel.setText(_translate("loginWindow", "ccs"))
        self.nowServingLogin.setText(_translate("loginWindow", "now serving"))
        self.priorityNumberLogin.setText(_translate("loginWindow", "000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
