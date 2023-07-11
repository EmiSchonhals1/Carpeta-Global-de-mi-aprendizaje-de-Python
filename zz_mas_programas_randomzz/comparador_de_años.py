#Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años 
# han pasado desde ese año o cuántos años faltan para llegar a ese año.

print ("COMPARADOR DE AÑOS")
año_actual = int(input("Ingrese el año actual: "))
año_elegido = int(input("Ingrese el año elegido: "))

if (año_actual < año_elegido) :
    diferencia = año_elegido - año_actual
    print (f"Faltan {diferencia} años para llegar al {año_elegido}")
elif (año_actual > año_elegido) :
    diferencia = año_actual - año_elegido
    print (f"Han pasado {diferencia} años desde el {año_elegido}")
else :
    print ("Ambos años son iguales") 
