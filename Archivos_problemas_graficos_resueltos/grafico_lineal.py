#Creando un gráfico lineal usando un csv con las fechas y cantidad de bostezos de ese día 

import pandas as pd
import matplotlib.pyplot as plt   #es una librería para visualizar datos de forma gráfica
import seaborn as sns   #es una librería que nos permite armar gráficos estadísticos

#abriendo el csv
df = pd.read_csv("Archivos_problemas_graficos_resueltos\\bostezos.csv") 
    
#creando el gráfico lineal
sns.lineplot(x="Fecha",y="Bostezos",data=df)

#creando un punto de forma manual, en este caso en el momento de más bostezos
plt.plot("05/03",7,"o")

#mostrando el gráfico
plt.show()





