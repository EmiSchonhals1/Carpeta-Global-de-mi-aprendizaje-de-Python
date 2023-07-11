diccionario = {
    "nombre" : 'Emiliano',
    "apellido" : 'Schonhals',
    "edad" : 19
}

claves = diccionario.keys()  #nos devuelve las claves en forma de TUPLA, tmb sirve para iterar
print (claves)

devuelve_valor = diccionario.get("nombre")  #nos devuelve el valor que le solicitemos
print (devuelve_valor)

diccionario.clear() #elimina todos los elementos del diccionario
print (diccionario)

diccionario.pop("nombre")  #elimina el valor elegido
print (diccionario)

diccionario_iterable = diccionario.items()  #devuelve dict_items iterables
print (diccionario_iterable)


