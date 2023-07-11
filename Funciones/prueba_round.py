num_float = float(input("Ingrese un número con coma: "))
cant_decimales = int(input("Ingrese la cantidad de decimales que desea que conserve el número: "))
print ("-----------------------------------------------------------------------------------")

num_redondeado = round(num_float , cant_decimales)
print (f"El número redondeado con {cant_decimales} decimales es: {num_redondeado}")