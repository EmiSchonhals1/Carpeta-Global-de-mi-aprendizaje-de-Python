#Programa que devuelva True si al elevar un número al cuadrado da mayor o igual a 10, caso contrario devolver False

lambda_func = lambda x: True if x**2 >= 10 else False #función lambda

print("Ingrese 2 números")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

print (lambda_func(num1)) 
print (lambda_func(num2)) 