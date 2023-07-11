#usando FILTER para iterar todos los elementos de una lista y crear una nueva lista con los valores mayores a 10 nomás

lista = []
cant_elementos = int(input("Ingrese la cantidad de elementos de la lista: "))

for i in range(cant_elementos) :
    valor = int(input(f"Número entero {i+1}: "))
    lista += [valor]


filtrado = filter(lambda x: x>10 , lista) #usamos FILTER para iterar y con lambda vamos guardando solo los números mayores a 10
print (list(filtrado)) #printeamos los resultados como lista

