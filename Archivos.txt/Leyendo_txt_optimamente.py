
#FORMA ÓPTIMA DE TRABAJAR CON ARCHIVOS .TXT
with open("Archivos.txt\\formacion_boca.txt", encoding="UTF-8") as archivo :
    #dentro ejecutamos todo lo que necesitemos
    print(archivo.read())
    
    #el archivo se cierra de forma automática


