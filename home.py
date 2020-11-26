# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonAddPeer = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddPeer.setGeometry(QtCore.QRect(80, 360, 160, 60))
        self.buttonAddPeer.setObjectName("buttonAddPeer")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(80, 240, 160, 60))
        self.buttonStart.setObjectName("buttonStart")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(98, 40, 111, 111))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("scripts/publicKey.png"))
        self.photo.setObjectName("photo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName("menubar")
        self.menufdsa = QtWidgets.QMenu(self.menubar)
        self.menufdsa.setObjectName("menufdsa")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVPN = QtWidgets.QAction(MainWindow)
        self.actionVPN.setObjectName("actionVPN")
        self.menufdsa.addAction(self.actionVPN)
        self.menubar.addAction(self.menufdsa.menuAction())

        MainWindow.showFullScreen()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonAddPeer.clicked.connect(self.showPubKey)
        self.buttonStart.clicked.connect(self.showIPKey)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonAddPeer.setText(_translate("MainWindow", "Add Peer"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))
        self.menufdsa.setTitle(_translate("MainWindow", "VPN"))
        self.actionVPN.setText(_translate("MainWindow", "VPN"))

    def showIPKey(self):
        self.photo.setPixmap(QtGui.QPixmap("scripts/ipAddr.png"))

    def showPubKey(self):
        self.photo.setPixmap(QtGui.QPixmap("scripts/publicKey.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())