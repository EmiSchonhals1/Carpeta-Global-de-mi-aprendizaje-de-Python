variable = input("Ingrese lo que desea multiplicar por 2: ")

resultado_string = variable * 2
print(f"El resultado es: {resultado_string}")  #TODOS LOS DATOS DE ENTRADA SON CONSIDERADOS STRINGS, POR ENDE SE MULTIPLICARÁ COMO STRING

#PARA PASAR ESA VARIABLE COMO INT O FLOAT LA FORMA CORRECTA DE HACERLO ES:
variable = input("Ingrese lo que desea multiplicar por 2: ")

resultado_int = int(variable) * 2
print(f"El resultado es: {resultado_int}")

#o si queremos pasarlo a float
resultado_float = float(variable) * 2
print(f"El resultado es: {resultado_float}")

















