#Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.
print("Ingrese dos números enteros")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

if (num1 > num2) :
    print (f"{num1} es mayor que {num2}")
elif (num1 < num2) :
    print (f"{num1} es menor que {num2}")
else :
    print ("Ambos números son iguales")
