#Creando una lista con función LIST(), no es lo mas común igual hacerlo de esta forma
lista = list(["Emiliano","Schonhals",19])
print (lista)

#Saber la cantidad de elementos de una lista 
cantidad_elementos = len(lista)
print (cantidad_elementos)

#MÉTODOS PARA AGREGAR ELEMENTOS
#Agregar elementos a la lista
lista.append("Soy de boca")   #con .append(" ") nos lo agregará en la última posición 
print (lista)

#Agregar elementos a la lista en un índice especificado
lista.insert(1, "Axel")
print (lista)

#Agregar varios elementos a la lista
lista.extend(["Boca Juniors", 44702037])
print (lista)

#MÉTODOS PARA ELIMINAR ELEMENTOS
#Eliminar un elemento por su índice (elimina el elemento que esté en ese índice)
lista.pop(0)  #Si en el índice ponemos -1 eliminará el ÚLTIMO elemento de la lista
print (lista) #Si en el índice ponemos -2 nos eliminará el ANTEÚLTIMO elemento de la lista, y asi sucesivamente

#Eliminar un elemento de la lista por su valor, si lo encuentra lo elimina
lista.remove("Boca Juniors")
print (lista)

#Eliminar todos los elementos de la lista
#lista.clear()
#print (lista)

#Ordenar elementos (NO FUNCIONA CON STRINGS)
#de forma descendente:
lista.sort()
print (lista)
#de forma ascendente:
lista.sort(reverse=True)
print (lista)

#Invertir los elementos de una lista
lista.reverse()
print (lista)


#Verificar si un elemento se encuentra en la lista
elemento_encontrado =lista.index("Emiliano")   #nos devolverá el índice donde se encuentra (en caso de que exista ese elemento en la lista)
print (elemento_encontrado)








