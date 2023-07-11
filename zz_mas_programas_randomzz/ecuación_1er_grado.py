#Escriba un programa que pida los coeficientes de una ecuación de primer grado (ax + b = 0) y escriba la solución
#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos 
# los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a

print ("CALCULADORA DE ECUACIÓN DE 1ER GRADO")
a = float(input("ingrese el valor del coeficiente a: "))
b = float(input("ingrese el valor del coeficiente b: "))

if (a == b == 0) :
    print ("Todos los números son solución")
elif (a == 0) :
    print ("La ecuación no tiene solución")
else: 
    solucion = -b / a
    print (f"La solución es {solucion}")  

