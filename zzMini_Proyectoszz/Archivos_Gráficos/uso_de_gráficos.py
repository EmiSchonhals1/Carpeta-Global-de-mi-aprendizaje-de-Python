#usaremos todos los gráficos en un mismo código

#siempre importamos las mismas librerías para gráficos
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#leemos el archivo.CSV
df = pd.read_csv("zzMini_Proyectoszz\Archivos_Gráficos\sueldos.csv")

print("Ingrese el gráfico que desea mostrar")
opcion = int(input("1: Lineal, 2: de Barras, 3: Dispersión, 4: Bigotes  : "))

if (opcion < 1 or opcion > 4) :
    print("Opción incorrecta, vuelva a ejecutar el programa")
else :
    if (opcion == 1) :
        #creando el gráfico lineal
        sns.lineplot(x="Nombre", y="Sueldo", data=df)
        #mostramos el gráfico
        plt.show()
    elif (opcion == 2) :
        #creando el gráfico de barras
        sns.barplot(x="Nombre",y="Sueldo",data=df)
        #mostramos el gráfico
        plt.show()
    elif (opcion == 3) :
        #creando el gráfico de dispersión
        sns.scatterplot(x="Nombre",y="Sueldo",data=df)
        #mostramos el gráfico
        plt.show()
    elif (opcion == 4) :
        #creando el gráfico de bigotes
        sns.boxplot(x="Nombre",y="Sueldo",data=df)
        #mostramos el gráfico
        plt.show()
    









