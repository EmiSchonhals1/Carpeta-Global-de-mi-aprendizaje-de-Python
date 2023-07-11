#llamamos al modulo_dibujar_caracter y le pasamos los 3 parámetros


from modulo_dibujar_caracter import rectangulo


alto = int(input("Ingrese la altura: "))
ancho = int(input("Ingrese el ancho: "))
caracter = input("Ingrese el caracter: ")

resultado = rectangulo(alto,ancho,caracter)
  
