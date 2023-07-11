#Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida una palabra y diga cuántas veces aparece esa palabra en la lista.

cant_palabras = int(input("Ingrese la cantidad de palabras: "))

lista = []
for i in range(cant_palabras) :
    palabra = input(f"Palabra {i+1}: ")
    lista += [palabra]

print(lista)

palabra_buscada = input("Ingrese la palabra que desea buscar: ")
contador = 0

for i in range(cant_palabras) :
    if (palabra_buscada == lista[i]) :
        contador = contador + 1
        
        
if (contador == 0) :
    print(f"La palabra {palabra_buscada} no aparece en la lista")
elif (contador == 1) :
    print(f"La palabra {palabra_buscada} aparece una vez en la lista")
else :
    print(f"La palabra {palabra_buscada} aparece {contador} veces en la lista")

