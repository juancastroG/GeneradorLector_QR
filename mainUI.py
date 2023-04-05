# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 227)
        MainWindow.setStyleSheet("background-color: rgb(251, 251, 251);")
        MainWindow.setGeometry(720,400,393,227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
    
        self.btn_hacerQR = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hacerQR.setGeometry(QtCore.QRect(60, 160, 121, 41))
        self.btn_hacerQR.setObjectName("btn_hacerQR")
        self.btn_LeerQR = QtWidgets.QPushButton(self.centralwidget)
        self.btn_LeerQR.setGeometry(QtCore.QRect(210, 160, 121, 41))
        self.btn_LeerQR.setObjectName("btn_LeerQR")
        self.lbl_Bienvenida = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Bienvenida.setGeometry(QtCore.QRect(70, 90, 261, 61))
        self.lbl_Bienvenida.setStyleSheet("font: 75 12pt \"DejaVu Serif\";")
        self.lbl_Bienvenida.setObjectName("lbl_Bienvenida")
        self.lbl_imagen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagen.setGeometry(QtCore.QRect(150, 20, 91, 81))
        self.lbl_imagen.setText("")
        self.lbl_imagen.setPixmap(QtGui.QPixmap("qr.jpeg"))
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setObjectName("lbl_imagen")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR-codificador"))
        self.btn_hacerQR.setText(_translate("MainWindow", "Genera QR"))
        self.btn_LeerQR.setText(_translate("MainWindow", "Leer QR"))
        self.lbl_Bienvenida.setText(_translate("MainWindow", "Bienvenido, Escoja una opcion"))


if __name__ == "__main__":
    print('hola')
