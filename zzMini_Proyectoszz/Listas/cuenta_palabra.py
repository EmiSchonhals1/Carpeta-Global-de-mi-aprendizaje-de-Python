#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra 
#y diga cuántas veces aparece esa palabra en la lista.

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
      print("¡Imposible!")
else:
      lista = []
      for i in range(numero):
          palabra = input(f"Dígame la palabra {i + 1}: ")
          lista += [palabra]
      print(f"La lista creada es: {lista}")

      buscar = input("Dígame la palabra a buscar: ")
      contador = 0
      for i in lista:
          if i == buscar:
              contador += 1
      if contador == 0:
          print(f"La palabra '{buscar}' no aparece en la lista.")
      elif contador == 1:
          print(f"La palabra '{buscar}' aparece una vez en la lista.")
      else:
          print(f"La palabra '{buscar}' aparece {contador} veces en la lista.")
