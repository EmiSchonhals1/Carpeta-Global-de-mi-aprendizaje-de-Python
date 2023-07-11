#Escriba un programa que pida un número de jugadores, que pida un valor a conseguir, que tire un dado 
# para cada jugador y diga si han conseguido obtener el valor.

import random #importamos la librería random

cant_jugadores = int(input("Ingrese la cantidad de jugadores: "))

if (cant_jugadores <= 0) :
    print ("Cantidad de jugadores errónea")
else :
    valor_a_conseguir = int(input("Ingrese el valor a conseguir: "))
    if (valor_a_conseguir < 1 or valor_a_conseguir > 6) :
        print ("Valor erróneo")
        
    for i in range(cant_jugadores) :
        dado = random.randrange(1, 7)
        
        if dado == valor_a_conseguir:
            print(f"Jugador {i + 1}: {dado} CONSEGUIDO")
        else:
            print(f"Jugador {i + 1}: {dado}")












