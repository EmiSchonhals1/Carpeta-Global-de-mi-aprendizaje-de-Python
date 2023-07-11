
#Crear una función que nos muestre si es par o no
numeros = [1,2,3,4,5,6,7,8,9,10]

#Función común
def es_par (num) :
    if (num % 2 == 0) :
        return (True)
    
#usando filter en una función común
numeros_pares = filter(es_par,numeros)  #LA FUNCIÓN FILTER EJECUTA TODOS LOS ELEMENTOS DE UN ITERABLE
print (list(numeros_pares)) #pasamos numeros_pares como lista para que nos guarde de esa forma sólo los números pares

print ("-----------------------------------------------------------------------------------------------------------------")

#CREANDO LO MISMO QUE ANTES PERO CON LAMBDA, pero esta vez de números impares
numeros_impares = filter(lambda numero : numero % 2 == 1, numeros)
print (list(numeros_impares))












