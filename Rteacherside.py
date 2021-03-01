from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1072, 563)
        self.appointmentsFrame = QtWidgets.QFrame(Dialog)
        self.appointmentsFrame.setGeometry(QtCore.QRect(10, 10, 611, 541))
        self.appointmentsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appointmentsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appointmentsFrame.setObjectName("appointmentsFrame")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.appointmentsFrame)
        self.scrollArea_7.setGeometry(QtCore.QRect(20, 100, 571, 171))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 569, 169))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.appform_8 = QtWidgets.QLabel(self.appointmentsFrame)
        self.appform_8.setGeometry(QtCore.QRect(20, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.appform_8.setFont(font)
        self.appform_8.setObjectName("appform_8")
        self.appform_9 = QtWidgets.QLabel(self.appointmentsFrame)
        self.appform_9.setGeometry(QtCore.QRect(20, 300, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.appform_9.setFont(font)
        self.appform_9.setObjectName("appform_9")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.appointmentsFrame)
        self.scrollArea_8.setGeometry(QtCore.QRect(20, 350, 571, 171))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 569, 169))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.settingsFrame = QtWidgets.QFrame(Dialog)
        self.settingsFrame.setGeometry(QtCore.QRect(650, 10, 411, 541))
        self.settingsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsFrame.setObjectName("settingsFrame")
        self.availabilityGroupBox = QtWidgets.QGroupBox(self.settingsFrame)
        self.availabilityGroupBox.setGeometry(QtCore.QRect(40, 130, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.availabilityGroupBox.setFont(font)
        self.availabilityGroupBox.setObjectName("availabilityGroupBox")
        self.radioButton = QtWidgets.QRadioButton(self.availabilityGroupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.availabilityGroupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 70, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.clockFrame = QtWidgets.QFrame(self.settingsFrame)
        self.clockFrame.setGeometry(QtCore.QRect(10, 10, 391, 111))
        self.clockFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.clockFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.clockFrame.setObjectName("clockFrame")
        self.label = QtWidgets.QLabel(self.clockFrame)
        self.label.setGeometry(QtCore.QRect(80, 30, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.settingsFrame)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 321, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.settingsFrame)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 340, 321, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.settingsFrame)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 410, 321, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.appform_8.setText(_translate("Dialog", "View Appointments"))
        self.appform_9.setText(_translate("Dialog", "Appointment History"))
        self.availabilityGroupBox.setTitle(_translate("Dialog", "Availability"))
        self.radioButton.setText(_translate("Dialog", "Taking Appointments"))
        self.radioButton_2.setText(_translate("Dialog", "Not Taking Appointments"))
        self.label.setText(_translate("Dialog", "CLOCK HERE EVENTUALLY"))
        self.pushButton.setText(_translate("Dialog", "Accept Appointment"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel Appointment"))
        self.pushButton_3.setText(_translate("Dialog", "Next Appointment"))