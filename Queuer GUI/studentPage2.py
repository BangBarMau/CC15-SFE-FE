# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentMain2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

#import login2
#from main import widget

count = 0
queue = 0

class Ui_studentAppointmentWindow2(object):
    #def logoutFunction(self): #SAME ERROR circular import
        #self.
        #logout = Ui_loginWindow2()
        #widget.addWidget(logout)
        #widget.setCurrentIndex(widget.currentIndex() + 1)

    def getDateTime(self):
        dt = self.dateTimeSchedule.dateTime()
        dt_string = dt.toString(self.dateTimeSchedule.displayFormat())
        return dt_string

    def getPriorityFunction(self):
        global count
        count += 1
        if count == 1:
            self.priorityNumberIndicator.setText(str(count).zfill(3))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Priority Number')
            msg.setText('Only 1 Priority Number per User')
            x = msg.exec_()

    def getAppointmentFunction(self):
        prioNum=str(count)
        subject = self.inputSubject.text()
        schedule = self.getDateTime()
        teacher = self.teacherComboBox.currentText()
        details = self.inputDetails.toPlainText()
        deets = str(details)
        appointmentFile=open(subject+".txt", 'w+')
        appointmentFile.write(subject + '\n')
        appointmentFile.write(schedule + '\n')
        appointmentFile.write(teacher + '\n')
        appointmentFile.write("PrioNum: "+prioNum + '\n')
        appointmentFile.write('\n' + deets)

        print('APPOINTMENT DETAILS:\n Subject: ', subject, '\nTeacher: ', teacher, '\nDetails: ', details)

        self.appointments.setItem(0, 1, QTableWidgetItem('a'))
        self.appointments.setItem(0, 2, QTableWidgetItem('b'))




    def setupUi(self, studentAppointmentWindow2):
        studentAppointmentWindow2.setObjectName("studentAppointmentWindow2")
        studentAppointmentWindow2.resize(1300, 850)
        studentAppointmentWindow2.setStyleSheet("background-color: rgb(21, 31, 41);\n"
"font: 12pt \"Nunito\";")
        #rgb(255, 255, 255)
        self.appointmentFrame = QtWidgets.QFrame(studentAppointmentWindow2)
        self.appointmentFrame.setGeometry(QtCore.QRect(0, 0, 701, 851))
        self.appointmentFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appointmentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appointmentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appointmentFrame.setObjectName("appointmentFrame")
        self.applicationFormLabel = QtWidgets.QLabel(self.appointmentFrame)
        self.applicationFormLabel.setGeometry(QtCore.QRect(240, 90, 291, 51))
        self.applicationFormLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.applicationFormLabel.setStyleSheet("font: 36pt \"Bebas Neue\";\n"
"color: rgb(21, 31, 41);")
        self.applicationFormLabel.setObjectName("applicationFormLabel")
        self.applicationSubjectLabel = QtWidgets.QLabel(self.appointmentFrame)
        self.applicationSubjectLabel.setGeometry(QtCore.QRect(80, 190, 191, 31))
        self.applicationSubjectLabel.setStyleSheet("font: 14pt bold \"Poppins\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(21, 31, 41);")
        self.applicationSubjectLabel.setObjectName("applicationSubjectLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.appointmentFrame)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 910, 281, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.inputSubject = QtWidgets.QLineEdit(self.appointmentFrame)
        self.inputSubject.setGeometry(QtCore.QRect(80, 220, 391, 31))
        self.inputSubject.setObjectName("inputSubject")
        self.setAppointmentButton = QtWidgets.QPushButton(self.appointmentFrame)
        self.setAppointmentButton.setGeometry(QtCore.QRect(80, 730, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setKerning(True)
        self.setAppointmentButton.setFont(font)
        self.setAppointmentButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setAppointmentButton.setAutoFillBackground(False)
        self.setAppointmentButton.setStyleSheet("font: 75 10pt \"Montserrat\";\n"
"color: rgb(230, 230, 230);\n"
"background-color: rgb(21, 31, 41);")
        self.setAppointmentButton.setDefault(False)
        self.setAppointmentButton.setFlat(False)


        self.setAppointmentButton.setObjectName("setAppointmentButton")
        self.setAppointmentButton.clicked.connect(self.getAppointmentFunction)


        self.cancelButton = QtWidgets.QPushButton(self.appointmentFrame)
        self.cancelButton.setGeometry(QtCore.QRect(430, 730, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet("font: 75 10pt \"Montserrat\";\n"
"color: rgb(230, 230, 230);\n"
"background-color: rgb(21, 31, 41);")
        self.cancelButton.setObjectName("cancelButton")
        self.setDateLabel = QtWidgets.QLabel(self.appointmentFrame)
        self.setDateLabel.setGeometry(QtCore.QRect(80, 290, 151, 16))
        self.setDateLabel.setStyleSheet("font: 14pt bold \"Poppins\";\n"
"color: rgb(21, 31, 41);")
        self.setDateLabel.setObjectName("setDateLabel")
        self.inputYear = QtWidgets.QLineEdit(self.appointmentFrame)
        self.inputYear.setGeometry(QtCore.QRect(770, 260, 101, 31))
        self.inputYear.setText("")
        self.inputYear.setObjectName("inputYear")
        self.detailsLabel = QtWidgets.QLabel(self.appointmentFrame)
        self.detailsLabel.setGeometry(QtCore.QRect(80, 470, 171, 21))
        self.detailsLabel.setStyleSheet("font: 14pt bold \"Poppins\";\n"
"color: rgb(21, 31, 41);")
        self.detailsLabel.setObjectName("detailsLabel")
        self.inputDetails = QtWidgets.QTextEdit(self.appointmentFrame)
        self.inputDetails.setGeometry(QtCore.QRect(80, 500, 541, 201))
        self.inputDetails.setObjectName("inputDetails")
        self.dateTimeSchedule = QtWidgets.QDateTimeEdit(self.appointmentFrame)
        self.dateTimeSchedule.setGeometry(QtCore.QRect(80, 310, 194, 22))
        self.dateTimeSchedule.setObjectName("dateTimeSchedule")
        self.dateTimeSchedule.setDisplayFormat("MM/dd/yyyy hh:mm")
        self.teacherLabel = QtWidgets.QLabel(self.appointmentFrame)
        self.teacherLabel.setGeometry(QtCore.QRect(80, 370, 171, 31))
        self.teacherLabel.setStyleSheet("font: 14pt bold \"Poppins\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(21, 31, 41);")
        self.teacherLabel.setObjectName("teacherLabel")
        self.teacherComboBox = QtWidgets.QComboBox(self.appointmentFrame)
        self.teacherComboBox.setGeometry(QtCore.QRect(80, 400, 281, 22))
        self.teacherComboBox.setObjectName("teacherComboBox")
        self.teacherComboBox.addItem("")
        self.teacherComboBox.addItem("")
        self.teacherComboBox.addItem("")
        self.teacherComboBox.addItem("")
        self.getPriorityButton = QtWidgets.QPushButton(self.appointmentFrame)
        self.getPriorityButton.setGeometry(QtCore.QRect(240, 730, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.getPriorityButton.setFont(font)
        self.getPriorityButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.getPriorityButton.setStyleSheet("font: 75 10pt \"Montserrat\";\n"
"color: rgb(230, 230, 230);\n"
"background-color: rgb(21, 31, 41);")


        self.getPriorityButton.setObjectName("getPriorityButton")
        self.getPriorityButton.clicked.connect(self.getPriorityFunction)


        self.logoutButtonStudent = QtWidgets.QPushButton(self.appointmentFrame)
        self.logoutButtonStudent.setGeometry(QtCore.QRect(530, 730, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.logoutButtonStudent.setFont(font)
        self.logoutButtonStudent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoutButtonStudent.setStyleSheet("font: 75 10pt \"Montserrat\";\n"
"color: rgb(230, 230, 230);\n"
"background-color: rgb(21, 31, 41);")


        self.logoutButtonStudent.setObjectName("logoutButtonStudent")


        self.priorityNumberLabel = QtWidgets.QLabel(self.appointmentFrame)
        self.priorityNumberLabel.setGeometry(QtCore.QRect(490, 190, 191, 31))
        self.priorityNumberLabel.setStyleSheet("font: 14pt bold \"Poppins\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(21, 31, 41);")
        self.priorityNumberLabel.setObjectName("priorityNumberLabel")
        self.priorityNumberIndicator = QtWidgets.QLabel(self.appointmentFrame)
        self.priorityNumberIndicator.setGeometry(QtCore.QRect(570, 220, 61, 31))
        self.priorityNumberIndicator.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.priorityNumberIndicator.setStyleSheet("font: 20pt bold \"Poppins\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(21, 31, 41);")
        self.priorityNumberIndicator.setObjectName("priorityNumberIndicator")
        self.teacherLabel.raise_()
        self.applicationFormLabel.raise_()
        self.applicationSubjectLabel.raise_()
        self.lineEdit_2.raise_()
        self.inputSubject.raise_()
        self.setAppointmentButton.raise_()
        self.cancelButton.raise_()
        self.setDateLabel.raise_()
        self.inputYear.raise_()
        self.detailsLabel.raise_()
        self.inputDetails.raise_()
        self.dateTimeSchedule.raise_()
        self.teacherComboBox.raise_()
        self.getPriorityButton.raise_()
        self.logoutButtonStudent.raise_()
        self.priorityNumberLabel.raise_()
        self.priorityNumberIndicator.raise_()
        self.appointmentLabel = QtWidgets.QLabel(studentAppointmentWindow2)
        self.appointmentLabel.setGeometry(QtCore.QRect(940, 120, 131, 51))
        self.appointmentLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.appointmentLabel.setStyleSheet("font: 20pt \"Bebas Neue\";\n"
"color: rgb(231, 231, 231);")
        self.appointmentLabel.setObjectName("appointmentLabel")
        self.appointmentHistory = QtWidgets.QTableWidget(studentAppointmentWindow2)
        self.appointmentHistory.setGeometry(QtCore.QRect(740, 520, 511, 271))
        self.appointmentHistory.setObjectName("appointmentHistory")
        self.appointmentHistory.setColumnCount(4)
        self.appointmentHistory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.appointmentHistory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointmentHistory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointmentHistory.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointmentHistory.setHorizontalHeaderItem(3, item)
        self.historyLabel = QtWidgets.QLabel(studentAppointmentWindow2)
        self.historyLabel.setGeometry(QtCore.QRect(960, 470, 71, 51))
        self.historyLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.historyLabel.setStyleSheet("font: 20pt \"Bebas Neue\";\n"
"color: rgb(231, 231, 231);")
        self.historyLabel.setObjectName("historyLabel")
        self.appointments = QtWidgets.QTableWidget(studentAppointmentWindow2)
        self.appointments.setGeometry(QtCore.QRect(740, 170, 511, 281))
        self.appointments.setObjectName("appointments")
        self.appointments.setColumnCount(4)
        self.appointments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.appointments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointments.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointments.setHorizontalHeaderItem(3, item)
        self.queuingSystemLabel_4 = QtWidgets.QLabel(studentAppointmentWindow2)
        self.queuingSystemLabel_4.setGeometry(QtCore.QRect(1200, 20, 71, 51))
        self.queuingSystemLabel_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.queuingSystemLabel_4.setStyleSheet("font: 36pt \"Bebas Neue\";\n"
"color: rgb(21, 31, 41);\n"
"background-color: rgb(255, 255, 255);")
        self.queuingSystemLabel_4.setObjectName("queuingSystemLabel_4")
        self.nowServingFrame3 = QtWidgets.QFrame(studentAppointmentWindow2)
        self.nowServingFrame3.setGeometry(QtCore.QRect(1110, 10, 191, 61))
        self.nowServingFrame3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nowServingFrame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nowServingFrame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nowServingFrame3.setObjectName("nowServingFrame3")
        self.nowServingMainStudent = QtWidgets.QLabel(self.nowServingFrame3)
        self.nowServingMainStudent.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.nowServingMainStudent.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nowServingMainStudent.setStyleSheet("font: 17pt \"Bebas Neue\";\n"
"color: rgb(21, 31, 41);\n"
"background-color: rgb(255, 255, 255);")
        self.nowServingMainStudent.setObjectName("nowServingMainStudent")
        self.priorityNumberMainStudent = QtWidgets.QLabel(self.nowServingFrame3)
        self.priorityNumberMainStudent.setGeometry(QtCore.QRect(110, 10, 71, 51))
        self.priorityNumberMainStudent.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.priorityNumberMainStudent.setStyleSheet("font: 36pt \"Bebas Neue\";\n"
"color: rgb(21, 31, 41);\n"
"background-color: rgb(255, 255, 255);")
        self.priorityNumberMainStudent.setObjectName("priorityNumberMainStudent")
        self.viewFrame = QtWidgets.QFrame(studentAppointmentWindow2)
        self.viewFrame.setGeometry(QtCore.QRect(700, 0, 601, 841))
        self.viewFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.viewFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.viewFrame.setObjectName("viewFrame")
        self.logoMainStudent = QtWidgets.QLabel(self.viewFrame)
        self.logoMainStudent.setGeometry(QtCore.QRect(340, 10, 71, 61))
        self.logoMainStudent.setText("")
        self.logoMainStudent.setPixmap(QtGui.QPixmap("upper.png"))
        self.logoMainStudent.setObjectName("logoMainStudent")
        self.viewFrame.raise_()
        self.appointmentLabel.raise_()
        self.appointmentFrame.raise_()
        self.appointmentHistory.raise_()
        self.historyLabel.raise_()
        self.appointments.raise_()
        self.queuingSystemLabel_4.raise_()
        self.nowServingFrame3.raise_()

        self.retranslateUi(studentAppointmentWindow2)
        QtCore.QMetaObject.connectSlotsByName(studentAppointmentWindow2)

    def retranslateUi(self, studentAppointmentWindow2):
        _translate = QtCore.QCoreApplication.translate
        studentAppointmentWindow2.setWindowTitle(_translate("studentAppointmentWindow2", "Dialog"))
        self.applicationFormLabel.setText(_translate("studentAppointmentWindow2", "APPOINTMENT FORM"))
        self.applicationSubjectLabel.setText(_translate("studentAppointmentWindow2", "Appointment Subject"))
        self.setAppointmentButton.setText(_translate("studentAppointmentWindow2", "SET APPOINTMENT"))
        self.cancelButton.setText(_translate("studentAppointmentWindow2", "CANCEL"))
        self.setDateLabel.setText(_translate("studentAppointmentWindow2", "Set Date"))
        self.detailsLabel.setText(_translate("studentAppointmentWindow2", "Appointment Details"))
        self.teacherLabel.setText(_translate("studentAppointmentWindow2", "Teacher"))
        self.teacherComboBox.setItemText(0, _translate("studentAppointmentWindow2", "Mr. Lowee Oliva"))
        self.teacherComboBox.setItemText(1, _translate("studentAppointmentWindow2", "Mr. Rangie Obispo"))
        self.teacherComboBox.setItemText(2, _translate("studentAppointmentWindow2", "Mr. Patrick Mac"))
        self.teacherComboBox.setItemText(3, _translate("studentAppointmentWindow2", "Ms. Bambi Jimenez"))
        self.getPriorityButton.setText(_translate("studentAppointmentWindow2", "GET PRIORITY NUMBER"))
        self.logoutButtonStudent.setText(_translate("studentAppointmentWindow2", "LOGOUT"))
        self.priorityNumberLabel.setText(_translate("studentAppointmentWindow2", "Priority Number"))
        self.priorityNumberIndicator.setText(_translate("studentAppointmentWindow2", "000"))
        self.appointmentLabel.setText(_translate("studentAppointmentWindow2", "APPOINTMENTS"))
        item = self.appointmentHistory.horizontalHeaderItem(0)
        item.setText(_translate("studentAppointmentWindow2", "Priority Number"))
        item = self.appointmentHistory.horizontalHeaderItem(1)
        item.setText(_translate("studentAppointmentWindow2", "Schedule"))
        item = self.appointmentHistory.horizontalHeaderItem(2)
        item.setText(_translate("studentAppointmentWindow2", "Teacher"))
        item = self.appointmentHistory.horizontalHeaderItem(3)
        item.setText(_translate("studentAppointmentWindow2", "Details"))
        self.historyLabel.setText(_translate("studentAppointmentWindow2", "HISTORY"))
        item = self.appointments.horizontalHeaderItem(0)
        item.setText(_translate("studentAppointmentWindow2", "Priority Number"))
        item = self.appointments.horizontalHeaderItem(1)
        item.setText(_translate("studentAppointmentWindow2", "Schedule"))
        item = self.appointments.horizontalHeaderItem(2)
        item.setText(_translate("studentAppointmentWindow2", "Teacher"))
        item = self.appointments.horizontalHeaderItem(3)
        item.setText(_translate("studentAppointmentWindow2", "Details"))
        self.queuingSystemLabel_4.setText(_translate("studentAppointmentWindow2", "000"))
        self.nowServingMainStudent.setText(_translate("studentAppointmentWindow2", "NOW SERVING"))
        self.priorityNumberMainStudent.setText(_translate("studentAppointmentWindow2", "000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentAppointmentWindow2 = QtWidgets.QDialog()
    ui = Ui_studentAppointmentWindow2()
    ui.setupUi(studentAppointmentWindow2)
    studentAppointmentWindow2.show()
    sys.exit(app.exec_())
