print ("PROGRAMA PARA CALCULAR")

def calcular(opcion, num1, num2) :
    if (opcion == 1) :
        resultado = num1 + num2
        print (f"El resultado es {resultado}")
    elif (opcion == 2) :
        resultado = num1 - num2
        print (f"El resultado es {resultado}")
    elif (opcion == 3) :
        resultado = num1 * num2
        print (f"El resultado es {resultado}")
    elif (opcion == 4) :
        resultado = num1 / num2
        print (f"El resultado es {resultado}")
    
        
print ("1:Suma, 2:Resta, 3:Multiplicación, 4:División")
decision = "y" #Para que entre por primera vez al bucle
while (decision == "y") :
    opcion = int(input("Ingrese la opción que desee: "))
    
    if (opcion !=1 and opcion !=2 and opcion !=3 and opcion !=4) : 
        print("Opción incorrecta, vuelva a ejecutar el programa")
        break   #Si se ingresa una opcion incorrecta se cerrara el programa
    
    num1 = float(input("Ingrese el 1er número: "))
    num2 = float(input("Ingrese el 2do número: "))

    calcular(opcion, num1, num2) #Llamada a la función con sus parámetros
    
    decision = input("Desea realizar otra operación? y/n: ")
    decision = decision.lower() #por si ingresa la opcion en Mayúsculas
