# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(487, 388)
        Dialog.setStyleSheet("background-color: rgb(251, 251, 251);")
        self.btn_leer = QtWidgets.QPushButton(Dialog)
        self.btn_leer.setGeometry(QtCore.QRect(190, 300, 91, 31))
        self.btn_leer.setObjectName("btn_leer")
        self.lbl_titulo = QtWidgets.QLabel(Dialog)
        self.lbl_titulo.setGeometry(QtCore.QRect(110, 20, 221, 41))
        self.lbl_titulo.setStyleSheet("font: 10000 16pt \"Ubuntu\";")
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.btn_atras = QtWidgets.QPushButton(Dialog)
        self.btn_atras.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.btn_atras.setObjectName("btn_atras")
        self.lbl_imagen = QtWidgets.QLabel(Dialog)
        self.lbl_imagen.setGeometry(QtCore.QRect(20, 80, 191, 171))
        self.lbl_imagen.setText("")
        self.lbl_imagen.setPixmap(QtGui.QPixmap("qr.jpeg"))
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.ln_salida = QtWidgets.QPlainTextEdit(Dialog)
        self.ln_salida.setEnabled(True)
        self.ln_salida.setGeometry(QtCore.QRect(240, 80, 221, 161))
        self.ln_salida.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.ln_salida.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ln_salida.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ln_salida.setReadOnly(True)
        self.ln_salida.setObjectName("ln_salida")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_leer.setText(_translate("Dialog", "Subir Archivo"))
        self.lbl_titulo.setText(_translate("Dialog", "Leer QR"))
        self.btn_atras.setText(_translate("Dialog", "Atras"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
