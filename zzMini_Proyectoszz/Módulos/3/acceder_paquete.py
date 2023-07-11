#accederemos al paquete
import paquete.modulo_salud as salud
import paquete.modulo_edad as años

peso = 86
altura = 1.87
edad = int(18)

#accedemos a la función imc del modulo_salud
resultado = salud.imc(peso,altura)
print(resultado)
#accedemos a la función mayor_de_edad del modulo_edad
resultado2 = años.mayor_de_edad(edad)
print(resultado2)


