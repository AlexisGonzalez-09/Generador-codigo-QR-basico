import qrcode # Importacion del modulo necesario para trabajar con codigos QR

#para que funcione debes tener el archivo dentro de una carpeta y ejecurarlo y asi se guardara el codigo QR
imagen = qrcode.make('https://www.instagram.com/young__nogitsune/')  # Creamos un codigo a partir de una cadena de texto

archivo_imagen = open('codigo.png', 'wb')
imagen.save(archivo_imagen) #Guarda el png en la carpeta
archivo_imagen.close()
