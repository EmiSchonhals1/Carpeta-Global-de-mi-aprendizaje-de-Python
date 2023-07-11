#ponemos la "w" de WRITE dentro del open para indicar que tendremos permisos de escritura
with open("Archivos.txt\\archivo_reescrito.txt", "w", encoding = "UTF-8") as archivo :

    #reescribiendo un archivo.txt
    #archivo.write("Hola que tal")
    
    #reescribiendo un archivo.txt usando arrays o iterables
    #Es la operación contraria al readlines(), ya que permite que escribamos un array línea por línea en el archivo
    archivo.writelines(["Hola Máquina, todo bien? \n", "Yo ando bien \n", "Al menos hasta que vea a Boca"])
    #Ponemos \n para indicar que hay un salto de línea
    
    
    











