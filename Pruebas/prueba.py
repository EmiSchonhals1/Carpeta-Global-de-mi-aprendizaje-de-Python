#Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if (num1 > num2) :
    print(f"{num1} es mayor que {num2}")
elif (num2 > num1) :
    print(f"{num2} es mayor que {num1}")
else :
    print("Ambos números son iguales")



