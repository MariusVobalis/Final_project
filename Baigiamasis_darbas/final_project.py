# Form implementation generated from reading ui file 'Final_project.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 232)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_Button.setGeometry(QtCore.QRect(10, 119, 75, 24))
        self.start_Button.setObjectName("start_Button")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 251, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.feedback_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.feedback_label.setGeometry(QtCore.QRect(290, 50, 341, 111))
        font = QtGui.QFont()
        font.setBold(True)
        self.feedback_label.setFont(font)
        self.feedback_label.setText("")
        self.feedback_label.setWordWrap(True)
        self.feedback_label.setObjectName("feedback_label")
        self.Enter_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Enter_label.setGeometry(QtCore.QRect(21, 50, 261, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.Enter_label.setFont(font)
        self.Enter_label.setObjectName("Enter_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_Button.setText(_translate("MainWindow", "Start"))
        self.Enter_label.setText(_translate("MainWindow", "Enter Web Address from elenta.lt"))
