#Escriba un programa que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*):

ancho = int(input("Ingrese el ancho: "))
altura = int(input("Ingrese la altura: "))

for i in range(altura) :
    for j in range(ancho) :
        print("p ", end="")
    print()
        
