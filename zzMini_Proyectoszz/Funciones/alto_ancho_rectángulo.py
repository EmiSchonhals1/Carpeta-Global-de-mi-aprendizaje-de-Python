#Escriba un programa que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*):
#Nos debe devolver: 
#   Anchura del rectángulo: 5
#   Altura del rectángulo: 3
#   * * * * *
#   * * * * *
#   * * * * *

print ("Impresión de un Rectángulo")
def rectangulo(ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ", end="")
        print()

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
rectangulo(anchura, altura)

