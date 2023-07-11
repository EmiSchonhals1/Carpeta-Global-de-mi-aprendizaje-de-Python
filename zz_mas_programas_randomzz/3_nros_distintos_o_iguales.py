#Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales 
# o si son los tres distintos

print ("COMPARADOR DE NÚMEROS")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
print ("---------------------")

if (num1 == num2 == num3) :
    print ("Los 3 números son iguales")
elif (num1 == num2 != num3 or num1 == num3 != num2 or num2 == num3 != num1) :
    print ("Dos de los números son iguales")
else :
    print ("Los 3 números son distintos")

