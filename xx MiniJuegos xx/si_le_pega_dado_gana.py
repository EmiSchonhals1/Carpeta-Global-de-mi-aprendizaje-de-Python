#Escriba un programa que pida un número de dados, que pida un valor a conseguir y que tire 
# después el número de dados indicado. El jugador gana si saca el valor ganador

import random #importamos la librería random

cant_dados = int(input("Ingrese la cantidad de dados a utilizar: "))
band = 0

if (cant_dados < 1) :
    print ("Cantidad de dados errónea")
else :
    objetivo = int(input("Ingrese el valor a conseguir: "))
    
    if (objetivo < 1 or objetivo > 6) :
        print ("Valor erróneo")
    else :
        print(f"Dados: ", end="") #usamos ,end="" para que los valores salgan en el mismo renglón
        for i in range(cant_dados) :
            dado = random.randrange(1,7)
            print (f"{dado} ", end="")
            if (dado == objetivo) :
                band = 1
    


if (band == 1):
    print ("") #para que el mensaje alusivo salga abajo de los dados y no en el mismo renglón
    print ("El jugador ha ganado!")
else :
    print ("")
    print ("El jugador ha perdido")
