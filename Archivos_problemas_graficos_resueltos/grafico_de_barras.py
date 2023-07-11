#Creando un gráfico de barras usando un csv  

import pandas as pd
import matplotlib.pyplot as plt   #es una librería para visualizar datos de forma gráfica
import seaborn as sns   #es una librería que nos permite armar gráficos estadísticos

#abriendo el csv
df = pd.read_csv("Archivos_problemas_graficos_resueltos\\ingresos.csv") 
    
#creando el gráfico de barras
sns.barplot(x="Fuente",y="Ingresos",data=df)

#mostrando el gráfico
plt.show()

#obteniendo el total de ingresos
total_ingresos = df['Ingresos'].sum()

#mostrando el total de ingresos
print(f"El total de ingresos es de: ${total_ingresos} USD")

