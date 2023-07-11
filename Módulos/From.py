#el From nos sirve para traer sólo las funciones u objetos que deseemos del módulo, 
# y no el módulo completo de forma innecesaria


#en este caso llamaremos a dos funciones que están dentro de esta carpeta
#Desde el modulo_saludar importamos las funciones saludar y bardear
from modulo_saludar import saludar,bardear

saludo = saludar("Emi")
bardo = bardear("Marcos")

print(saludo)
print(bardo)

