#programa calcule una division (dividendo y divisor), 
# si el divisor es igual a cero nos muestre un cartelito en pantalla diciendo que no puede ser 0
# solo se muestra el resultado si el divisor no es cero

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

if (divisor == 0) :
    print("No se puede dividir por cero")
else :
    resultado = dividendo / divisor
    print (f"El resultado es {resultado}")

