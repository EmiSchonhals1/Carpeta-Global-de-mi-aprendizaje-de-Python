
#----------------------------------ABRIR EL ARCHIVO .TXT ----------------------------------------------------------------------
#para eso escribimos dentro del open la carpeta \\ archivo.txt
archivo = open("Archivos.txt\\formacion_boca.txt", encoding="UTF-8")
#ponemos encoding = "UTF-8" al final de la apertura para evitar que salgan caracteres raros durante la lectura del archivo


#----------------------------------LEER EL ARCHIVO .TXT------------------------------------------------------------------------
#LEER EL ARCHIVO COMPLETO 
#print(archivo.read())

#o también

#archivo = archivo.read()
#print(archivo)


#LEER LÍNEA POR LÍNEA CREANDO UN ARRAY CON CADA UNA DE ELLAS 
#lineas = archivo.readlines()
#print(lineas)


#LEER LA CANTIDAD DE CARACTERES QUE DESEEMOS 
#cant_caracteres = archivo.readline(10)               #en este caso nos devolverá 10 caracteres(espacios incluídos)
#print(cant_caracteres)

#-----------------------------------CERRAR EL ARCHIVO .TXT---------------------------------------------------------------------
archivo.close()








