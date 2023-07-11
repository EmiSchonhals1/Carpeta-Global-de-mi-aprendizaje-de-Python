#Recorriendo la lista animales
animales = ["perro", "gato", "loro", "cocodrilo"]

for animal in animales :         #FOR se ejecuta tantas veces como elementos tenga
    print (animal)

#Recorrer una lista por su índice (IMPORTANTE POR QUE CREA UNA TUPLA CON EL INDICE Y EL VALOR SEPARADOS)
numeros = [4, 6, 8, 10]
for nro in enumerate(numeros) :    #La función ENUMERATE() nos genera una tupla de dos elementos
    indice = nro[0]    #en el parámetro 0 se guardan los índices
    valor = nro[1]     #en el parámetro 1 se guradan los valores
    print (f"El índice {indice} contiene el valor {valor}")



#Recorriendo la lista números y multiplicando sus elementos por 10
for num in numeros :
    resultado = num * 10
    print (f"{num} * 10 es {resultado}")


#Para iterar ambas listas juntas, ambas deben tener la misma cantidad de elementos
#Usamos la función zip(lista1 , lista2)
for animal,num in zip(animales,numeros) :
    print (f"Recorriendo lista 1: {animal}")
    print (f"Recorriendo lista 2: {num}")


#USO DEL ELSE
for nro in numeros :
    print (f"los números son: {nro}")
else: print ("El bucle se terminó")



