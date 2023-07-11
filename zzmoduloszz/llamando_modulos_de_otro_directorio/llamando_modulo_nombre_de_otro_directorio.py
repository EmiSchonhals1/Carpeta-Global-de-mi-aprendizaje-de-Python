#programa que importa los módulos saludar y bardear de otra carpeta diferente

#para usar módulos de otras carpetas debemos importar sys
import sys

sys.path.append("C:\\Users\\ASUS\\Desktop\\Carpetas VSC Python\\Módulos\\modulo_saludar")

import saludar as saludo, bardear as bardo

nombre = input("Ingrese el nombre que desea usar: ")
print("Ingrese la opción que desea elegir")
opcion = int(input("Saludar:1, Bardear:2   : "))

if (opcion == 1) :
    #resultado = saludo(nombre)
    #print(resultado)
    print(saludo(nombre))
elif (opcion == 2) :
    #resultado = bardo(nombre)
    #print(resultado)
    print(saludo(nombre))
else :
    print("Opción incorrecta, vuelva a ejecutar ")



