#ordenaremos el archivo.csv por horas o publicaciones, dependiendo la opción que elija el usuario

import pandas as pd

df = pd.read_csv("zzMini_Proyectoszz\\archivos2.csv\\horas.csv")

print("Ingrese la opción con la que desea ordenar el archivo.csv")
opcion = int(input("1: por horas, 2: por publicaciones : "))
sub_opcion = int(input("1: Forma Ascendente, 2: Forma Descendente : "))

if (opcion == 1) :
    if (sub_opcion == 1) :
        df = df.sort_values("Horas")
    else : 
        df = df.sort_values("Horas",ascending=False)
else :
    if (sub_opcion == 1) :
        df = df.sort_values("Publicaciones")
    else : 
        df = df.sort_values("Publicaciones",ascending=False)

print("----------------------------------------------------------------------------------")
print(df)





