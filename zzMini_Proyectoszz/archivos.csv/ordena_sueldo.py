#Ordenaremos los sueldos del archivo.csv y mostraremos las 3 personas que tengn mejor sueldo

import pandas as pd

df = pd.read_csv("zzMini_Proyectoszz\\archivos.csv\\sueldos.csv")

print("\n")
print("LISTADO DE SUELDOS ")
print(df)
print("-------------------------------------------------------------------------------------")

print("LAS 3 PERSONAS QUE MAS COBRAN SON ")
#ordenamos de forma DESCENDENTE
sueldo_ordenado = df.sort_values("Sueldo",ascending=False)

#mostramos los 3 sueldos mas altos
print(sueldo_ordenado[0:3])







