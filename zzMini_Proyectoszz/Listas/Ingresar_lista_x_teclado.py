#Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y 
#luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

cant_palabras = int(input("Dígame cuántas palabras tiene la lista: "))

if (cant_palabras < 1) :
      print("La lista no debe dejarse vacía")
else:
      lista = []
      for i in range(cant_palabras):
          palabra = input(f"Dígame la palabra {i + 1}: ")
          lista += [palabra]
      print(f"La lista creada es: {lista}")

