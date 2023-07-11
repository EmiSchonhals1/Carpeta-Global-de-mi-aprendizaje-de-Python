#Importamos el módulo desde la misma ruta y carpeta

from modulo_salud import imc

kg = float(input("Ingrese su peso (kg): "))
mts = float(input("Ingrese su altura (metros): "))

resultado = imc(kg,mts)
print (resultado)



