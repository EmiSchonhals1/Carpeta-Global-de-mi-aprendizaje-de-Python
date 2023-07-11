#Importamos la librería CSV
import csv

#Abrimos los archivos .CSV de la misma forma que los archivos txt
with open("Archivos.csv\\datos.csv", encoding="utf-8") as archivo :
    leer = csv.reader(archivo)
    #nos devuelve un iterable, por ende lo podemos recorrer
    for filas in leer :
        print (filas)
        #nos está devolviendo listas con las filas del archivo.CSV
















