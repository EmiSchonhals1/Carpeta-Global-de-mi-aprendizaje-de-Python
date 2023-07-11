#Escriba un programa que pida la anchura y altura de un rectángulo y el caracter a utilizar en el dibujo

altura = int(input("Ingrese la altura del rectángulo: "))
anchura = int(input("Ingrese la anchura del rectángulo: "))
caracter = input("Ingrese el caracter que desea utilizar para la impresión: ")

def rectangulo(alto,ancho,carac) :
    for i in range(altura) :
        for j in range(anchura) :
            print (carac, end="  ") #el end nos sirve para darle espacios entre los caracteres dsp de imprimir cada caracter
        print()

resultado = rectangulo(altura,anchura,caracter)
print (resultado)
