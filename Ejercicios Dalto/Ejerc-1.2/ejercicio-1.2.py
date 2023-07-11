
frase = input("Ingrese la frase y calcularemos cuánto tardarías en decirla: ")
palabras_separadas = frase.split(" ") #separamos las palabras mediante el delimitador (en este caso el espacio en blanco)
cantidad_de_palabras = len(palabras_separadas) #con la función len() conocemos la cantidad de palabras del string

segundos_normal = cantidad_de_palabras / 2
#suponiendo q una persona normal diga dos palabras por segundo
print (f"Dijiste {cantidad_de_palabras} palabras, y tardarías {segundos_normal} segundos en decirlo")

#Si demora mas de 1 minuto con su frase
if (cantidad_de_palabras > 120) : 
    print ("Para flaco tampoco te pedí un testamento")

print("------------------------------------------------------------------------------------------------------------")
segundos_dalto =segundos_normal - (cantidad_de_palabras / 2) * 0.3
print (f"Dalto lo diría en {segundos_dalto} segundos")




