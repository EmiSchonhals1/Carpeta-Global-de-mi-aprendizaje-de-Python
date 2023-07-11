#programa que encuentre el menor número y lo redondee con la cantidad de números después de la coma que deseemos

cant_elementos = int(input("Ingrese la cantidad de elementos de la lista: "))
lista = []

print (f"Ingrese {cant_elementos} números con coma")
for i in range(cant_elementos) :
    nro = float(input(f"número {i+1}: "))
    lista += [nro]
    
print ("---------------------------------------------------------------------------------------")
numero_menor = min(lista)
print (f"El menor número es el {numero_menor}")

print ("---------------------------------------------------------------------------------------")
num_dsp_coma = int(input("Ingrese la cantidad de números después de la coma: "))
redondear = round(numero_menor, num_dsp_coma)
print (f"El número ahora es {redondear}")

