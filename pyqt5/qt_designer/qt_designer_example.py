# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\\Python programming\\Python libraries lessons\\Lesson13 - pyqt5 - qtDesigner\\example.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(40, 50, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        self.mainbutton = QtWidgets.QPushButton(self.centralwidget)
        self.mainbutton.setGeometry(QtCore.QRect(470, 350, 431, 161))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.mainbutton.setFont(font)
        self.mainbutton.setObjectName("mainbutton")
        self.hide_label = QtWidgets.QLabel(self.centralwidget)
        self.hide_label.setGeometry(QtCore.QRect(40, 160, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.hide_label.setFont(font)
        self.hide_label.setObjectName("hide_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainbutton.clicked.connect(self.button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def button_clicked(self):
        print('hello im clicked')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "Main label of this window"))
        self.mainbutton.setText(_translate("MainWindow", "Click me"))
        self.hide_label.setText(_translate("MainWindow", "hide me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

