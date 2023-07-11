#Para trabajar con expresiones regulares importamos la librería re
import re

#para que el string tenga varias líneas usamos TRIPLE COMILLAS SIMPLES
texto = '''Hola maestro, esta es la cadena 1. Como estás?
Esta es la línea 278 de texto.
Y esta es la última línea, la 7876. '''

#BÚSQUEDA SIMPLE----------------------------------------------------------------------------------------------------
#si queremos que nos diga si encuentra la coincidencia en el string
#resultado = re.search("esta", texto)

#si queremos que nos encuentre y devuelva todas las coincidencias que hay en el string
#resultado = re.findall("esta", texto)
#print(resultado)

#El problema surge cuando están las mismas coincidencias pero varían las mayúsculas
#En ese caso ponemos: 
#resultado_sin_importar_mayus = re.findall("esta", texto, flags=re.IGNORECASE)
#print(resultado_sin_importar_mayus)

# \d --> busca todos los dígitos numéricos del 0 al 9--------------------------------------------------------------
resultado1 = re.findall(r"\d", texto)
#print(resultado1)

# \D --> busca TODO MENOS dígitos numéricos del 0 al 9-------------------------------------------------------------
resultado2 = re.findall(r"\D", texto)
#print(resultado2)

# \w --> busca todos los caracteres alfanuméricos (a-z  A-Z  0-9  _ )----------------------------------------------
resultado3 = re.findall(r"\w", texto)
#print(resultado3)

# \W --> busca TODO MENOS caracteres alfanuméricos-----------------------------------------------------------------
resultado4 = re.findall(r"\W", texto)
#print(resultado4)

# \s --> busca todos los espacios en blanco (espacios, tabs, saltos de línea)--------------------------------------
resultado5 = re.findall(r"\s", texto)
#print(resultado5)

# \s --> busca TODO MENOS los espacios en blanco-------------------------------------------------------------------
resultado6 = re.findall(r"\S", texto)
#print(resultado6)

# \n --> busca todos los saltos de línea---------------------------------------------------------------------------
resultado7 = re.findall(r"\n", texto)
#print(resultado7)

# . --> busca TODO MENOS los saltos en línea-----------------------------------------------------------------------
resultado8 = re.findall(r".", texto)
#print(resultado8)

# \ --> cancela todos los caracteres especiales (los que no son alfanuméricos)-------------------------------------
#cancelando la función del punto y buscando puntos
resultado9 = re.findall(r"\.", texto)
#print(resultado9)


#BUSCANDO UNA EXPRESIÓN REGULAR COMPUESTA--------------------------------------------------------------------------
#en este caso, buscaremos un patrón o coincidencia en el texto en el que haya un nro, luego un punto y luego un espacio
#al buscar un string que cumpla esas condiciones ponemos f en vez de r
resultado10 = re.findall(f"\d\.\s", texto)
#print(resultado10)

# ^ --> el acento circunflejo o v invertida busca el comienzo de una línea-----------------------------------------
#usamos Alt + 94 para ponerlo
#buscando si "Esta" está al principio de la primer línea
resultado11 = re.findall(r"^Esta", texto)
#print(resultado11)

#si queremos saber si está en alguna de TODAS las líneas debemos poner flags= re.M
resultado11 = re.findall(r"^Esta", texto, flags=re.M)
#print(resultado11)

# $ --> busca el final de una línea o de todas las líneas (en el caso de que usemos el parámetro flags= re.M)
resultado12 = re.findall(r"texto.$", texto, flags=re.M)
#en este caso debemos incluir el punto ya que no termina en la palabra texto, sino que termina con texto.
#print(resultado12)

# {n} --> busca n cantidad de coincidencias consecutivas del valor que pongamos a su izquierda----------------------
#en este caso buscamos en el texto 3 números consecutivos
resultado13 = re.findall(r"\d{3}", texto)
#print(resultado13)

# {n,m} --> {n,m}: busca mínimo n y máximo m coincidencias----------------------------------------------------------
#en este caso buscamos que haya entre 1 y 4 números juntos en el texto
resultado14 = re.findall(r"\d{1,4}", texto)
#print(resultado14)

# | --> Con que alguna de las dos opciones que le demos se cumpla nos la devolverá
resultado15 = re.findall(r"\d{1,4}|Hola", texto)
#print(resultado15)

