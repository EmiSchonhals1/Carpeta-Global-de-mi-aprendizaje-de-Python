#Escriba un programa que pida un número de jugadores y tire un dado para cada jugador.

import random #importamos la librería random

cant_jugadores = int(input("Ingrese la cantidad de jugadores: "))

if (cant_jugadores <= 0) :
    print ("Cantidad de jugadores errónea")
else :
    for i in range(cant_jugadores) :
        print (f"Jugador {i+1}: {random.randrange(1,7)}")  
         #nos devolverá un valor random entre 1 y 6
