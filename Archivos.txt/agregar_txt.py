#ponemos la "a" de Append dentro del with open para poder agregar líneas al archivo.txt sin borrar los datos anteriores del mismo
with open("Archivos.txt\\archivo_agregado.txt", "a", encoding = "UTF-8") as archivo :
    
    #podemos usar las mismas operaciones que usabamos en el "w", con la diferencia de que al poner la "a" nos lo agregará 
    #sin eliminar todos los datos anteriores del archivo.txt
    
    #podemos usar un Bucle para agregar la cantidad de líneas que deseemos
    archivo.write("\n") #para que al inicio nos de un salto de línea si es que hay algo antes de lo que agregamos
    for i in range(5) :
        archivo.write(f"Línea {i+1} agregada \n")
        
    


















