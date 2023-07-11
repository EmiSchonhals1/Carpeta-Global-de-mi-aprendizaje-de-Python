#Usaremos la función que se encuentra en el módulo saludar

import modulo_saludar #importamos el módulo

#Al llamar una función de otro módulo debemos darle a una variable el valor del :
# Nombre_del_módulo.nombre_de_la_función(valor_que_ingresemos)
saludo = modulo_saludar.saludar("Emi")
print (saludo)
