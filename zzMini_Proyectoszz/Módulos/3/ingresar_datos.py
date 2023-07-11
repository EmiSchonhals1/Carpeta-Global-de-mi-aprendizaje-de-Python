#importamos la función ficha para crear una ficha personal y la función lista para crear una lista con los datos
from modulo_datos import ficha,lista
#importamos la función num_random del modulo_nro_random
from modulo_nro_random import num_random

#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))
#dni = input("Ingrese su DNI: ")
#telefono = input("Ingrese su teléfono: ")
#direccion = input("Ingrese su dirección: ")
#tope = int(input("Ingrese el tope que tendrá el número random: "))

#datos para las funciones ficha y lista
nombre = "Emiliano Schonhals"
edad = "19"
dni = "44702037"
telefono = "343 4258024"
direccion = "Hilario de la Quintana 1297 bis"
#dato para la función num_random
tope = 10

print("-----------------------------------------------------------------------------")
#mostramos los datos en formato ficha
print (ficha(nombre,edad,dni,telefono,direccion))
print("-----------------------------------------------------------------------------")
#mostramos los datos en formato lista
print(lista(nombre,edad,dni,telefono,direccion))
print("-----------------------------------------------------------------------------")
#mostramos el nro random
resultado = num_random(tope)
print(f"Su número random entre el 1 y el {tope} es {resultado}")


