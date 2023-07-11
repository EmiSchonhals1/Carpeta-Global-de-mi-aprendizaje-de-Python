#Escriba un programa que pida la cantidad de números positivos que se tienen que escribir y a continuación 
# pida números hasta que se haya escrito la cantidad de números positivos indicada.

cant_numeros = int(input("Ingrese la cantidad de números positivos a ingresar: "))
contador = 1

while (contador <= cant_numeros) :
    numero = int(input("Número: "))
    if (numero >= 0) :
        contador = contador + 1
    

print (f"YA SE INGRESARON LOS {cant_numeros} NÚMEROS POSITIVOS")

