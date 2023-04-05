from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QFileDialog
import sys
import os
from GenerarQR_UI import Dialog
from mainUI import MainWindow
from Leer_UI import Dialog2
import qrcode
import cv2

'''
REFERENCIAS:

1. http://help.seagullscientific.com/2019/es/Content/ErrorCorrection_GS1QRCode.html#:~:text=Nivel%20L%3A%20Es%20posible%20restaurar,de%20las%20palabras%20de%20acceso.

2. http://help.seagullscientific.com/2019/es/Content/mod_bar_correction.htm

3. https://pypi.org/project/qrcode/
'''


class app(QMainWindow):
    """Clase Principal del programa"""

    def __init__(self):# Contructor de la clase principal del programa
        QMainWindow.__init__(self) 
        self.ui = MainWindow() #Abrimos la ventana principal
        self.ui.setupUi(self) #Inicializamos la clase principal

        self.ui.btn_hacerQR.clicked.connect(self.hacerQR)
        self.ui.btn_LeerQR.clicked.connect(self.leerQR)

    

    def leerQR(self):
        """Metodo que se encargara de leer el codigo QR"""
        self.leer = Leer(self)
        self.leer.show()
        self.hide()



    def hacerQR(self):
        """Metodo que se encargara de generar el codigo QR"""
        self.generadorQR = GenerarQR(self)
        self.generadorQR.show()
        self.hide()
        


class GenerarQR(QDialog):
    def __init__(self,main):# Contructor de la clase generar QR
        QDialog.__init__(self)
        self.main = main 
        self.ui = Dialog() #Abrimos la ventana generar QR
        self.ui.setupUi(self) #Inicializamos la clase generar QR
        self.ui.btn_aceptar.clicked.connect(self.generar)
        self.ui.btn_atras.clicked.connect(self.atras)

    def generar(self):

        if self.ui.rdb_H.isChecked():
            error = qrcode.constants.ERROR_CORRECT_H
        elif self.ui.rdb_L.isChecked():
            error = qrcode.constants.ERROR_CORRECT_L
        elif self.ui.rdb_M.isChecked():
            error = qrcode.constants.ERROR_CORRECT_M
        elif self.ui.rdb_Q.isChecked():
            error = qrcode.constants.ERROR_CORRECT_Q

        data = self.ui.ln_datos.toPlainText() #Se toma el texto del usuario
        qr = qrcode.QRCode(error_correction = error)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image() #Se genera el codigo  QR
        path = os.getcwd() #Obtenemos la ruta del codigo
        ruta, _ = QFileDialog.getSaveFileName(self,'Guardar archivo',path) #Obtenemos la ruta completa que el usuario escogio
        img.save(ruta) #Se guarda la imagen 
        msg = QMessageBox() #Se crea la ventana de confirmacion
        msg.setWindowTitle('Mensaje')
        msg.setText('Su imagen ha sido guardada con exito')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec() #Se ejecuta la ventana de confirmacion
        
    def atras(self):
        main.show()
        self.hide()

class Leer(QDialog):
    def __init__(self,main):
        super().__init__()
        self.main = main
        self.ui = Dialog2() #Abrimos la ventana leer QR
        self.ui.setupUi(self) #Inicializamos la clase leer QR
        self.ui.btn_atras.clicked.connect(self.atras)
        self.ui.btn_leer.clicked.connect(self.leer)
    
    def atras(self):
        self.main.show()
        self.hide()

    def leer(self):
        path = os.getcwd() #obtenemos la ruta de la carpeta actual
        ruta,_ = QFileDialog.getOpenFileName(self,"Abrir archivo",path) # abrimos la ruta del archivo
        
        self.ui.lbl_imagen.setPixmap(QtGui.QPixmap(ruta)) #mostramos el codigo QR
        img = cv2.imread(ruta) #Se lee la imagen con el QR
        detector = cv2.QRCodeDetector() #Se crea el objeto detector
        data, _, _ = detector.detectAndDecode(img) #Se extrae la informacion del QR
        self.ui.ln_salida.setPlainText(data) #Se muestra en pantalla el texto



if __name__ == "__main__":
    aplicacion = QApplication([])   
    main = app()
    main.show()
    sys.exit(aplicacion.exec_())    #Cierra el bucle que muestra la interfaz