#Ingreso de texto y eleccion sobre que hacer con él

texto = input("Ingrese el texto que desea convertir: ")
opcion = int(input("""1:Pasar a minúsculas, 2:Pasar a mayúsculas, 
    3:Primera letra en mayus, 4:Saber cantidad de coincidencias :"""))

if (opcion == 1) :
    resultado = texto.lower()
    print (f"El resultado es: {resultado}")
elif (opcion == 2) :
    resultado = texto.upper()
    print (f"El resultado es: {resultado}")
elif (opcion == 3) :
    resultado = texto.capitalize()
    print (f"El resultado es: {resultado}")
elif (opcion == 4) :
    buscar = input("Ingrese lo que desea contar: ")
    resultado = texto.count(buscar)
    print (f"El resultado es: {resultado}")
    