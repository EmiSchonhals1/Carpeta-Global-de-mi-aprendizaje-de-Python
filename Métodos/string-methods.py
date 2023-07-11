cadena = "Emiliano, Schonhals"

print (dir(cadena))  #la función DIR nos permite ver que podemos hacerle a un string determinado

#LOS METODOS SON CONSIDERADOS ASI CUANDO SE ESCRIBEN dato.metodo()
#LAS FUNCIONES SON CONSIDERADAS ASI CUANDO SE ESCRIBEN funcion(dato)
#LOS MÉTODOS SON FUNCIONES PERO LAS FUNCIONES NO SIEMPRE SON MÉTODOS

#Método para pasar un string a Mayúsculas    
mayus = cadena.upper()
print (mayus)
         # o también 
mayus2 = "hola que tal".upper()
print (mayus2)

#Pasar un string a minúsculas               
minus = cadena.lower()
print (minus)

#Primera letra en mayúscula                 
primer_letra_mayus = cadena.capitalize() #1ro convierte todo el string a minúscula y luego pone en mayúscula solo la primer letra del string 
print (primer_letra_mayus)

#Buscar una cadena dentro de otra            
busqueda_find = cadena.find("ilia")
print (busqueda_find)   #SI NOS RETORNA -1 SIGNIFICA QUE NO SE ENCUENTRA LA CADENA, CASO CONTRARIO NOS RETORNARÁ LA POSICION DONDE SE ENCUENTRA

#Otra forma de buscar dentro de otra cadena     
busqueda_index = cadena.index("jose")
print (busqueda_index)   #Funciona igual que el método .find(“ ”), pero si no encuentra resultados en vez de devolvernos -1 nos devolverá una excepción en forma de error

#Saber si el string contiene sólo números    
es_numerico = cadena.isnumeric()
print (es_numerico)  #Si es numérico nos devuelve TRUE, caso contrario nos devuelve FALSE

#Saber si el string es Alfanumérico           
es_alfanumerico = cadena.isalpha()
print (es_alfanumerico)  #Si es alfanumérico devuelve TRUE, caso contrario devuelve FALSE

#Contar coincidencias      
contar_coincidencias = cadena.count("i")
print (contar_coincidencias)  #devuelve la cantidad de coincidencias

#Contamos cuantos caracteres tiene una cadena      
contar_caracteres = len(cadena)
print (contar_caracteres)

#Saber si una cadena empieza con...            
empieza_con = cadena.startswith("E")
print (empieza_con)

#Saber si una cadena termina con...            
termina_con = cadena.endswith("no")
print (termina_con)

#Reemplaza un pedazo de la cadena dada por otra cadena dada, en caso de no encontrar coincidencias nos devolverá la cadena anterior
cadena_nueva = cadena.replace("liano","to")
print (cadena_nueva)

#Separar cadenas por las cadenas que les pasemos
cadena_separada = cadena.split(",")  #Nos devuelve una lista con las cadenas separadas mediante los delimitadores ingresados
print (cadena_separada)