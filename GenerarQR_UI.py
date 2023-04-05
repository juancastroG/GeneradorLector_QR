# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(477, 371)
        Dialog.setGeometry(720,400,477,371)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("qr.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(251, 251, 251);")
        Dialog.setSizeGripEnabled(False)
        self.ln_datos = QtWidgets.QPlainTextEdit(Dialog)
        self.ln_datos.setGeometry(QtCore.QRect(30, 130, 271, 171))
        self.ln_datos.setObjectName("ln_datos")
        self.lbl_texto = QtWidgets.QLabel(Dialog)
        self.lbl_texto.setGeometry(QtCore.QRect(50, 70, 241, 51))
        self.lbl_texto.setStyleSheet("font: 75 13pt \"DejaVu Serif\";")
        self.lbl_texto.setObjectName("lbl_texto")
        
        self.btn_aceptar = QtWidgets.QPushButton(Dialog)
        self.btn_aceptar.setGeometry(QtCore.QRect(200, 320, 101, 31))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.lbl_titulo = QtWidgets.QLabel(Dialog)
        self.lbl_titulo.setGeometry(QtCore.QRect(130, 20, 221, 41))
        self.lbl_titulo.setStyleSheet("font: 10000 16pt \"Ubuntu\";")
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.btn_atras = QtWidgets.QPushButton(Dialog)
        self.btn_atras.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.btn_atras.setObjectName("btn_atras")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(340, 130, 118, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rdb_L = QtWidgets.QRadioButton(self.widget)
        self.rdb_L.setObjectName("rdb_L")
        self.verticalLayout.addWidget(self.rdb_L)
        self.rdb_M = QtWidgets.QRadioButton(self.widget)
        self.rdb_M.setObjectName("rdb_M")
        self.rdb_M.setChecked(True)
        self.verticalLayout.addWidget(self.rdb_M)
        self.rdb_Q = QtWidgets.QRadioButton(self.widget)
        self.rdb_Q.setObjectName("rdb_Q")
        self.verticalLayout.addWidget(self.rdb_Q)
        self.rdb_H = QtWidgets.QRadioButton(self.widget)
        self.rdb_H.setAutoFillBackground(False)
        self.rdb_H.setObjectName("rdb_H")
        self.verticalLayout.addWidget(self.rdb_H)
        self.lbl_errores = QtWidgets.QLabel(Dialog)
        self.lbl_errores.setGeometry(QtCore.QRect(320, 90, 131, 31))
        self.lbl_errores.setObjectName("lbl_errores")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generar QR"))
        self.lbl_texto.setText(_translate("Dialog", "Escriba el texto a codificar"))
        self.btn_aceptar.setText(_translate("Dialog", "Generar QR"))
        self.lbl_titulo.setText(_translate("Dialog", "Generar QR"))
        self.btn_atras.setText(_translate("Dialog", "Atras"))
        self.rdb_L.setText(_translate("Dialog", "L"))
        self.rdb_M.setText(_translate("Dialog", "M"))
        self.rdb_Q.setText(_translate("Dialog", "Q"))
        self.rdb_H.setText(_translate("Dialog", "H"))
        self.lbl_errores.setText(_translate("Dialog", "Correccion de errores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
