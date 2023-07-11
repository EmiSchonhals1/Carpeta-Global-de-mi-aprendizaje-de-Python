#Creando un gráfico de bigotes usando un csv  

import pandas as pd
import matplotlib.pyplot as plt   #es una librería para visualizar datos de forma gráfica
import seaborn as sns   #es una librería que nos permite armar gráficos estadísticos

#abriendo el csv
df = pd.read_csv("Archivos_problemas_graficos_resueltos\\bigotes.csv") 
    
#creando el gráfico de bigotes
sns.boxplot(x="Categoría",y="Valor",data=df)

#mostrando el gráfico
plt.show()