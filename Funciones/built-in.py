numeros = [2, 29, 5, 6, 11, 30, 4]

#Función para encontrar el número mas grande
numero_mayor = max(numeros)
print (f"El número mas alto es el {numero_mayor}")

print ("----------------------------------------")

#Función para encontrar el número mas chico
numero_menor = min(numeros)
print (f"El número mas bajo es el {numero_menor}")

print ("----------------------------------------")

#Función para redondear a la cantidad de decimales que deseemos
redondear = round(3.14120394 , 2)  #en el 1er parámetro ponemos el número y en el 2do la cantidad de decimales que queremos que tenga
print (f"El número redondeado es {redondear}")  

print ("----------------------------------------")

#Función Bool   nos devuelve False ---> 0, vacío, False, none
#               nos devuelve True ----> distinto a 0, datos no vacíos, True, cadenas
resultado_bool_1 = bool(["Jorge", 67])
print (resultado_bool_1)

resultado_bool_2 = bool(0)
print (resultado_bool_2)

print ("----------------------------------------")

#Función All    nos devuelve True si todos los valores son verdaderos 
#comprueba todos los valores que están dentro de un iterable (lista, tupla, conjunto, etc)
resultado_all = all(["Aaron", 19, 1.87]) 
print (resultado_all)  #nos devuelve True ya que no hay un elemento que se falso

resultado_all_2 = all([0, None])
print (resultado_all_2) #nos devuelve False ya que existen elementos falsos

print ("----------------------------------------")

#Sumar todos los valores de un iterable
numero = [2, 4, 10]
resultado_sum = sum(numero)
print (resultado_sum)
