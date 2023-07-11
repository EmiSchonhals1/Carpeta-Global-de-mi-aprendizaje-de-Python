#Escriba un programa que pida un número de dados y muestre los valores de ese número de dados, al azar.

import random  #importamos la libreria random

cant_dados = int(input("Ingrese la cantidad de dados que se usarán: "))

if (cant_dados < 1) :
    print ("Cantidad de dados errónea")
else :
    print ("Dados: ", end="")
    for i in range(cant_dados) :
        print(f"{random.randrange(1, 7)} ", end="")
    
    # random.randrange(va desde , va hasta(sin contarlo al valor))
    #el ,end="" lo usamos para que printee en forma horizontal
