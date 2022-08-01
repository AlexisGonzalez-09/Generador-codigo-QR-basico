import qrcode # Importamos el modulo necesario para trabajar con codigos QR

"""data = ("https://www.instagram.com/young__nogitsune/")"""


imagen = qrcode.make('https://www.instagram.com/young__nogitsune/')  # Creamos un codigo a partir de una cadena de texto

archivo_imagen = open('codigo.png', 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()