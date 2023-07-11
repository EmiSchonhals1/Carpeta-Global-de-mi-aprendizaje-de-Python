#PARTE A)
#Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta.
#PARTE B)
#Amplíe el programa anterior haciendo que el programa pida primero al usuario cuántas multiplicaciones se van a plantear.
#PARTE C)
#Amplíe el programa anterior haciendo que el programa lleve la cuenta de las respuestas correctas e incorrectas e indique la nota correspondiente.

import random #importamos la librería random

cant_multiplicaciones = int(input("Ingrese la cantidad de preguntas que desea contestar: "))

bien = 0
mal = 0

if (cant_multiplicaciones < 1) :
    print ("Cantidad errónea")
else :
    
    for i in range(cant_multiplicaciones) :
        num1 = random.randrange(2,11)
        num2 = random.randrange(2,11)

        resultado = num1 * num2

        result_usuario = int(input(f"Cuánto es {num1} * {num2}?: "))


        if (result_usuario == resultado) :
            print ("Respuesta correcta!")
            bien = bien + 1
        else :
            print ("Respuesta incorrecta")
            mal = mal + 1


print (f"Ha contestado correctamente {bien} preguntas")

nota = round(bien / cant_multiplicaciones * 10, 1)  #redondeamos con un solo decimal el cálculo de la nota
print (f"La nota es {nota}")