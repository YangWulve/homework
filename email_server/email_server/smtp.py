# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ssurf\Desktop\代码包\A-Email-Demo-master\A-Email-Demo-master\apps\smtp.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 91, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(550, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 160, 521, 21))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 71, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 210, 521, 21))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 250, 71, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 260, 521, 301))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 580, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 580, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.ffliechose = QtWidgets.QPushButton(self.centralwidget)
        self.ffliechose.setGeometry(QtCore.QRect(660, 260, 111, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ffliechose.setFont(font)
        self.ffliechose.setObjectName("ffliechose")
        self.choosefile = QtWidgets.QLineEdit(self.centralwidget)
        self.choosefile.setGeometry(QtCore.QRect(660, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.choosefile.setFont(font)
        self.choosefile.setObjectName("choosefile")
        self.yes = QtWidgets.QLineEdit(self.centralwidget)
        self.yes.setGeometry(QtCore.QRect(280, 630, 221, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yes.setFont(font)
        self.yes.setObjectName("yes")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "发件人账号："))
        self.label_4.setText(_translate("MainWindow", "我的昵称："))
        self.label_5.setText(_translate("MainWindow", "收件人邮箱："))
        self.label_6.setText(_translate("MainWindow", "邮件主题："))
        self.label_7.setText(_translate("MainWindow", "邮件正文："))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.ffliechose.setText(_translate("MainWindow", "添加附件"))
        self.label.setText(_translate("MainWindow", "邮件客户端"))