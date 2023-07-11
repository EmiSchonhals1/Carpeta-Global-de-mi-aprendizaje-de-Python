#Programa para mostrar datos de un alumno y un promedio de sus respectivas notas

def alumno (nya,*notas) :
    suma = (sum(*notas)) / cant_notas
    #promedio = suma / cant_notas
    print (f"{nya} su promedio es de {list(suma)}")



nombre = input("Ingrese su nombre y apellido: ")
años = int(input("Ingrese su edad: "))
cant_notas = int(input("Ingrese la cantidad de notas que ingresará: "))
for i in range(cant_notas) :
    evaluaciones = []
    valor = float(input(f"Nota {i+1}: "))
    evaluaciones += [valor]


ficha = alumno(nombre, evaluaciones)


ARREGLAR PROBLEMA AL INTENTAR PROMEDIAR






