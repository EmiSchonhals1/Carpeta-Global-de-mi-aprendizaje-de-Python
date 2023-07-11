#Ésta es la forma óptima de leer archivos.CSV

import pandas as pd  #pd es la sigla universal con la que se conoce a la librería pandas

#usamos la funcion read_csv para leer el archivo.CSV
df = pd.read_csv("Archivos.csv\\datos.csv")
#ponemos df (DATA FRAME), son estructuras de datos bidimensionales parecidos a una hoja de cálculo
#por ende tiene sólo dos valores: Filas y Columnas, las cuales podemos usar para mostrar datos específicos del csv

#mostrando la columna nombre----------------------------------------------------------------------
print("Columna Nombre")
print(df["nombre"])
print("\n")

#ordenando por la columna edad de forma ASCENDENTE------------------------------------------------
df_ordenado = df.sort_values("edad")
print("Ordenado de forma ascendente")
print(df_ordenado)
print("\n")

#IMPORTANTE: Para poder usar ésta función, NO debemos dejar ningún espacio en blanco luego de cada coma en el archivo.csv,
# sino nos devolverá errores de la librería pandas

#ordenando por la columna edad de forma DESCENDENTE-----------------------------------------------
df_ordenado_descendente = df.sort_values("edad", ascending=False)
print("Ordenado de forma descendente")
print(df_ordenado_descendente)
print("\n")


#concatenando dos dataframes----------------------------------------------------------------------
df2 = pd.read_csv("Archivos.csv\\datos.csv")

df_concatenado = pd.concat([df,df2])
print("Dataframes concatenados")
print(df_concatenado)
print("\n")

#accediendo a las primeras 3 líneas del dataframe-------------------------------------------------
primeras_lineas = df.head(3)
print("Primeras 3 líneas del dataframe")
print(primeras_lineas)
print("\n")

#accediendo a las últimas dos líneas del dataframe------------------------------------------------
ultimas_lineas = df.tail(2)
print("Últimas 2 líneas del dataframe")
print(ultimas_lineas)
print("\n")

#saber la cantidad de filas y columnas con shape--------------------------------------------------
filas_y_columnas_totales = df.shape
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]

#otra forma es usar el desempaquetado
filas_totales,columnas_totales = df.shape

#acceder a un elemento específico del dataframe---------------------------------------------------
elemento_especifico_loc = df.loc[2,"apellido"]
#o
elemento_especifico_iloc = df.iloc[2,2]

#acceder a todas las filas de una columna del dataframe-------------------------------------------
#usamos el slicing para indicar que accederemos a todas las filas de esa columna
apellidos = df.loc[:,"apellido"]
#o
apellidos = df.iloc[:,2]

#acceder a todas las columnas de una fila del dataframe-------------------------------------------
fila_3 = df.loc[2,:]
#o
fila_3 = df.iloc[2,:]  #en este caso no varía

#Mostrar las filas que cumplan una condición------------------------------------------------------
#fila con edad mayor que 25
mayor_que_25 = df.loc[df["edad"], :]






