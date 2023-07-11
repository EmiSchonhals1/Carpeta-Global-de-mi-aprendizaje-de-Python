#A)	Pedir nombre y edad de los compañeros que fueron a clase y ordenar los datos de menor a mayor
#B)	El mayor es el profesor y el menor es el asistente, ¿quién es quién?

def obtener_compañeros (cant_compañeros) :
    compañeros = []
    for i in range(cant_compañeros) :
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        #hacemos que persona sea una tupla y luego la agregamos dentro de la lista principal con .append para dsp ordenarla por edad
        persona = (nombre, edad) 
        compañeros.append(persona) #.append agrega elementos a la lista, uno detras de otro
    
    #ordenando por edad
    compañeros.sort(key = lambda x: x[1]) #.sort crea un iterable que ordena la key que le pongamos, en este caso 
                                            #el índice 1 de compañeros, osea por la edad

   
    #como tiene tuplas dentro una lista, el primer índice es la tupla y el segundo es el elemento que queremos de esa tupla
    asistente = compañeros[0][0] #primer tupla, primer elemento de ella (ya que la ordenamos de menor a mayor)
    profesor = compañeros[-1][0] #última tupla, primer elemento de ella
    
    #retornamos los valores que necesitamos, en este caso una tupla
    return (asistente, profesor)


#INICIO DEL PROGRAMA
numero = int(input("Ingrese la cantidad de compañeros que fueron a la clase: "))

#llamamos a la función y desempaquetamos los valores de la tupla
asistente,profesor = obtener_compañeros(numero)

#printeamos los resultados
print(f"El profesor es {profesor} y su asistente es {asistente}")
    
