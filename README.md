# Generador y lector de códigos QR con detección de errores

Este proyecto es una aplicación de escritorio desarrollada en Python con PyQt5 que permite generar y leer códigos QR. La aplicación cuenta con la capacidad de ajustar los tipos de error que se pueden introducir en los códigos generados, con opciones para los niveles de corrección de errores H, L, M y Q. Además, también puede leer los códigos QR presentes en imágenes cargadas por el usuario.

## que es QR?
Los códigos QR (Quick Response) son una forma de código de barras bidimensional que se utiliza para almacenar información en una matriz de puntos. A diferencia de los códigos de barras unidimensionales, los códigos QR pueden almacenar una cantidad significativa de información, como direcciones web, información de contacto, mensajes de texto y más. Los códigos QR se han vuelto muy populares debido a su capacidad para ser escaneados rápidamente con dispositivos móviles, lo que los convierte en una herramienta valiosa para la publicidad, el marketing y la gestión de inventarios.

## Tecnologías utilizadas

* PyQt5: framework de interfaz gráfica de usuario para Python

* qrcode: librería para la generación de códigos QR

* cv2: librería OpenCV para la detección de códigos QR en imágenes

## Uso

Para utilizar la aplicación, se debe ejecutar el archivo app.py. Una vez abierta la interfaz gráfica, el usuario podrá elegir entre generar un nuevo código QR o leer uno existente. Si se elige la opción de generación, se pueden seleccionar los parámetros de error deseados y el texto a codificar. Si se elige la opción de lectura, se puede cargar una imagen y la aplicación detectará automáticamente los códigos QR presente

## Autoria y Licencia

Este proyecto ha sido desarrollado por Juan Carlos Castro Guevara. No cuenta con licencia específica, pero se invita a los usuarios a respetar los términos y condiciones de las librerías utilizadas en el proyecto.
