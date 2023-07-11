#Importando las 3 librerías que usamos siempre para gráficos
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#leyendo el archivo.CSV
df = pd.read_csv("zzMini_Proyectoszz\\Archivos_Gráficos\\ejer1\\ventas_de_junio.csv")

#creando el gráfico de bigotes
sns.boxplot(x="Club", y="Ventas en Junio", data=df)

#Mostrando el gráfico
plt.show()

#calculando cuanto dinero ingresó a los clubes argentinos
total = df['Ventas en Junio'].sum()
print(f"Ingresaron ${total} a los clubes argentinos en el mercado de Junio")



