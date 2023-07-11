
cant_elementos = int(input("Ingrese la cantidad de elementos de la lista: "))
lista = []

for i in range(cant_elementos) :
    numero = int(input("ingrese un número entero: "))
    lista += [numero]
    
print (f"La lista es: {lista}")
print ("-----------------------------------------------------------------")
    
print ("Ingrese lo que desea ver en pantalla")
opcion = int(input("1:Número Mayor  2:Número Menor  : "))  

if (opcion == 1) :
    num_mayor = max(lista)
    print (f"El número mas grande de la lista es el {num_mayor}")
elif (opcion == 2) :
    num_menor = min(lista)
    print (f"El número mas chico de la lista es el {num_menor}")
else :
    print ("Opción inválida")
    