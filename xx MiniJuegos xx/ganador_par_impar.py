#Escriba un programa que pida un número de dados y tire esa cantidad de dados. 
# El primer jugador obtiene un punto por cada dado par. 
# El segundo jugador obtiene un punto por cada dado impar. 
# El jugador que saque más puntos, gana

import random #importamos la librería random

print ("El jugador 1 gana un punto por cada dado par")
print ("El jugador 2 gana un punto por cada dado impar")

cant_dados = int(input("Ingrese el número de dados: "))
player1 = 0
player2 = 0

if (cant_dados < 1) :
    print ("Cantidad de dados errónea")
else :
    print ("Dados: ", end="")
    for i in range(cant_dados) :
        dado = random.randrange(1,7)
        print (f"{dado} ", end="")
        if (dado % 2 == 0) :
            player1 = player1 + 1
        else :
            player2 = player2 + 1
        

if (player1 > player2) :
    print ()
    print (f"El ganador es el jugador 1")
elif (player1 == player2) :
    print ()
    print ("Empate")
else :
    print ()
    print (f"El ganador es el jugador 2")

