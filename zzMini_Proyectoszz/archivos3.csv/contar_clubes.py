#contaremos la cantidad de hinchas de Boca Juniors que hay en el archivo.csv 
# y mostraremos la cantidad de filas y columnas que tiene el archivo.csv

#importamos la librería pandas
import pandas as pd

#abrimos de forma óptima el archivo.csv
df = pd.read_csv("zzMini_Proyectoszz\\archivos3.csv\\clubes.csv")

#desempaquetamos la tupla que nos devuelve df.shape con las filas y columnas del csv
filas_totales,columnas_totales = df.shape 
print(f"El archivo tiene {filas_totales} filas y {columnas_totales} columnas ")
print("-----------------------------------------------------------------------------------------")

#guardaremos todos los elementos de la columna Clubes del csv
apellidos = df.loc[:,"Clubes"]
#contará la cantidad de personas que son hinchas de Boca Juniors
cant_boca = 0
for i in range(filas_totales) :
    if (apellidos[i]=="Boca Juniors") :
        cant_boca = cant_boca + 1


if (cant_boca == 1) :
    print(f"Hay {cant_boca} hincha de Boca Juniors en el archivo.csv")
else :
    print(f"Hay {cant_boca} hinchas de Boca Juniors en el archivo.csv")







