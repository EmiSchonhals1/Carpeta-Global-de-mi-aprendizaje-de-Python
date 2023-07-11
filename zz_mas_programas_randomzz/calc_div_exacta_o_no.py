#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no

print ("------------------------------------------------------------------")
print ("Ingrese dos números enteros para dividirlos")
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

if (divisor == 0) :
    print ("No se puede dividir por cero")
else :
    cociente = dividendo // divisor
    resto = dividendo % divisor

    if (resto == 0) :
        print (f"La división es exacta, cociente: {cociente} resto: {resto}")
    else :
        print (f"La división no es exacta, cociente: {cociente} resto: {resto}")

print ("------------------------------------------------------------------")
