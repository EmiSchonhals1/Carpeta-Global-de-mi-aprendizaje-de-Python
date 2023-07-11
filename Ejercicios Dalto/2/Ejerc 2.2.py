#Crear una función que nos devuelva los números primos entre 0 y el valor que ingresemos

#creamos la función que verifica qué números son primos
def es_primo (num) :
    #verificamos que el número anterior no pueda dividirse por ningún número entre el 2 y el mismo número
    for i in range(2 , num-1) :
        #si es divisible por alguno retornamos False 
        if (num%i==0) :
            return False
    
    #si no fue divisible retornamos True
    return True


#creamos otra función para que cree una lista con todos los números primos
def primos_hasta(num) :
    #creamos la lista
    primos = []
    for i in range (2, num+1) :
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea primo lo agregamos a la lista
        if (resultado == True) :
            primos.append(i)
            
    #devolvemos la lista
    return primos



#INICIO DEL PROGRAMA
print("Se mostrarán todos los números primos entre el 2 y el número que ingrese")
numero = int(input("Ingrese el número: "))

#llamada a la función 
resultado = primos_hasta(numero)
#printeo final
print (resultado)
