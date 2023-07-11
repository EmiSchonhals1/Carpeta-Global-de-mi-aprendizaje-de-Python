
diccionario = {
    'nombre' : "Emiliano",
    'apellido' : "Schonhals",
    'altura' : 1.87,
    'peso' : 87
}

for datos in diccionario.items() :
    key = datos[0]
    value = datos[1]
    print (f"El índice es {key} y el dato es {value}")
