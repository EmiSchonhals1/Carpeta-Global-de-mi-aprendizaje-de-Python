#Nos permite, en el caso que lo deseemos, darle otro nombre más simple al módulo al que queremos acceder 
# para poder usar ese nuevo nombre cuando nos refiramos a él
#Nos ayuda sobre todo con módulos cuyo nombre es muy tedioso y largo


#importaremos el mismo módulo del programa anterior y lo nombramos como modulo para su uso en este programa
import modulo_saludar as modulo    

nombre = input("Ingrese su nombre: ")

#Al llamar una función de otro módulo debemos darle a una variable el valor del :
# Nombre_del_módulo.nombre_de_la_función(valor_que_ingresemos)
saludo = modulo.saludar(nombre)
print(saludo)



