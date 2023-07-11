#COMO CAMBIAR EL TIPO DE DATO DE UNA COLUMNA

#Siempre en archivos.cv debemos usar la librería pandas
import pandas as pd
df = pd.read_csv("Archivos_problemas_resueltos\datos.csv")

#Convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#Reemplazando los datos "Emi" por "Nahuel" en la columna nombres
df['nombre'].replace("Emi","Nahuel",inplace=True)
print(df['nombre'])
print("\n")

#Eliminando las filas con datos vacíos
df_no_vacio = df.dropna()
print("Dataframe sin filas con elementos vacíos")
print(df_no_vacio)
print("\n")

#Eliminando las filas con datos duplicados
df_no_duplicado = df.drop_duplicates()
print("DataFrame sin filas duplicadas")
print(df_no_duplicado)
print("\n")

#Si queremos un df totalmente limpio de filas vacías o filas duplicadas
df = df.dropna()
df = df.drop_duplicates()
print("DF totalmente clean")
print(df)

#CREANDO UN CSV CON EL DF LIMPIO DE LÍNEAS VACÍAS Y DUPLICADAS
df.to_csv("Archivos_problemas_resueltos\\datos_limpios.csv")


