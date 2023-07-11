
from modulo_operaciones import suma,resta,multip,div

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
opcion = input("Ingrese la operación que desea realizar (+,-,*,/): ")

if (opcion == "+") :
    resultado = suma(num1,num2)
elif (opcion == "-") :
    resultado = resta(num1,num2)
elif (opcion == "*") :
    resultado = multip(num1,num2)
elif (opcion == "/") :
    resultado = div(num1,num2)
else :
    print ("Opción incorrecta")

print("-----------------------------------------------------------------------------")
print(f"El resultado es {resultado}")

