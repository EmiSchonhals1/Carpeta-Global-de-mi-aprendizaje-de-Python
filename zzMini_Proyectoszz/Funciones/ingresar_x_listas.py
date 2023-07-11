#Escriba un programa que pida cuántas listas se quieren crear y las solicite al final del programa

#Función
def crea_lista(contador):
    print("Dígame cuántas palabras tiene la lista", str(contador) + ": ", end="")
    cant_palabras = int(input())
    lista = []
    for i in range(cant_palabras):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    return lista



#Inicio del programa
print("Generador de listas")
cant_palabras = int(input("¿Cuántas listas quiere escribir? "))

#guardamos las listas dentro de otra lista que las contiene a todas, dsp usamos un for para printearlas mediante su índice
listas = []
for i in range(1, cant_palabras + 1):
    listas += [crea_lista(i)]

for i in range(cant_palabras):
    print("La lista", i + 1, "es:", listas[i])
